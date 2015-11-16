def sizeof_fmt(num):
    for unit in ['','k','m','g','t','p','e','z']:
        if num < 1024.0:
            return str(num)+unit
        num /= 1024.0
    return str(num)+str(unit)
def cpy(fi,s,d):
	t=str(s)+"/"+str(fi)
	shutil.copy(t,d)
import os
import shutil
import math
import platform
import threading
T=threading.Thread
osplat=platform.system()
source=raw_input("Enter Source:- ");
dest=raw_input("Enter Destination:- ")
if os.path.isfile(source):
	file_size=os.stat(source).st_size
	convert_size=sizeof_fmt(file_size)
	if osplat=="Linux":
		if str(file_size)!=convert_size:
			dest=dest.replace("\ ","")
			part=float(convert_size[:-1])/10.0
			part=str(int(math.ceil(part)))+convert_size[len(convert_size)-1]
			cwd="def"
			if "/" in source:
				cwd=source
				cwd=cwd.rsplit("/",1)
				mainfilename=str(cwd[1])
				cwd=str(cwd[0])
			if cwd=="def":
				cwd=os.getcwd()
				mainfilename=str(source)
			os.chdir(cwd)
			source=source.replace(" ","\ ")
			print "Preparing....."
			os.system("split -b "+part+" "+source)
			fileli=[]
			for i in os.listdir(cwd):
				if i.startswith("xa"):
					fileli.append(i)
			fileli.sort()
			f=0
			if os.path.isdir(dest):
				print "Copying..."
				os.chdir(cwd)
				f=1
			else:
				response=raw_input("The directory does'nt exist. Do you want to create a new one in home directory??(Y/N)").lower()
				if response=="y":
					os.chdir(os.path.expanduser("~"))
					os.system("mkdir " +dest);
					os.chdir(cwd)
					print "Copying..."
					f=1
				else:
					print "File Copy Operation Failed !!"
			if f==1:
				for r in fileli:
					while threading.active_count()>10:
						continue
					t = T(target=cpy,args=(r,cwd,dest))
					t.start()
					t.join()
				print "Copy Done"
				print "Appending...."
				os.system("rm x*")
				os.chdir(dest)
				os.system("cat x*>"+mainfilename)
				os.system("rm x*")	
				print "Completed file copy of "+mainfilename	
		else:
			if os.path.isdir(dest):
				shutil.copy(source,dest)
				if "/" in source:
					t=source
					t=t.rsplit("/",1)
					t=str(t[1])
				else:
					t=source
				print "Completed File Copy of:- "+t
			else:
				response=raw_input("The directory does'nt exist. Do you want to create a new one in home directory??(Y/N)").lower()
				if response=="y":
					os.chdir(os.path.expanduser("~"))
					os.system("mkdir " +dest);
					shutil.copy(source,dest)
					if "/" in source:
						t=source
						t=t.rsplit("/",1)
						t=str(t[1])
					else:
						t=source
					print "Completed File Copy of:- "+t
				else:
					print "File Copy Operation Failed !!"
		#os.system("split -b 1m "+source)
else:
	print "File doesn't exists"

