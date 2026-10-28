"""Metadata-only example. Does not download transcripts or third-party data."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Create transcript references without downloading transcripts."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("activitynet-captions-dataset-20000-videos/data/sample_manifest.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "activitynet-captions-dataset-20000-videos/data/transcript_references.json"
        ),
    )
    args = parser.parse_args()

    manifest = json.loads(args.input.read_text(encoding="utf-8"))
    references = []

    for record in manifest.get("records", []):
        references.append(
            {
                "record_id": record.get("record_id"),
                "caption_reference": record.get("caption_reference"),
                "transcript_status": "REFERENCE_ONLY",
                "rights_status": record.get("rights_status"),
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(references, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(references)} transcript references to {args.output}")


if __name__ == "__main__":
    main()