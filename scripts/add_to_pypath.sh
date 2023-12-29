#!/bin/bash

cd ..
basedir=$(pwd)

filters_dir="/cstm_filters/"
preproc_dir="/preprocessing/"
filters_path="$basedir""$filters_dir"
preproc_path="$basedir""$preproc_dir"

export PYTHONPATH="${PYTHONPATH}:$filters_path"
echo "$filters_path added to PYTHONPATH"

export PYTHONPATH="${PYTHONPATH}:$preproc_path"
echo "$preproc_path added to PYTHONPATH"