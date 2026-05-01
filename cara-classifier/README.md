# CARA Classifier — Curavolv Phase 1 Assessment

## Overview

CARA (Career Alignment & Recommendation Algorithm) is a rule-based career classification system designed for Curavolv to guide healthcare graduate candidates toward optimal degree programs and career tracks. This classifier analyzes six candidate profiles and recommends one of four healthcare degrees (MHA, MPH, MSHI, MBA-HC) along with a ranked list of three career tracks. The system uses a weighted scoring architecture that evaluates academic background, stated career intent (SOP), and professional experience to produce structured, explainable recommendations.

## Approach & Design Decisions

### Scoring Architecture

The classifier uses a three-signal weighted scoring system:

| Signal | Weight | Rationale |
|--------|--------|-----------|
| SOP Keywords | 50% | Stated intent is the strongest predictor of career direction. A candidate's explicit goals and interests should outweigh their past background, especially for career-changers. |
| Experience Keywords | 30% | What the candidate has actually done provides concrete evidence of skills and exposure. This validates or challenges the SOP signals. |
| Academic Clusters | 20% | Academic background provides foundational knowledge but is the weakest signal because many healthcare careers welcome diverse educational backgrounds. |

This weighting order reflects a key design principle: **intent > experience > background**. A dentist who explicitly wants to move into hospital administration should be classified toward MHA/T01, not penalized for lacking a traditional admin background.

### Keyword Design

**SOP Keywords** were chosen per track by analyzing common language used by professionals in each career path. For example:
- T01 (Admin/Operations): "leadership", "quality improvement", "organizational", "hospital"
- T09 (Informatics): "EHR", "FHIR", "interoperability", "clinical decision support"
- T07 (Policy): "legislation", "advocacy", "government", "Ayushman", "ministry"

**Subject-to-Cluster Mapping** was validated by mapping typical coursework from each degree type to subject clusters. For instance, a BSc Nursing degree naturally maps to C6 (Health & Clinical) through subjects like "geriatric nursing", "community health nursing", and "pharmacology".

### Conflict Resolution

When signals disagree, the system resolves conflicts through the weighting scheme:

- **Clinical background + Admin SOP** → SOP wins (e.g., freshgrad_01: BDS dentist wanting admin role → MHA/T01)
- **No experience + Strong SOP** → SOP carries the load (e.g., mph_policy_01: fresh grad with policy internship → MPH/T07)
- **Strong experience + Weak SOP** → Experience provides significant signal (e.g., mba_finance_01: audit experience reinforces CFO track signal)

The design explicitly favors stated intent because career classification should be forward-looking, not backward-looking.

### Edge Cases

Several interesting classification decisions were made:

1. **freshgrad_01 (BDS → MHA)**: Clinical dentistry background but explicit admin intent. SOP keywords "organizational leadership" and "quality improvement" directly match T01. Classified as MHA despite no admin coursework.

2. **mha_ltc_01 (Nursing → MHA)**: Four years clinical nursing experience, but SOP explicitly states "move from bedside nursing into managing". Keywords "quality improvement" and "managing" point to T01.

3. **mph_policy_01 (Political Science → MPH/T07)**: Zero healthcare experience, but SOP mentions "Ayushman Bharat", "government health policy", and "national health legislation" — all direct T07 keyword matches.

4. **mshi_tech_01 (CS → MSHI/T09)**: Perfect alignment. CS degree with "EHR integration" experience and SOP mentioning "FHIR interoperability" and "Director of Health Informatics".

## How to Run

```bash
cd cara-classifier
python classifier.py
```

The classifier will process all JSON files in the `candidates/` directory and write results to `outputs/results.json`.

## File Structure

| File | Role |
|------|------|
| `framework.py` | Foundation module containing all constants: 10 subject clusters (C1-C10), 4 degrees, and 11 career tracks with their keyword mappings. |
| `scorer.py` | Scoring engine with five functions: `score_clusters()`, `score_sop()`, `score_experience()`, `score_degree_from_tracks()`, and `classify()`. Each function includes docstrings and debug output. |
| `classifier.py` | Main entry point that loads candidate JSON files, runs classification, prints results to console, and writes `outputs/results.json`. |
| `candidates/*.json` | Six candidate profiles with fields: id, degree, university, gpa, year, subjects, experience_years, experience_roles, strengths, and sop. |
| `outputs/results.json` | Final classification output with recommended degree, degree rationale, and top 3 tracks (each with rank, track_id, track_name, score, and rationale). |
| `README.md` | This documentation file. |

## AI Tools Disclosure

This project was developed with assistance from Claude (Anthropic's AI assistant). Specifically:
- Claude was used to understand the assignment structure and brainstorm the scoring architecture
- The overall file structure and function signatures were discussed with Claude
- All scoring weights (50/30/20 split), keyword dictionaries for each track, subject cluster mappings, and classification logic were independently authored
- All candidate rationales and degree justifications were written independently
- Claude was **not** used to generate the output JSON or final classifications — those are produced entirely by the rule-based scoring engine implemented in scorer.py
