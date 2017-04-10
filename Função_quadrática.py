print("ax²+bx+c")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
if a==0:
	if b!=0:
		print("\nx =",-c,"/",b)
		print("x =",-c/b)
		print("\nA raiz é",-c/b)
	elif c==0:
		print("\n0 = 0")
		print("As raizes são todos os números reais")
	else:
		print("")
		print(c,"= 0")
		print("\nNão possuí raízes")
else:
	delta=b**2-4*a*c
	print("\nΔ =",b,"*",b,"- 4 *",a,"*",c)
	if 4*a>=0: print("Δ =",b**2,"-",4*a,"*",c)
	else: print("Δ =",b**2,"- (",4*a,"*",c,")")
	if 4*a*c>=0: print("Δ =",b**2,"-",4*a*c)
	else: print("Δ =",b**2,"+",-4*a*c)
	print("Δ =",delta,"\n")
	if delta==0:
		if b==0:
			print("x = ",b,"/ ( 2 *",a,")")
			print("x = ",b,"/",2*a)
			print("x =",b)
			print("\nA raiz é",b)
		else:
			print("x = -",b,"/ ( 2 *",a,")")
			print("x = -",b,"/",2*a)
			print("x =",-b/(2*a))
			print("\nA raiz é",-b/(2*a))
	elif delta<0:
		import math
		print ("Não possuí raizes reais\n")
		i,fat=2,[]
		while math.fabs(delta)>i:
			while delta%i==0:
				delta=delta/i
				fat.append(i)
			i+=1
		delta,i,pares=b**2-4*a*c,1,[]
		while i<len(fat):
			if fat[i-1]==fat[i]:
				pares.append(fat[i])
				i+=1
			i+=1
		i,dentro,fora=0,math.fabs(delta),1
		while i<len(pares):
			dentro=dentro/(pares[i]**2)
			fora=fora*pares[i]
			i+=1
		print("√Δ =",math.sqrt(-(delta)),"* i")
		print("x = (-",b,"±",math.sqrt(-(delta)),"* i )/ ( 2 *",a,")")
		print("x = (-",b,"±",math.sqrt(-(delta)),"* i )/",2*a)
		print("x = -",b/(2*a),"-",math.sqrt(-(delta))/(2*a),"* i ou x = -",b/(2*a),"+",math.sqrt(-(delta))/(2*a),"* i")
		print("x =",(-b-math.sqrt(-(delta)))/(2*a),"* i ou x =",(-b+math.sqrt(-(delta)))/(2*a),"* i")
		if -b-math.sqrt(-(delta))==0 and -b+math.sqrt(-(delta))==0: print("\nA raiz é 0.0")
		elif -b-math.sqrt(-(delta))==0: print("\nAs raizes são 0.0 e",(-b+math.sqrt(-(delta)))/(2*a),"* i")
		elif -b+math.sqrt(-(delta))==0: print("\nAs raizes são",(-b-math.sqrt(-(delta)))/(2*a),"* i e 0.0")
		else: print("\nAs raizes são",(-b-math.sqrt(-(delta)))/(2*a),"* i e",(-b+math.sqrt(-(delta)))/(2*a),"* i")
	else:
		import math
		print("√Δ =",math.sqrt(delta))
		print("x = (-",b,"±",math.sqrt(delta),")/ ( 2 *",a,")")
		print("x =",-b+math.sqrt(delta),"/",2*a,"ou x =",-b-math.sqrt(delta),"/",2*a)
		print("x =",(-b+math.sqrt(delta))/(2*a),"ou x =",(-b-math.sqrt(delta))/(2*a))
		print("\nAs raizes são",(-b+math.sqrt(delta))/(2*a),"e",(-b-math.sqrt(delta))/(2*a))
