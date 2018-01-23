#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

with open('data/raw.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    for row in readCSV:
        print(row)