'''
Condicionales en Python

Los condiconales permiten tomar decisiones dentro de un programa. Mediante un estructura
de condiciones segun si una condicion es verdadera o falsa
* if 
* else
'''

#EJEMPLO DE IF - ELSE
edad = 18

if edad >= 18:
    print("Eres Mayor de edad") #Bloque si la condicion es verdadera
else:
    print("Eres menor de edad") #Bloque si la condicion es falsa


#EJEMPLO IF- ELIF -ELSE

nota = 5

if nota == 5:
    print("Excelente")
elif nota >= 4:
    print("Aprobo")
else:
    print("Reprobo")