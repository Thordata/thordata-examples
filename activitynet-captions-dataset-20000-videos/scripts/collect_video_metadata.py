"""Metadata-only example. Does not download video, captions, or third-party data."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Create metadata records from an approved manifest."
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
            "activitynet-captions-dataset-20000-videos/data/video_metadata.json"
        ),
    )
    args = parser.parse_args()

    manifest = json.loads(args.input.read_text(encoding="utf-8"))
    metadata = []

    for record in manifest.get("records", []):
        metadata.append(
            {
                "record_id": record.get("record_id"),
                "source": record.get("source"),
                "media_reference": record.get("media_reference"),
                "duration_seconds": record.get("duration_seconds"),
                "rights_status": record.get("rights_status"),
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(metadata)} metadata records to {args.output}")


if __name__ == "__main__":
    main()