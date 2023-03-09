#!/bin/bash

input="/Users/jeromecoffin/sustainablehashtag.csv"
while IFS= read -r line
do
  tag_popularity=$(python3 count_hashtag.py "$line")
  echo "###"
  echo $line
  echo $tag_popularity
  echo "###"
  if (( $tag_popularity < 500000 )); then
    python3 get_influenceur.py "$line"
  fi
done < "$input"
