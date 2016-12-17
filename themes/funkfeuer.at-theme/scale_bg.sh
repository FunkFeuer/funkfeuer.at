#!/bin/sh

for WIDTH in 800 1280 2048 3840
do
	JPGEXTENT=$(($WIDTH/6))kb
	echo "generating assets/images/bg-$WIDTH.jpg with target size of $JPGEXTENT"
	convert -resize $WIDTH -define jpeg:extent=$JPGEXTENT images_original/brenner.jpg assets/images/bg-$WIDTH.jpg
done
