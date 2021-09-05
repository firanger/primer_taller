'''UNIVERSIDAD DE LA COSTA CUC FUNDAMENTOS ALGORÍTMICOS  TALLER DE ALGORITMOS SECUENCIALES PROFESOR: ING.  ROBERTO MORALES 
'''
print("todos los ejercicios estan comentados para que sea mas facil ejecutarlos uno por uno")
'''Calcule el valor de Y indicando paso a paso como llegó al resultado '''

'''Calcule el valor de Y indicando paso a paso como llegó al resultado '''

'''punto 1:
 y = ( (5+2-5)^2 * 5+8/2 -30 )  / 2 * 5 -3
print("primero que todo, hay que resolver el primer parentesis de adentro hacia afuera: (5+2-5)^2 ")
print("dando como resultado: ",(5+2-5)**2)
print("segundo, hay que multiplicar y dividir de izquierda a derecha la expresion;: 4*5+8/2-30", )
print("dando como resultado:", 4*5+8/2-30)
print("tercero, hay que dividir y multiplicar la expresion: -6/2*5")
print("dando como resultado: -15")
print("por ultimo, solo hay que restar de izquierda a derecha:-15-3")
print("la respues final es:\n", ( (5+2-5)**2 * 5+8/2 -30 )  / 2 * 5 -3 )'''

'''Realizar los algoritmos que den solución a la problemática presentada 
en los siguientes ejercicios: '''

'''1.  Haga un algoritmo que calcule la masa de la siguiente fórmula: 
Masa = (presión * volúmen) / (0.37 * (temperatura + 460)) 

presion=int(input("ingrese el valor la presion "))
volumen=int(input("ingrese el valor del volumen "))
temperatura=int(input("ingrese el valor de la temperatura "))

masa=(presion * volumen) / (0.37 * (temperatura + 460))
print("la masa es igual a: ",masa)'''

'''2. Calcular  el  número  de  pulsaciones  que  una  persona  debe  tener  por 
cada 10 segundos de ejercicio, si la fórmula es: 
Num. Pulsaciones = (200 – edad) /10.
nombre=input("ingrese el nombre de la persona en cuestion ")
print("ingrese la edad de ",nombre, " para realizar el calculo ")
edad=int(input(""))
pulsaciones = (200 - edad) /10
print("el numero de pulsaciones que debe tener ",nombre , " cada 10s es: ",pulsaciones)'''

'''3. Tres  personas  deciden  invertir  su  dinero  para  fundar  una  empresa. 
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje 
que cada quien invierte con respecto a la cantidad total invertida.

persona_1=float(input("ingrese la cantidad invertida de persona 1 "))
persona_2=float(input("ingrese la cantidad invertida de persona 2 "))
persona_3=float(input("ingrese la cantidad invertida de persona 3 "))

total=persona_3+persona_1+persona_2
print("el porcentaje invertido por la persona_1 es: ", (persona_1/total)*100,"%")
print("el porcentaje invertido por la persona_1 es: ", (persona_2/total)*100,"%")
print("el porcentaje invertido por la persona_1 es: ", (persona_3/total)*100,"%")'''

'''4.  Un  banco  da  a  sus  ahorradores  un  interes  de  1.5%  sobre  el  monto 
ahorrado. Teniendo como dato de entrada el saldo inicial del 
ahorrador determine el saldo final. 

saldo=float(input("ingrese el saldo del ahorrador "))
saldo_final=(saldo*0.015)+saldo
print("el saldo final es: ",saldo_final)'''

'''5. Una empresa le hace los siguientes descuentos sobre el sueldo base 
a  sus  trabajadores:  1%  por  ley  de  politica  pública,  4%  por  seguro 
social,  0.5%  por  seguro  forzoso  y  5%  por  caja  de  ahorro.  Realice  un algoritmo que determine el monto de cada descuento y el monto total 
a pagar al trabajador. 

sueldo=float(input("ingrese el sueldo base del traubajador "))

desc_ley_p=sueldo*0.01
desc_seguro_social=sueldo*0.04
desc_seguro_forz=sueldo*0.005
desc_caja_ahorro=sueldo*0.05
monto=sueldo-(desc_caja_ahorro+desc_ley_p+desc_seguro_forz+desc_seguro_social)
print("el valor descontado por ley  de  politica  pública es: ", desc_ley_p)
print("el valor descontado por seguro social es: ", desc_seguro_social)
print("el valor descontado por seguro  forzoso es: ", desc_seguro_forz)
print("el valor descontado por caja  de  ahorro es: ", desc_caja_ahorro)
print("el monto total a pagar al traubajador es: ", monto)'''

''' 6. El  periódico  el  Informador  cobra  por  un  aviso  clasificado  un  monto 
que depende del número de palabras, tamaño en cetímetros y 
número  de  colores.  Cada  palabra  tiene  un  costo  de  $20.000,  cada 
centímetro  tiene  un  costo  de  $15.000  y  cada  color  tiene  un  costo  de 
$25.000. Realice un algoritmo que determine el monto a pagar por un 
aviso clasificado.

palabras = float(input("ingrese numero de palabras"))
centimetros = float(input("ingrese numero de centimetros"))
colores = float(input("ingrese numero de colores"))

monto=(palabras * 20000)
totalc=(centimetros * 15000)
totalcolor=(colores * 25000)

monto=(monto+totalc+totalcolor)

print("el monto total es : ", monto)'''

'''7.Una  empresa  paga  a  sus  empleados  un  bono  por  antigüedad  que 
consiste  en  $100.000  por  el  primer  año  laboral  y  $120.000  por  cada 
año siguiente. Realice un algoritmo que determine el monto del bono 
a pagar a un trabajador que tiene varios años en la empresa.
años=int(input("ingrese el numero de años que lleva el trabajador en la pempresa "))
monto=0
for i in range(años):
    if i !=0 :
        monto+=120000
    if años==0:
        monto=0
    if años==1:
        monto=100000
if años>1:
    print("el monto total por natiguedad es:", (monto+100000))
if años ==1 or años==0:    
    print("el monto total por natiguedad es:", monto) '''