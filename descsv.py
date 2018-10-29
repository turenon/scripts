#!/usr/bin/env python3
#coding:utf-8
import os
import codecs
import csv
#工作量统计，a为异常列表，b为总服务器 + 项目

with open('./a','r',encoding='utf-8') as f:
	machlinelist = f.readlines()
with open('./b','r',encoding='utf-8') as f:
	allmachs = f.readlines()
machlist = []
allmachd = {}

for allmach in allmachs:
    allmach = allmach.split()
    allmachd[allmach[0].strip()] = allmach[1]

with open('c.csv','w') as f:
	csv_writer = csv.writer(f,delimiter = ',')
	for mach in machlinelist:
		mach = mach.strip()
		if mach in allmachd:
			pro = allmachd[mach]
			print(pro)
			csv_writer.writerow([mach,pro])
		else:
		    csv_writer.writerow([mach,'site'])













