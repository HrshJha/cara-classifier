
import json
import os
import glob
from scorer import classify


def main():
    print("\n🚀 CARA Classifier — Curavolv Phase 1 Assessment")
    print("=" * 60)

    candidate_files = sorted(glob.glob("candidates/*.json"))

    if not candidate_files:
        print("❌ No candidate files found in candidates/ directory.")
        return

    results = []

    for filepath in candidate_files:
        with open(filepath, "r") as f:
            candidate = json.load(f)

        result = classify(candidate)
        results.append(result)

        print(f"\n✓ {candidate['id']}")
        print(f"   Degree : {result['recommended_degree']}")
        print(f"   Track 1: {result['top_3_tracks'][0]['track_id']} — {result['top_3_tracks'][0]['track_name']}")
        print(f"   Track 2: {result['top_3_tracks'][1]['track_id']} — {result['top_3_tracks'][1]['track_name']}")
        print(f"   Track 3: {result['top_3_tracks'][2]['track_id']} — {result['top_3_tracks'][2]['track_name']}")

    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/results.json"

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"✅ All {len(results)} candidates classified.")
    print(f"📄 Output saved to: {output_path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
