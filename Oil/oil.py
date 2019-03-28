#!/usr/bin/python
# -*- coding: utf-8 -*-
#import uniout
import pandas as pd
from os import listdir
from os.path import isfile, isdir, join
import numpy
import os
import obspy
from obspy.core import read
import glob
import numpy as np
import csv
# 指定要列出所有檔案的目錄
data_path = 'D:\\test\\Application_Math\\Oil'
files = listdir(data_path)

# 取得所有檔案與子目錄名稱
#*----------------------------------------------------------------校正檔案內容

#*----------------------------------------------------------------校正完畢
i=0
rows=[]
data=[]
for f in files:
	if f.endswith('.csv'):
		csvfile=open(str(f),'r',encoding="utf-8")
		i+=1
		
		for row in csv.reader(csvfile,delimiter=','):#----------------開始處理資料顛倒問題
			#for z in range(len(row[1])+1):
			data+=[row[1]]
		data.reverse()
		output=open(str(1999+i)+'.txt','w+')
		l=-2
		for x in data:
			l+=1
			output.write(str(l)+'\t'+str(x)+'\n')
		data=[]
			#rows=[]
		output.close()
			

	#print(f,type(data.read()))		
#f.writelines(lines_PGA)
	
