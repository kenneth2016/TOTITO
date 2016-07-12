
print ("bienvenido al totito supremo 2016 69")
l= [["a", "b", "c"],
	["d", "e", "f"],
	["g", "h", "i"],
	]

print (l[0])
print (l[1])
print (l[2])
w= False
while w != True:

	p= str(input("ingrese que poscicion quiere, jugador 1: "))
	p_valor= ord (p)- ord("a")
	p_fila= p_valor % 3
	p_columna= p_valor//3
	l[p_columna][p_fila]="X"

	

	if l[0][0]=="x" and l[0][1]=="x" and l[0][2]=="x":
		print ("jugador 1 gano")
		w=True
	if l[1][0]=="x" and l[1][1]=="x" and l[1][2]=="x":
		print ("jugador 1 gano")
		w=True
	if l[2][0]=="x" and l[2][1]=="x" and l[2][2]=="X":
		print ("jugador 1 gano")
		w=True
	if l[0][0]=="x" and l[1][0]=="x" and l[2][0]=="x":
		print ("jugador 1 gano")
		w=True
	if l[0][1]=="x" and l[1][1]=="x" and l[2][1]=="x":
		print ("jugador 1 gano")
		w=True
	if l[0][2]=="x" and l[1][2]=="x" and l[2][2]=="X":
		print ("jugador 1 gano")
		w=True
	if l[0][0]=="x" and l[1][1]=="x" and l[2][2]=="x":
		print ("jugador 1 gano")
		w=True
	if l[2][0]=="x" and l[1][1]=="x" and l[0][2]=="X":
		print ("jugador 1 gano")
		w=True


	print (l[0])
	print (l[1])
	print (l[2])
	if w!= True:

		p= str(input("ingrese que poscicion quiere, jugador 2: "))

		if p=="a":
			l[0][0]="O"

		if p=="b":
			l[0][1]="O"

		if p=="c":
			l[0][2]="O"

		if p=="d":
			l[1][0]="O"

		if p=="e":
			l[1][1]="O"

		if p=="f":
			l[1][2]="O"

		if p=="g":
			l[2][0]="O"

		if p=="h":
			l[2][1]="O"

		if p=="i":
			l[2][2]="O"

		if l[0][0]=="O" and l[0][1]=="O" and l[0][2]=="O":
			print ("jugador 2 gano")
			w=True
		if l[1][0]=="O" and l[1][1]=="O" and l[1][2]=="O":
			print ("jugador 2 gano")
			w=True
		if l[2][0]=="O" and l[2][1]=="O" and l[2][2]=="O":
			print ("jugador 2 gano")
			w=True
		if l[0][0]=="O" and l[1][0]=="O" and l[2][0]=="O":
			print ("jugador 2 gano")
			w=True
		if l[0][1]=="O" and l[1][1]=="O" and l[2][1]=="O":
			print ("jugador 2 gano")
			w=True
		if l[0][2]=="O" and l[1][2]=="O" and l[2][2]=="O":
			print ("jugador 2 gano")
			w=True
		if l[0][0]=="O" and l[1][1]=="O" and l[2][2]=="O":
			print ("jugador 2 gano")
			w=True
		if l[2][0]=="O" and l[1][1]=="O" and l[0][2]=="O":
			print ("jugador 2 gano")
			w=True


		print (l[0])
		print (l[1])
		print (l[2])