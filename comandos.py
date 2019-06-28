import os;
from iof import fixp;

local=os.getcwd();

def comandos(comando):
	import time;
	import webbrowser;
	import os;
	import time;

	#next(os.walk(os.getcwd()))[ 0 el path, 1 las carpetas, 2 los archivos

	comando = comando.strip(' ');
	if (comando == "off"):
		return 0;
	if (comando == "shvar"):
		return 10;
	if (comando == "shd"):
		print((os.getcwd()).replace("\\","/"));
	if (comando == "shinfo"):
		comandos("ls");
		file=input("chfile << ").strip(" ");
		file=fixp(file);
		if(file!="0"):
			if(os.path.isfile(file)==True):
				aux="";
				print("La info. del archivo "+file.split("/")[len(file.split("/"))-1]+"\n");
				for i in range(0,len((file.split("/")[len(file.split("/"))-1]).split("."))-1):
					aux=aux+(file.split("/")[len(file.split("/"))-1]).split(".")[i]+".";
				print("Su nombre es "+aux.rstrip("."));
				print("Su tamaño es "+str(os.path.getsize(file))+" bytes");
				print("El ultimo acceso que se tuvo fue "+time.ctime(os.path.getmtime(file)));
				print("Se creo en "+time.ctime(os.path.getctime(file)));
				print("Se ubica en "+os.getcwd().replace("\\","/")+"/"+file);
			if(os.path.isdir(file)==True):
				print("La info. del directorio "+file.split("/")[len(file.split("/"))-1]+"\n");
				print("Su nombre es "+file.split("/")[len(file.split("/"))-1]);
				print("Su tamaño es "+str(os.path.getsize(file))+" bytes");
				print("El ultimo acceso que se tuvo fue "+time.ctime(os.path.getatime(file)));
				print("Se creo en "+time.ctime(os.path.getctime(file)));
				print("Se ubica en "+os.getcwd().replace("\\","/")+"/"+file);
		else:
			print("No se pudo realizar la operacion por un error de uno de los path")
	if (comando.find("cd ")!=-1):
		cdir="".join(comando.split("cd ")).strip(" ");
		if(cdir.isspace()!=True and cdir!=""):
			if(cdir.find("..")!=-1):
				nowdir=(os.getcwd()).split("\\");
				for times in range(0,cdir.count("..")):
					nowdir.pop();
				cdir="/".join(nowdir);
				if((os.getcwd()).split("\\")[0]==cdir):
					cdir=cdir+"/";
			elif(cdir.find(os.getcwd().split("\\")[0])==-1):
				if(os.path.exists(cdir.split("\\")[0]+"/")!=True):
					cdir=os.getcwd().replace("\\","/")+"/"+cdir;
			os.chdir(cdir);
	if (comando == "cls"):
		os.system("cls");
	if (comando == "cn"):
		aux=(os.getcwd()).replace("\\","/");
		os.chdir(local);
		with open("preferencias.txt","r+") as carac:
			carac.seek(0);
			lines=carac.readlines();
		with open("preferencias.txt","w+") as carac:
			lines[0]=input("¿? << ")+"\n";
			carac.writelines(lines);
		os.chdir(aux);
	if (comando == "explorer"):
		link = input("link << ");
	if (comando.find("ct")!=-1):
		aux="".join(comando.split("ct")).strip(" ");
		if(aux=="f"):
			print(str(len(next(os.walk(os.getcwd()))[2]))+" file(s) encontrados");
		elif(aux=="d"):
			print(str(len(next(os.walk(os.getcwd()))[1]))+" dir(s) encontrados");
		elif(aux==""):
			print(str(len(next(os.walk(os.getcwd()))[1]))+" dir(s) encontrados");
			print(str(len(next(os.walk(os.getcwd()))[2]))+" file(s) encontrados");
		else:
			cont=0;
			filestring=next(os.walk(os.getcwd()))[2];
			for file in filestring:
				if(file.split(".")[len(file.split("."))-1]==aux):
					cont+=1;
			print(str(cont)+" file(s) con extension "+aux+" encontrados");
	if (comando == "ls"):
		for file in next(os.walk(os.getcwd()))[2]:
			aux="";
			filestring=file.split(".");
			space=10;
			for letra in filestring[len(filestring)-1]:
				space-=1;
			for i in range(0,len(filestring)-1):
				aux=aux+filestring[i]+".";
			print(filestring[len(filestring)-1]+"".rjust(space," ")+aux.rstrip("."));
		if(len(next(os.walk(os.getcwd()))[1])>0):
			print("<DIR>     "+"\n<DIR>     ".join(next(os.walk(os.getcwd()))[1]));
	if (comando == "lsd"):
		if(len(next(os.walk(os.getcwd()))[1])>0):
			print("<DIR>     "+"\n<DIR>     ".join(next(os.walk(os.getcwd()))[1]));
	if (comando == "lsf"):
		aux="";
		for file in next(os.walk(os.getcwd()))[2]:
			filestring=file.split(".");
			space=10;
			for letra in filestring[1]:
				space-=1;
			for i in range(0,len(filestring)-1):
				aux=aux+filestring[i]+".";
			print(filestring[len(filestring)-1]+"".rjust(space," ")+aux.rstrip("."));
	if(comando == "lsinfo"):
		for file in next(os.walk(os.getcwd()))[2]:
			aux="";
			auxspace = 15;
			filestring=file.split(".");
			space=10;
			for letra in filestring[len(filestring)-1]:
				space-=1;
			for letra in str(os.path.getsize(file)):
				auxspace-=1;
			for i in range(0,len(filestring)-1):
				aux=aux+filestring[i]+".";
			print(time.ctime(os.path.getatime(file))+"    "+str(os.path.getsize(file))+" bytes"+"".rjust(auxspace," ")+filestring[len(filestring)-1]+"".rjust(space," ")+aux.rstrip("."));
		if(len(next(os.walk(os.getcwd()))[1])>0):
			for dirs in next(os.walk(os.getcwd()))[1]:
				auxspace = 15;
				for letra in str(os.path.getsize(file)):
					auxspace-=1;
				print(time.ctime(os.path.getatime(dirs))+"    "+str(os.path.getsize(file))+" bytes"+"".rjust(auxspace," ")+"<DIR>     "+dirs);
	if (comando == "time"):
		print (time.strftime("%H:%M:%S"));
	if (comando == "date"):
		print (time.strftime("%d/%m/%y"));
	if (comando == "alltd"):
		print (time.strftime("%H:%M:%S %d/%m/%y"));
	if (comando == "h" or comando == "help"):
		print ("off\ntime\nshvar\nexplorer\ndate\nalltd\ncls\ncn\nshd\nshinfo\ncd\nls\nlsf\nlsd\nlsinfo");
