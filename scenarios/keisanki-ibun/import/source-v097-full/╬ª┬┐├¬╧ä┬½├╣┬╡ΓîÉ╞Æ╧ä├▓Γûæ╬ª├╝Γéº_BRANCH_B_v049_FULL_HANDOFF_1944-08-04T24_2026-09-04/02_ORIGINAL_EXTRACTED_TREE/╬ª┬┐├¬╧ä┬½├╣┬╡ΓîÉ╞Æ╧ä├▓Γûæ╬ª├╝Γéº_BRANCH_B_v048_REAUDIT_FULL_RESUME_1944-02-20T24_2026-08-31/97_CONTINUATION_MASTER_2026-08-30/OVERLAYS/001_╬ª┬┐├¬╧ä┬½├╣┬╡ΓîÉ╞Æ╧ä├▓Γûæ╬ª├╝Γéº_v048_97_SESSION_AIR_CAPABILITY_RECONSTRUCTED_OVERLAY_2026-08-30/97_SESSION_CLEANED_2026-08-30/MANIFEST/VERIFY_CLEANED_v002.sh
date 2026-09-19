#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
sha256sum -c 97_SESSION_CLEANED_2026-08-30/MANIFEST/SHA256SUMS_CLEANED_v002.txt
