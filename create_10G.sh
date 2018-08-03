#!/bin/bash

for i in $(seq 1 10);do
	python create_data.py 1G --min 10 --max 10 --chars > part$i &
done

wait

cat part* > data_file.txt
