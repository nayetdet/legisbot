#!/bin/bash
readonly DIR="./data"

wget -r \
     --no-parent \
     --progress=bar \
     --timeout=15 \
     --tries=3 \
     --user-agent="Mozilla/5.0" \
     -A html,htm \
     -P "$DIR" \
     "https://www.planalto.gov.br/ccivil_03/"

find "$DIR" -type f | while read -r file; do
    readonly tmpfile=$(mktemp)
    trap 'rm -f "$tmpfile"' EXIT

    if iconv -f utf-8 -t utf-8 -c "$file" -o "$tmpfile"; then
        mv "$tmpfile" "$file"
        echo "Cleared: $file"
        trap - EXIT
    else
        echo "Error: $file"
    fi
done
