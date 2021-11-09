import os
import PythonMagick	# 该模块需要下载whl进行安装
#获取目录下文件名清单
files = os.listdir()
if not os.path.exists('icon'):
	os.mkdir('icon')  
#对文件名清单里的每一个文件名进行处理
for filename in files:
    portion = os.path.splitext(filename) # portion为名称和后缀分离后的列表
    if portion[1] ==".jpg" or portion[1] ==".png": # 如果为JPG则更改名字
        newfile = portion[0]+".ico" # 要改的新后缀#改好的新名字
        # 进行格式转换
        img = PythonMagick.Image(filename)
        img.sample('256x256')
        path = os.path.join('icon',newfile)	
        img.write(path)
        print("%s --> %s" % (filename,newfile))     
