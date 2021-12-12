#!/usr/bin/env bash

day="$1"
dir="d$day"

session="$(cat .sessionid)"

echo "Creating directory $dir"
mkdir -p "$dir"
echo "Trying to download input"
curl "https://adventofcode.com/2021/day/$day/input" -H "Cookie: session=$session" -o "$dir/input" || echo "Failed"
