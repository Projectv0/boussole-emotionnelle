#!/bin/bash
P="https://cdn.nanobanana.io/production/predictions/8d00112f-81da-469a-af7e-bf59dae9a372/"
D="/Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/illustrations"
mkdir -p "$D"; n=0; s=0
while IFS='|' read -r nom fic; do
  [ -z "$nom" ] && continue
  if [ -f "$D/$nom.jpg" ]; then s=$((s+1)); continue; fi
  curl -s -o "$D/$nom.jpg" "$P$fic" && n=$((n+1))
done
echo "téléchargées : $n · déjà présentes : $s"
