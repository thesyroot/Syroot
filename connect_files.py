from comandos import comandos
from iof import iof,rm,mv,cpy,rn
from boTH import isboTHtype,boTH
from editor import editor
from colorama import Fore,init
import os

local = os.getcwd();

init();

with open("preferencias.txt","a+") as file:
	file.seek(0);

	aux=file.readline();
	while aux!="/=\n":
		aux=file.readline();
	aux="";
	while aux!="/=\n":
		aux=file.readline();
		if(aux!="/=\n"):
			aux=aux.strip("\n");
			if(aux.strip("=").strip("\t")==""):
				print(Fore.GREEN + aux.strip("\n")+Fore.WHITE);
			else:
				print(Fore.RED + aux.strip("\n")+Fore.WHITE);

print("");

while True:
	aux=str(os.getcwd());
	os.chdir(local);
	with open("preferencias.txt","a+") as carac:
		carac.seek(0);
		line=(carac.readline()).strip("\n");
		if(line=="pathdir"):
			name=aux;
		else:
			name=line;
	os.chdir(aux.replace("\\","/"));
	txt=(input(name+" >> ")).strip(" ");

	if(txt.find("~")!=-1):
		intupla=txt.split("~");
		intupla[0]+=" ";
		txt=(intupla[0].strip(" ")).lower();
		tuplacom=(str(intupla[1]).strip(" ")).split(";");
		for com in tuplacom:
			rtacom=comandos(com);
		if(rtacom==0):
			break;

	if(comandos(txt)==0):
		break;

	if(txt.count("=")>1):
		auxbo=txt.split("=");
		txt="";
		for elem in auxbo:
			if(isboTHtype(elem)==True):
				elem=boTH(elem);
			elif(elem=="\\"):
				elem="=";
			txt=txt+elem;
		print(txt);
		txt=txt.strip(" ");

	if(txt.find("iof ")!=-1):
		iof(("".join(txt.split("iof "))).strip(" "));
		
	if(txt.find("rm ")!=-1):
		rm("".join(txt.split("rm ")).strip(" "));

	if(txt.find("mv ")!=-1):
		txt="".join(txt.split("mv ")).strip(" ");
		if(txt.find(",")!=-1):
			mv(txt.split(",")[0].strip(" "),txt.split(",")[1].strip(" "));
		else:
			mv(txt);

	if(txt.find("cpy ")!=-1):
		txt="".join(txt.split("cpy ")).strip(" ");
		if(txt.find(",")!=-1):
			cpy(txt.split(",")[0].strip(" "),txt.split(",")[1].strip(" "));
		else:
			cpy(txt);

	if(txt.find("rn ")!=-1):
		txt="".join(txt.split("rn ")).strip(" ");
		cpy(txt.split(",")[0].strip(" "),txt.split(",")[1].strip(" "));

	if(txt=="banner"):
		comandos("cls");
		with open("preferencias.txt","a+") as file:
			file.seek(0);

			aux=file.readline();
			while aux!="/=\n":
				aux=file.readline();
			aux="";
			while aux!="/=\n":
				aux=file.readline();
				if(aux!="/=\n"):
					aux=aux.strip("\n");
					if(aux.strip("=").strip("\t")==""):
						print(Fore.GREEN + aux.strip("\n")+Fore.WHITE);
					else:
						print(Fore.RED + aux.strip("\n")+Fore.WHITE);
		print("");

	if(txt.find("edit")!=-1):
		if(txt.strip("edit")==""):
			editor();
		else:
			txt="".join(txt.split("edit ")).strip(" ");
			if(txt.find(os.getcwd().split("\\")[0])==-1):
				if(os.path.exists(txt)==False):
					txt=os.getcwd().replace("\\","/")+"/"+txt;
			editor(txt);
