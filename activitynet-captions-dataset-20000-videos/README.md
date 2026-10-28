# Proxy for Streaming Data Extraction

This repository documents a metadata-only reference pipeline for collecting,
validating, and preparing video-related records for AI data workflows.

The pipeline separates metadata, captions, transcripts, media references, and
manifests. It does not download or redistribute ActivityNet Captions videos,
captions, transcripts, or other third-party media.

## What This Example Does

This example demonstrates how to:

- Read an approved source manifest;
- Process records incrementally;
- Preserve record identifiers and source references;
- Separate video metadata from caption and transcript references;
- Prepare a versioned output manifest;
- Record rights status before any future media use.

The current implementation is intentionally metadata-only. It does not make
network requests, call a scraping API, download media, or route traffic through
a proxy.

## Repository Structure

```text
activitynet-captions-dataset-20000-videos/
├── README.md
├── requirements.txt
├── .env.example
├── scripts/
│   ├── collect_video_metadata.py
│   ├── collect_transcripts.py
│   └── prepare_manifest.py
└── data/
    ├── sample_manifest.json
    ├── video_metadata.json
    ├── transcript_references.json
    └── final_manifest.json
```

## Pipeline Flow

```text
Approved source manifest
          |
          v
Video metadata references
          |
          v
Transcript and caption references
          |
          v
Validated final manifest
```

Each stage writes structured records. Metadata, captions, transcripts, and
media references remain separate so downstream workflows can select only the
fields and files they are authorized to use.

## Run the Example

The example uses only the Python standard library.

From the repository root, run:

```bash
python activitynet-captions-dataset-20000-videos/scripts/collect_video_metadata.py
```

```bash
python activitynet-captions-dataset-20000-videos/scripts/collect_transcripts.py
```

```bash
python activitynet-captions-dataset-20000-videos/scripts/prepare_manifest.py
```

The commands generate:

```text
data/video_metadata.json
data/transcript_references.json
data/final_manifest.json
```

These files contain metadata and references only. They do not contain video
files, audio files, captions, or transcripts.

## Example Record

```json
{
  "record_id": "example-000001",
  "source": "AUTHORIZED_SOURCE",
  "media_reference": "APPROVED_MEDIA_REFERENCE",
  "caption_reference": "APPROVED_CAPTION_REFERENCE",
  "duration_seconds": 0,
  "rights_status": "REVIEW_REQUIRED",
  "split": "train"
}
```

## Record Validation

Before using a record in a downstream workflow, check:

- `record_id` exists and is unique;
- The source and media references are traceable;
- Caption and transcript references are separated from media references;
- Duration and other numeric fields use the expected format;
- Rights status is documented;
- Missing annotations are represented explicitly;
- Credentials and private URLs are not present in the record;
- The record is not treated as permission to download or redistribute media.

## Proxy and API Boundary

A production collection pipeline may use an authorized API adapter or proxy
transport for approved requests. That transport layer is separate from record
parsing and manifest preparation.

This repository does not include:

- Proxy credentials;
- API keys or tokens;
- A live collection endpoint;
- YouTube or TikTok adapters;
- A media download command;
- A proxy rotation implementation;
- A third-party source scraper.

A proxy can transport a request, but it does not establish permission to collect,
copy, train on, or redistribute the returned data.

## Resumable Collection Design

A future authorized collection implementation should:

1. Read approved source identifiers from a versioned manifest;
2. Write each completed record incrementally;
3. Use stable record identifiers for checkpoints;
4. Retry only transient failures with bounded backoff;
5. Record failed identifiers and failure reasons;
6. Validate completed files before marking them available;
7. Preserve the source manifest and collection timestamp.

The current repository documents this design but does not execute downloads.

## Training Data Preparation

A metadata record is not a training sample by itself. A future preparation
workflow may map approved metadata, captions, transcripts, and media references
into task-specific records, but only after rights and quality review.

Possible downstream formats include:

- Video-text pairs;
- Captioning records;
- Video understanding manifests;
- Retrieval metadata;
- Multimodal training references.

This repository does not provide a training dataset or claim that ActivityNet
Captions may be used for commercial training, fine-tuning, or redistribution.

## ActivityNet Captions Scope

ActivityNet Captions is used here as a reference for pipeline structure and
metadata organization.

This repository does not redistribute the complete ActivityNet Captions
dataset, source videos, captions, or transcripts. Users must obtain the data
from an authorized source and follow its applicable license and usage terms.

The name of a dataset in this example does not grant access rights or change the
terms of the original dataset.

## Responsible Use

Do not upload:

- Source videos or audio;
- Third-party captions or transcripts;
- Personal information;
- Credentials, API keys, or access tokens;
- Private download URLs;
- Unverified derived data.

Before retaining or reusing any media or annotation, review:

- Source-platform terms;
- Dataset license;
- Commercial-use permission;
- AI training and evaluation permission;
- Modification and derivative-use permission;
- Redistribution permission;
- Privacy and personal-information requirements.

## Related Projects

- [Video Dataset Toolkit](https://github.com/Thordata/video-dataset-toolkit)
- [Licensed Video Dataset Directory](https://github.com/Thordata/awesome-licensed-video-datasets)
- [Thordata Video Datasets](https://www.thordata.com/products/multi-platform-video-datasets)

## Current Status

This is a metadata-only reference implementation.

It is suitable for demonstrating record processing, manifest preparation, and
data governance boundaries. It is not a complete 20,000-video downloader,
training dataset, video retrieval benchmark, or production collection service.

## License

The MIT License applies only to this repository's code and documentation.

It does not apply to ActivityNet Captions, third-party videos, audio, captions,
transcripts, metadata, derived data, or any other external dataset assets.
