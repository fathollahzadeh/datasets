#!/bin/bash


db_list=$1
dst_dir=$2

# ./run1DownloadData.sh $db_list $dst_dir
./run2DecompressCSV.sh $db_list $dst_dir