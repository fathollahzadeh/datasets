#!/bin/bash

IFS=',' read -ra DBS <<< "$1"
DST_DIR=$2

WORKING_DIR=$(pwd)
data_dir="$DST_DIR/PublicBIbenchmark"

for db in "${DBS[@]}"; do 
    d="${data_dir}/${db}"
	cd $d
	for file in ./*.bz2; do
		echo "$(date) decompressing $file"
		bzip2 -dk $file &
	done
	cd ../
done
wait

echo "$(date) done"