"""Prepare a metadata-only manifest from approved references."""

import argparse
import json
from pathlib import Path


def load_records(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("records", [])


def main():
    parser = argparse.ArgumentParser(
        description="Merge metadata and transcript references into a manifest."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(
            "activitynet-captions-dataset-20000-videos/data/sample_manifest.json"
        ),
    )
    parser.add_argument(
        "--metadata",
        type=Path,
        default=Path(
            "activitynet-captions-dataset-20000-videos/data/video_metadata.json"
        ),
    )
    parser.add_argument(
        "--transcripts",
        type=Path,
        default=Path(
            "activitynet-captions-dataset-20000-videos/data/transcript_references.json"
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "activitynet-captions-dataset-20000-videos/data/final_manifest.json"
        ),
    )
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    metadata_by_id = {
        item["record_id"]: item for item in load_records(args.metadata)
    }
    transcripts_by_id = {
        item["record_id"]: item for item in load_records(args.transcripts)
    }

    records = []
    for record in manifest.get("records", []):
        record_id = record["record_id"]
        merged = dict(record)
        merged.update(metadata_by_id.get(record_id, {}))
        merged.update(transcripts_by_id.get(record_id, {}))
        records.append(merged)

    output = dict(manifest)
    output["records"] = records
    output["metadata_only"] = True

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} records to {args.output}")


if __name__ == "__main__":
    main()