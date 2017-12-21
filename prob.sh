#!/bin/bash
		truncate -s 0 teste.txt
        for i in `seq 1 100`; do
            python casino.py | grep OVERALL: >> teste.txt
        done
        ./teste.py