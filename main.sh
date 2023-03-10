#!/bin/bash

input="/Users/jeromecoffin/git_repo/instafollower/sustainablehashtag.csv"
while IFS= read -r line
do
  tag_popularity=$(docker run --rm -e HASHTAG="$line" get_hashtagpopularity)
  echo "###"
  echo $line
  echo $tag_popularity
  echo "###"
  if (( $tag_popularity < 500000 )); then
    python3 /Users/jeromecoffin/git_repo/instafollower/get_influenceur.py "$line"
  fi
done < "$input"


docker run --restart always -e HASHTAG="$line" -v ~/data:/data get_influenceur
