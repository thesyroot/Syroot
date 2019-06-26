import msvcrt as m
import os
from colorama import init,Cursor,Back

init();

print("Holaaaaa\n soy jose");
pos=[1,0,0,0];

print("hola lola\nsoy un capo");
print(Cursor.UP(pos[0]+1));
# print(Cursor.DOWN(pos[1]));
# print(Cursor.BACK(pos[2]));
# print(Cursor.FORWARD(pos[3]));
print(Back.RED+"s");

# while True:
# 	aux=["",""];

	# for i in range(0,2):
	# 	if(i==1  and aux[0]==b'\xe0'):
	# 		aux[i]=m.getch();
	# 	if(i==0):
	# 		aux[i]=m.getch();

	# if(aux[0]==b'\xe0' and aux[1]==b'H'):
	# 	# print(Back.RESET+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	pos[0]-=1;
	# 	# print(Back.RED+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	print(Cursor.POS(0,1)+Back.RED+"s");
	# elif(aux[0]==b'\xe0' and aux[1]==b'P'):
	# 	# print(Back.RESET+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	pos[0]+=1;
	# 	# print(Back.RED+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	print(Cursor.POS(pos[0],0)+Back.RED+"s");
	# elif(aux[0]==b'\xe0' and aux[1]==b'M'):
	# 	print(Back.RESET+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	posiciones[3]+=1;
	# 	print(Back.RED+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# elif(aux[0]==b'\xe0' and aux[1]==b'K'):
	# 	print(Back.RESET+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	posiciones[2]+=1;
	# 	print(Back.RED+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# elif(aux[0]==b'\x1b' and aux[1]==""):
	# 	print(Back.RESET+Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"s");
	# 	print(Cursor.UP(posiciones[0])+Cursor.DOWN(posiciones[1])+Cursor.BACK(posiciones[2])+Cursor.FORWARD(posiciones[3])+"hola");
		
	# 	posiciones=[0,0,0,0];
	# else:
	# 	try:
	# 		print(aux[0].decode());
	# 	except UnicodeDecodeError:
	# 		print("No se pudo decodificar el caracter");



