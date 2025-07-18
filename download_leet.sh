#!/bin/bash

# Create folder if it doesn't exist
mkdir -p ./downloads
cd ./downloads

echo "📥 Fetching list of solved problems..."

# Get list of solved Python problems
leetcode list -q s -l python | awk 'NR>1 {print $2}' > solved.txt

echo "✅ Found solved problems. Starting download..."

# Loop through each problem and download its solution
while read problem; do
    fname=$(echo $problem | tr '-' '_' ).py
    if [ ! -f "$fname" ]; then
        echo "⬇️  Downloading: $problem"
        leetcode show "$problem" -g -l python > "$fname"
    else
        echo "✅ Already downloaded: $problem"
    fi
done < solved.txt

echo "🎉 All done! Solutions are in the 'downloads' folder."
