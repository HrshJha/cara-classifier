# scorer.py — Scoring engine for CARA classifier

from framework import CLUSTERS, DEGREES, TRACKS


def score_clusters(subjects):
    """
    Maps candidate subjects to subject clusters (C1-C10) and returns
    a degree score dict showing how strongly each degree is supported
    by the candidate's academic background.

    Returns: { "MHA": float, "MPH": float, "MSHI": float, "MBA-HC": float }
    """
    degree_scores = {d: 0 for d in DEGREES}
    subject_lower = [s.lower() for s in subjects]

    for cluster_id, cluster in CLUSTERS.items():
        matches = [s for s in subject_lower if s in cluster["subjects"]]
        for match in matches:
            for degree in cluster["degrees"]:
                degree_scores[degree] += 1

    # Normalize to 0-1
    max_score = max(degree_scores.values()) if max(degree_scores.values()) > 0 else 1
    return {d: round(v / max_score, 4) for d, v in degree_scores.items()}


def score_sop(sop_text):
    """
    Scans the SOP text for track-specific keywords and returns a
    normalized score per track showing how strongly the SOP signals
    each career track.

    Returns: (track_scores dict, matched_keywords dict)
    """
    sop_lower = sop_text.lower() if sop_text else ""
    track_scores = {}
    matched_keywords = {}

    for track_id, track in TRACKS.items():
        hits = [kw for kw in track["sop_keywords"] if kw in sop_lower]
        score = len(hits) / len(track["sop_keywords"]) if track["sop_keywords"] else 0
        track_scores[track_id] = round(score, 4)
        matched_keywords[track_id] = hits

    return track_scores, matched_keywords


def score_experience(experience_roles):
    """
    Scans experience role descriptions for track-specific keywords and
    returns a normalized score per track showing career track alignment
    based on what the candidate has actually done.

    Returns: (track_scores dict, matched_keywords dict)
    """
    exp_text = " ".join(experience_roles).lower() if experience_roles else ""
    track_scores = {}
    matched_keywords = {}

    for track_id, track in TRACKS.items():
        hits = [kw for kw in track["experience_keywords"] if kw in exp_text]
        score = len(hits) / len(track["experience_keywords"]) if track["experience_keywords"] else 0
        track_scores[track_id] = round(score, 4)
        matched_keywords[track_id] = hits

    return track_scores, matched_keywords


def score_degree_from_tracks(top_tracks, cluster_degree_scores):
    """
    Determines the recommended degree by combining:
    - Primary degree signals from the top 3 ranked tracks (weighted by track rank)
    - Cluster-based degree scores from academic background

    Returns: str — the recommended degree ("MHA", "MPH", "MSHI", or "MBA-HC")
    """
    degree_votes = {d: 0.0 for d in DEGREES}

    # Top track gets highest weight, rank 3 gets lowest
    # Weights are designed so the top track's primary degree dominates
    rank_weights = [1.0, 0.5, 0.25]
    for i, track in enumerate(top_tracks):
        primary = TRACKS[track["track_id"]]["primary_degree"]
        degree_votes[primary] += rank_weights[i]

    # Blend with cluster academic scores (smaller weight - background is secondary)
    for degree, score in cluster_degree_scores.items():
        degree_votes[degree] += score * 0.1

    return max(degree_votes, key=degree_votes.get)


def classify(candidate):
    """
    Main classification function. Takes a candidate dict and returns
    a structured output with recommended degree and top 3 career tracks.

    Scoring weights:
      SOP keywords:        50%  (stated intent is strongest signal)
      Experience keywords: 30%  (what they've actually done)
      Degree alignment:    20%  (academic background cluster signal)
    """
    cid = candidate["id"]
    print(f"\n{'='*60}")
    print(f"Classifying: {cid}")
    print(f"{'='*60}")

    # --- Signal 1: Academic cluster scoring ---
    cluster_degree_scores = score_clusters(candidate.get("subjects", []))
    print(f"  [Cluster Scores] {cluster_degree_scores}")

    # --- Signal 2: SOP scoring ---
    sop_track_scores, sop_keywords_fired = score_sop(candidate.get("sop", ""))
    print(f"  [Top SOP Tracks] {sorted(sop_track_scores.items(), key=lambda x: -x[1])[:3]}")

    # --- Signal 3: Experience scoring ---
    exp_track_scores, exp_keywords_fired = score_experience(candidate.get("experience_roles", []))
    print(f"  [Top Exp Tracks] {sorted(exp_track_scores.items(), key=lambda x: -x[1])[:3]}")

    # --- Degree alignment bonus: map cluster degree scores to tracks ---
    # Normalize cluster degree scores
    max_cds = max(cluster_degree_scores.values()) if max(cluster_degree_scores.values()) > 0 else 1
    norm_cluster = {d: v / max_cds for d, v in cluster_degree_scores.items()}

    degree_alignment_bonus = {}
    for track_id, track in TRACKS.items():
        primary = track["primary_degree"]
        degree_alignment_bonus[track_id] = norm_cluster.get(primary, 0)

    # --- Combine all signals ---
    final_scores = {}
    for track_id in TRACKS:
        final_scores[track_id] = round(
            (sop_track_scores[track_id] * 0.50) +
            (exp_track_scores[track_id] * 0.30) +
            (degree_alignment_bonus[track_id] * 0.20),
            4
        )

    # --- Rank and pick top 3 ---
    ranked = sorted(final_scores.items(), key=lambda x: -x[1])
    top_3_ids = [r[0] for r in ranked[:3]]

    # --- Build top 3 track output with specific rationales ---
    top_3_tracks = []
    for rank_idx, track_id in enumerate(top_3_ids, 1):
        track = TRACKS[track_id]
        sop_hits = sop_keywords_fired.get(track_id, [])
        exp_hits = exp_keywords_fired.get(track_id, [])

        rationale_parts = []
        if sop_hits:
            rationale_parts.append(f"SOP keywords matched: {', '.join(repr(k) for k in sop_hits)}")
        else:
            rationale_parts.append("No direct SOP keyword match")
        if exp_hits:
            rationale_parts.append(f"Experience keywords matched: {', '.join(repr(k) for k in exp_hits)}")
        if degree_alignment_bonus[track_id] > 0.3:
            rationale_parts.append(f"Academic background supports {track['primary_degree']} (degree alignment score: {round(degree_alignment_bonus[track_id], 2)})")

        top_3_tracks.append({
            "rank": rank_idx,
            "track_id": track_id,
            "track_name": track["name"],
            "score": final_scores[track_id],
            "rationale": ". ".join(rationale_parts) + "."
        })

    # --- Determine recommended degree ---
    recommended_degree = score_degree_from_tracks(top_3_tracks, cluster_degree_scores)
    print(f"  [Recommended Degree] {recommended_degree}")
    print(f"  [Top 3 Tracks] {[t['track_id'] for t in top_3_tracks]}")

    # --- Degree rationale ---
    top_cluster_degrees = sorted(cluster_degree_scores.items(), key=lambda x: -x[1])[:2]
    degree_rationale = (
        f"Academic clusters most strongly support {top_cluster_degrees[0][0]} "
        f"and {top_cluster_degrees[1][0]}. "
        f"Top-ranked track {top_3_tracks[0]['track_id']} has {recommended_degree} as primary degree. "
        f"Combined signal points to {recommended_degree}."
    )

    return {
        "candidate_id": cid,
        "recommended_degree": recommended_degree,
        "degree_rationale": degree_rationale,
        "top_3_tracks": top_3_tracks
    }
