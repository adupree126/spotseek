#!/bin/zsh

playlist_id=$1
if [[ $playlist_id == "" ]]; then
  printf "enter spotify playlist ID: "
  read playlist_id
fi

mkdir $playlist_id 2>> /dev/null
cd $playlist_id
echo $playlist_id | python ../api_calls.py
while read -r line; do
   soulseek q -m flac $line
 done <track_list.txt
