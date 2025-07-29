#!/bin/bash

IFS=',' read -ra DBS <<< "$1"
DST_DIR=$2
WORKING_DIR=$(pwd)

BASE_URL="https://event.cwi.nl/da/PublicBIbenchmark"

rm -rf "$DST_DIR/PublicBIbenchmark"
mkdir -p "$DST_DIR/PublicBIbenchmark"

for db in "${DBS[@]}"; 
do
    wb_path="${WORKING_DIR}/benchmark/${db}"
    echo $wb_path
    wb="$(basename $wb_path)"
    mkdir -p "$DST_DIR/PublicBIbenchmark/$wb"
    for f in $wb_path/samples/*
    do
        t="$(basename $f)"; t="${t%.sample.csv}"
        wget -P "$DST_DIR/PublicBIbenchmark/$wb" "$BASE_URL/$wb/$t.csv.bz2"
    done
done