# Proxy for Streaming Data Extraction Pipeline

This example documents a streaming data extraction pipeline for collecting,
resuming, validating, and preparing video-related records for AI workflows.

## What This Example Covers

- Streaming collection of structured records
- Resumable downloads
- Record-level validation
- Separate metadata, captions, transcripts, and media references
- Versioned manifests for downstream processing

## Dataset Scope

This example uses ActivityNet Captions as a reference for pipeline structure
and metadata organization.

It does not redistribute the complete dataset, source videos, captions, or
third-party media. Users must obtain data through an authorized source and
follow the applicable license and usage terms.

## Suggested Pipeline

1. Collect approved metadata and record identifiers.
2. Write records incrementally to a staging directory.
3. Validate required fields and record identifiers.
4. Resume incomplete downloads instead of restarting the full job.
5. Keep metadata, captions, transcripts, and media references separate.
6. Generate a versioned manifest for downstream processing.
7. Review licensing and redistribution permissions before use.

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
Responsible Use
This example does not grant rights to download, copy, modify, train on, or redistribute ActivityNet Captions or any other third-party dataset.

Do not upload source videos, captions, credentials, or unverified derived data.

Related Projects
Video Dataset Toolkit
Licensed Video Dataset Directory
License
The MIT License applies only to this repository's code and documentation. Third-party data remains subject to its own license and usage terms.
