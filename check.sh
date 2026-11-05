set -e
cd -- "$(dirname -- "$0")"
echo "=== Calculator Quality Gate ==="
python3 -m pytest -v
echo "Quality Gate Passed"
