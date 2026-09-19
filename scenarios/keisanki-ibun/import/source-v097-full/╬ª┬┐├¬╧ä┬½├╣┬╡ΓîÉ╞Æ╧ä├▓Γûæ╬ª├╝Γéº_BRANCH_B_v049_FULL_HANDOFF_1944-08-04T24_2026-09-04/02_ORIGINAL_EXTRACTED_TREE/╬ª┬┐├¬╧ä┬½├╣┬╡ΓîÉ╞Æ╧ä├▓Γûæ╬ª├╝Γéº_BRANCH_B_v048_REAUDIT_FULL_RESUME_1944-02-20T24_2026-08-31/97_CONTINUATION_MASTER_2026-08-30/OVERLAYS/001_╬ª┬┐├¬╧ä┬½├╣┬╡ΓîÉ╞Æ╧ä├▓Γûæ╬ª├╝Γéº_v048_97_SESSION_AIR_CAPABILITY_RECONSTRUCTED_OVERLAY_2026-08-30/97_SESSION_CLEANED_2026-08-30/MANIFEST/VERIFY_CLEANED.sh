#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT"
sha256sum -c 97_SESSION_CLEANED_2026-08-30/MANIFEST/SHA256SUMS_CLEANED_v001.txt
