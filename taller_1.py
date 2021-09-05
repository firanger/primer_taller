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