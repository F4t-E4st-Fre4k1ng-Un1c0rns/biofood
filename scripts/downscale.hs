#!/bin/bash

# Set IFS to newline only to handle spaces in filenames
IFS=$'\n'

for filepath in $PWD/$1; do
	filename=$(basename "$filepath")
	filename="${filename%.*}"
	ffmpeg -i "$filepath" -vf scale=700:320,setsar=1/1 -c:v libwebp -y -frames:v 1 "$HOME/Downloads/блюда pegged/$filename.webp"
done

