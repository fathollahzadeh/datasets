#!/bin/bash

IFS=',' read -ra DBS <<< "$1"
DST_DIR=$2

WORKING_DIR=$(pwd)
data_dir="$DST_DIR/PublicBIbenchmark"

for db in "${DBS[@]}"; do 
    d="${data_dir}/${db}"
	cd $d
	rm -rf ./*.csv
	for file in ./*.bz2; do
		echo "$(date) decompressing $file"
		bzip2 -dk $file 
	done

	for file in ./*.csv; do
		echo "$(date) unicode $file"
		sed 's/“/"/g; s/”/"/g' $file > "${file}_tmp"
		rm -rf $file
		mv "${file}_tmp" $file
		rm -rf "${file}_tmp"

		if [[ "$db" == "HashTags" || "$db" == "Corporations" || "$db" == "Euro2016" || "$db" == "IGlocations2" || "$db" == "Rentabilidad" || "$db" == "Romance" || "$db" == "TableroSistemaPenal" || "$db" == "NYC" ]]; then
    		python "${WORKING_DIR}/refine.py" --data-path ${file} --dataset-name ${db}
			rm -rf $file
			mv "${file}_clean" $file
		fi
	done	
	cd ../
done

echo "$(date) done"
