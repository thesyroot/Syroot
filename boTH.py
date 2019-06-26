def boTH(ask):

	simbolos = ('+', '-','*','x' ,'/' ,'%' ,'**' ,'^');
	numero = [ask+"+0"];
	acum = 0;
	rta = "";

	for sim in simbolos:
		for conta in range(len(numero)):
			if (numero[conta].find(sim) != -1):
				aux = numero[conta].split(sim);
				for i in range(len(aux)):
					if(sim == '-'):
						if(i != 0):
							numero.insert(conta+i, "_"+aux[i]);
						else:
							numero.insert(conta+i, aux[i]);
						# p=0;
						# for elem in numero:
						# 	if(elem==""):
						# 		numero.pop(p);
						# 	p+=1;
					elif(sim == '/'):
						if(aux[i].find('_') != -1):
							aux[i] = aux[i].replace('_', '-');
						numero.insert(conta, str(int(int(aux[i])/int(aux[i+1]))));
						if(aux[i].find('-') != -1):
							aux[i] = aux[i].replace('-', '_');
						y=conta+i;
						# p=0;
						# for elem in numero:
						# 	if(elem==""):
						# 		numero.pop(p);
						# 	p+=1;
						break;
					elif (sim == '*' or sim == 'x'):
						if(aux[i].find('_') != -1):
							aux[i] = aux[i].replace('_', '-');
						numero.insert(conta, str(int(aux[i])*int(aux[i+1])));
						if(aux[i].find('-') != -1):
							aux[i] = aux[i].replace('-', '_');
						y=conta+i;
						# p=0;
						# for elem in numero:
						# 	if(elem==""):
						# 		numero.pop(p);
						# 	p+=1;
						break;
					elif (sim == '**' or sim == '^'):
						if(aux[i].find('_') != -1):
							aux[i] = aux[i].replace('_', '-');
						numero.insert(conta, str(int(aux[i])**int(aux[i+1])));
						if(aux[i].find('-') != -1):
							aux[i] = aux[i].replace('-', '_');
						y=conta+i;
						# p=0;
						# for elem in numero:
						# 	if(elem==""):
						# 		numero.pop(p);
						# 	p+=1;
						break;
					elif (sim == '%'):
						if(aux[i].find('_') != -1):
							aux[i] = aux[i].replace('_', '-');
						numero.insert(conta, str(int(aux[i])%int(aux[i+1])));
						if(aux[i].find('-') != -1):
							aux[i] = aux[i].replace('-', '_');
						y=conta+i;
						# p=0;
						# for elem in numero:
						# 	if(elem==""):
						# 		numero.pop(p);
						# 	p+=1;
						break;
					else:
						numero.insert(conta+i, aux[i]);
					y=conta+i;
				numero.pop(y+1);
	for num in numero:
		if(num.find('_') != -1):
			num = num.replace('_', '-');
		if (num==""):
				num=0;
		acum += int(num);
		
	return str(acum);

def isboTHtype(elemento):
	simbol=('0','1','2','3','4','5','6','7','8','9','/', '%','**','^' ,'x' ,'*' ,'+' ,'-');

	if(elemento.isspace()==True or elemento == ""):
		return False;

	for letra in elemento:
		for simbolo in simbol:
			if(letra==simbolo):
				elemento = elemento.replace(letra,"a");
	if(elemento.strip("a")==""):
		return True;
	else:
		return False;