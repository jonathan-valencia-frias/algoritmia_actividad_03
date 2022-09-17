import math

def triangulo():
    print("ingrese la base")
    base=int(input())
    print("ingrese la altura")
    altura=int(input())
    area=(base*altura)/2
    print("el area es "+str(area))

def cuadrado():
    print("ingrese el lado")
    lado=int(input())
    area=lado**2
    print("el area es "+str(area))

def circulo():
    print("ingrese el radio")
    radio=float(input())
    area=math.pi*(radio**2)
    print("el area es "+str(area))
    
def zodiaco():
    print("ingrese el dia de nacimiento")
    dia=int(input())
    print("ingrese el mes de nacimiento")
    mes=int(input())
    if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)): signo = 'aries'
    elif ((mes==4) and (dia>=21)) or ((mes==5) and (dia<=20)): signo = 'tauro'
    elif ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)): signo = 'geminis'
    elif ((mes==6) and (dia>=22)) or ((mes==7) and (dia<=22)): signo = 'cancer'
    elif ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)): signo = 'leo'
    elif ((mes==8) and (dia>=24)) or ((mes==9) and (dia<=22)): signo = 'virgo'
    elif ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)): signo = 'libra'
    elif ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=22)): signo = 'escorpio'
    elif ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=21)): signo = 'sagitario'
    elif ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)): signo = 'capicornio'
    elif ((mes==1) and (dia>=21)) or ((mes==2) and (dia<=19)): signo = 'acuario'
    elif ((mes==2) and (dia>=20)) or ((mes==3) and (dia<=20)): signo = 'piscis'
    print(signo+'\n')
    
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)
    
def euler(l):
    limite = l
    n = 0
    e = 0
    while n < limite:
        e += 1/factorial(n)
        n = n + 1
    print(e)
        

euler(2)
print('\n\n')
euler(5)
print('\n\n')
euler(10)
print('\n\n')