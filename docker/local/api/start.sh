#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# Get the number of available CPU cores
CPU_CORES=$(python -c 'import multiprocessing; print(multiprocessing.cpu_count())')

echo "Starting server with $CPU_CORES workers..."

# Run server with workers equal to CPU cores
uvicorn cmd/server:app --host 0.0.0.0 --port 8000 --reload --workers $CPU_CORES --timeout-keep-alive 60 --timeout-grace 60 --log-level debug