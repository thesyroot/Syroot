import os;

def fixp(path):
	if(path.strip(" ")=="" or path.strip(" ")=="this"):
		path=os.getcwd();
	if(path.find(os.getcwd().split("\\")[0])==-1):
		if(os.path.exists(path)==False):
			path=os.getcwd().replace("\\","/")+"/"+path;
	if(os.path.exists(path)==True):
		return path;
	else:
		return "0";

def iof (incode):
	import os;

	incode=incode.strip(" ");

	if(incode.count("#:")==1):
		valores=incode.split("#:");

		if(valores[1]!=""):
			if(os.path.exists(valores[1])==False):
				print("No existe el directorio indicado\n");
			else:
				os.mkdir(valores[1]+"/"+valores[0]);
		else:
			os.mkdir((os.getcwd().replace("\\","/"))+"/"+valores[0]);
	elif(incode.count("#:")==2):
		valores=incode.split("#:");
		name=valores[0];

		if(valores[2]!=""):
			if(os.path.exists(valores[2])==False):
				print("No existe el directorio indicado\n");
			else:
				aux=os.getcwd();
				os.chdir(valores[2]);

				Cfile=open(name,"a+");
				Cfile.write(valores[1]);
				Cfile.close();

				os.chdir(aux.replace("\\","/"));
		else:
			Cfile=open(name,"a+");
			Cfile.write(valores[1]);
			Cfile.close();
	elif(incode.count("#:")==0):
		if(fixp(incode)!="0"):
			if(os.path.isdir(fixp(incode))==True):
				print("Solo se pueden leer los archivos");
			if(os.path.isfile(fixp(incode))==True):
				aux=os.getcwd().replace("\\","/");
				cdir="";
				for dirs in range(0,len((os.getcwd().replace("\\","/")+"/"+incode).split("/"))-1):
					cdir=cdir+(os.getcwd().replace("\\","/")+"/"+incode).split("/")[dirs]+"/";
				os.chdir(cdir.rstrip("/"));
				print(cdir.rstrip("/"));
				file=open(incode.split("/")[len(incode.split("/"))-1],"r+");

				print("****************File****************");
				print("".join(file.readlines()));
				print("***************EndFile**************");

				file.close();
				os.chdir(aux);
		else:
			print("El archivo indicado no existe");

def rm (fpath):
	import os
	import shutil

	fpath=fixp(fpath);
	if(fpath!="0"):
		if(os.path.isdir(fpath)==True):
			shutil.rmtree(fpath);
		if(os.path.isfile(fpath)==True):
			os.remove(fpath);
	else:
		print("El directorio o archivo indicado no existe");

def mv (oldp,newp=os.getcwd()):
	import shutil

	if(fixp(oldp)!="0"):
		if(fixp(newp)!="0"):
			shutil.move(fixp(oldp),fixp(newp));
		else:
			print("No se pudo realizar la operacion por un error de uno de los path");
	else:
		print("No se pudo realizar la operacion por un error de uno de los path");

def cpy (oldp,newp):
	import shutil

	if(fixp(oldp)!="0"):
		if(newp.find(os.getcwd().split("\\")[0])==-1):
			if(os.path.exists(newp)==False):
				newp=os.getcwd().replace("\\","/")+"/"+newp;
		if(os.path.isdir(fixp(oldp))==True):
			shutil.copytree(fixp(oldp),newp);
		if(os.path.isfile(fixp(oldp))==True):
			shutil.copy(fixp(oldp),newp);
	else:
		print("No se pudo realizar la operacion por un error de uno de los path");

def rn (oldn,newn):
	import shutil

	if(fixp(oldn)!="0"):
		if(newn.find(os.getcwd().split("\\")[0])==-1):
			newn=os.getcwd().replace("\\","/")+"/"+newn;
		if(os.path.isdir(fixp(oldn))==True):
			shutil.copytree(fixp(oldn),newn);
			shutil.rmtree(fixp(oldn));
		if(os.path.isfile(fixp(oldn))==True):
			shutil.copy(fixp(oldn),newn);
			os.remove(fixp(oldn));
	else:
		print("No se pudo realizar la operacion por un error de uno de los path");