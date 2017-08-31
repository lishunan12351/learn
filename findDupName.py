#coding=utf-8
import os
import sys

'''
获取当前python脚本的目录
'''
isIgnore = True ## 是否忽略大小写

curDir = sys.path[0]


txtFile = curDir + '/total.txt'
fp = open(txtFile,'w')

files = os.listdir(curDir)

fp.write('重名图片如下:')
fp.write('\n\n')

imageMap = {} #已检查
haveWriteMap = {} # 已写入

def GetFileNameAndExt(filename):
	shotname = os.path.splitext(filename)[0]
	return shotname

def dirlist(path):
    filelist =  os.listdir(path)
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):
			if filename != 'publish':
				dirlist(filepath) 
        else:
        	filterName = os.path.splitext(filepath)[1]
        	if filterName == '.png' or filterName == 'jpg':
				print 'check: ' + filepath
				lname = GetFileNameAndExt(filename)
				if isIgnore:
					lname = lname.lower()
				print 'lname',lname
				if lname in imageMap.keys():
					if haveWriteMap.has_key(lname) == False:
						haveWriteMap[lname] = 1
						fp.write(filepath + '\n')
				else:
					imageMap[lname] = filepath
					

dirlist(curDir)   
fp.write('结束')
fp.close()






	