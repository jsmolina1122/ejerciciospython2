# EJERCICIOS CONCEPTOS BASICOS
#--------------------------------------------------------------------------------
# base=float(input("Ingrese La Base Del Triangulo: \n"))

# height=float(input("Ingrese La Altura Del Triangulo: \n"))

# print(f"El Area Del Triangulo Es : {(base*height)/2}")

#--------------------------------------------------------------------------------

# dolar=float(input("Ingrese La Cantidad De Dolares A Covertir A Pesos: \n"))

# pesos=float(input("Ingrese El Precio Actual Del Dolar : \n"))

# print(f"Los {dolar} Dolares A Pesos Colombiano Equivalen A : {dolar*pesos}")

#-----------------------------------------------------------------------------------------------------

# centigrados=float(input("Ingrese La Cantidad De Grados Centigrados A Convertir En Fahrenheit: \n"))

# print(f"Los {centigrados} Grados centigrados A fahrenheit equivalen A : {centigrados*1.8000+32.00}")

#----------------------------------------------------------------------------------------------------------

# print((f"La Cantidad De Segundos Que Tiene Un Lustro Son :{31536000*5} \n"))

#-------------------------------------------------------------------------------------------------------------

# print((f"La Cantidad De Segundos Que Le Toma A La Luz Viajar Del Sol A Marte es :{ 227943824 / 300000} Segundos \n"))

#-----------------------------------------------------------------------------------------------------------------------
# circunferncia=(3.1416*50)/100000

# print((f"La Cantidad De Vueltas Que Da Una llanta De Diametro 50 En Un Kilometro es :{ 1/ circunferncia} Vueltas \n"))

#------------------------------------------------------------------------------------------------------------------------

# import math

# cuadrado=math.sqrt(3)

# print((f"La longitud De La Sombra De Un Edificio de 20 mtr Con Un Angulo Al Sol De 20° es :{20*cuadrado} \n"))

#---------------------------------------------------------------------------------------------------------------

# edad1=int(input("Ingrese La Edad De La Primera Persona: \n"))

# edad2=int(input("Ingrese La Edad De La Segunda Persona : \n"))

# if edad1 == edad2:

#     print(True)

# else :

#     print(False)

#---------------------------------------------------------------------------------------------------------------------

from datetime import datetime,timedelta

fecha_actual = input('Introducir Fecha  actual (dd/mm/yyyy): ')

fecha_hasta = input('Introducir Fecha De Nacimiento (dd/mm/yyyy): ')

fecha_actual = datetime.strptime(fecha_actual, '%d/%m/%Y')

fecha_hasta = datetime.strptime(fecha_hasta, '%d/%m/%Y')

diferencia=(fecha_actual - fecha_hasta)


print(f'Han Pasado: {(diferencia.days)/30} meses') 


#----------------------------------------------------------------------------------------------------------------------

# materia1=float(input("Ingrese La Nota Definitiva De Español: \n"))

# materia2=float(input("Ingrese La Nota Definitiva De Matematicas : \n"))

# materia3=float(input("Ingrese La Nota Definitiva DeEconomia: \n"))

# materia4=float(input("Ingrese La Nota Definitiva De Programacion: \n"))

# materia5=float(input("Ingrese La Nota Definitiva De ingles: \n"))

# promedio=(materia1+materia2+materia3+materia4+materia5)/5

# print((f"El Promedio Del Alumno es :{promedio} \n"))

#------------------------------------------------------------------------------------------------------------------------------
