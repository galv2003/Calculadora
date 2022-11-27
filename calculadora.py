import math
import re
from math import cos
from math import sin
from math import tan
import numpy


#INICIO OPERACIONES

#Suma
def suma(expresion):
  divisionesPuntoCero = re.search('[.]{1}[0]+',expresion)
  if divisionesPuntoCero != None:
    expresion = expresion.replace(divisionesPuntoCero.group(),"")
  numeros = re.findall('\d+[.]?\d*',expresion)
  resultado = 0
  for i in range(len(numeros)):
    resultado += float(numeros[i])
  return resultado

#Resta
def resta(expresion):
  divisionesPuntoCero = re.search('[.]{1}[0]+',expresion)
  if divisionesPuntoCero != None:
    expresion = expresion.replace(divisionesPuntoCero.group(),"")
  numeros = re.findall('\d+[.]?\d*',expresion)
  resultado = float(numeros[0])
  for i in range(1, len(numeros)):
    resultado -= float(numeros[i])
  return resultado

#Multiplicación
def multiplicacion(expresion):
  divisionesPuntoCero = re.search('[.]{1}[0]+',expresion)
  if divisionesPuntoCero != None:
    expresion = expresion.replace(divisionesPuntoCero.group(),"")
  numeros = re.findall('\d+[.]?\d*',expresion)
  i = 0
  resultado = 1
  for i in range(len(numeros)):
    resultado *= float(numeros[i])
  if resultado - int(resultado) == 0:
    resultado = int(resultado)
  return resultado

#División
def division(expresion):
  numeros = re.findall('\d+[.]*\d*',expresion)
  resultado = float(numeros[0])
  resultado = resultado/float(numeros[1])
  return resultado

#Raíz_Cuadrada
def raíz_cuadrada(expresion):
  numeros = re.findall('\d+[.]*\d*',expresion)
  resultado = float(numeros[0])
  resultado = math.sqrt(float(resultado))
  return resultado

#Exponente al cuadrado
def cuadrado(expresion):
  numero = re.findall('\d+[.]*\d*',expresion)
  num = float(numero[0])
  resultado = pow(num,2)
  return resultado

#Seno
def seno(expresion):
  minipatron = re.compile('\d+[.]*\d*')
  numero = minipatron.search(expresion)
  numero = numero.group()
  numero = numpy.radians(float(numero))
  resultado = sin(numero)
  return resultado
  
#Coseno
def coseno(expresion):
  minipatron = re.compile('\d+[.]*\d*')
  numero = minipatron.search(expresion)
  numero = numero.group()
  numero = numpy.radians(float(numero))
  resultado = cos(numero)
  return resultado

#Tangente
def tangente(expresion):
  numero = re.compile('\d+[.]*\d*')
  numero = numero.search(expresion)
  numero = numero.group()
  numero = numpy.radians(float(numero))
  resultado = tan(numero)
  return resultado

#Divisón Entera
def divisionEntera(expresion):
  numeros = re.findall('\d+',expresion)
  resultado = int(numeros[0])
  resultado = resultado/int(numeros[1])
  return int(resultado)

#Residuo
def residuo(expresion):
  numeros = re.findall('\d+[.]*\d*',expresion)
  resultado = float(numeros[0])
  resultado = float(resultado)%float(numeros[1])
  return resultado

#Factorial
def factorial(expresion):
  numero = re.compile('\d+[.]*\d*',expresion)
  resultado = 1
  while numero > 1:
    resultado *= numero
    numero -= 1
  return resultado


#PATRONES

#Patrón de suma No.1
patronSuma = re.compile('[(]{1}[+]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de resta No. 2
patronResta = re.compile('[(]{1}[-]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de multiplicación No.3
patronMultiplicacion = re.compile('[(]{1}[*]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de división No.4
patronDivision = re.compile('[(]{1}[/]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*[)]{1}')

#Patrón de raiz cuadrada No.5
patronRaíz = re.compile('[(]{1}[s]{1}[q]{1}[r]{1}[o]{1}[o]{1}[t]{1}[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de potencia cuadrada No.6
patronCuadrado = re.compile('[(]{1}[s]{1}[q]{1}[r]{1}[ ]{1}\d+[.]*\d*[)]{1}')

#Patrón de seno No.7
patronSeno = re.compile('[(]{1}[s]{1}[e]{1}[n]{1}[ ]{1}\d+[.]*\d*[)]{1}')

#Patrón de coseno No.8
patronCoseno = re.compile('[(]{1}[c]{1}[o]{1}[s]{1}[ ]{1}\d+[.]*\d*[)]{1}')

#Patrón de Tangente No.9
patronTangente = re.compile('[(]{1}[t]{1}[a]{1}[n]{1}[ ]{1}\d+[.]*\d*[)]{1}')

#Patrón de división entera No.10
patronDivisionEntera = re.compile('[(]{1}[d]{1}[i]{1}[v]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de Residuo No.11
patronResiduo = re.compile('[(]{1}[%]{1}[ ]{1}\d+[.]?\d*[ ]{1}\d+[.]?\d*([ ]{1}\d+[.]?\d*)*[)]{1}')

#Patrón de factorial No.12
patronFactorial = re.compile('[(]{1}[f]{1}[a]{1}[c]{1}[t]{1}[!]{1}[ ]\d+[.]*\d*[)]{1}')

#Patrón de número solo No.13
patronSolo = re.compile("[(]?\d+[.]?\d*[)]?")
   
#INICIO DE PROCESO MADRE
def procesoMadre(expresion):
  repetir = True
  while repetir:
    nuevaExpresion = []
    #INICIO RECONOCIMIENTO DE FALLOS         
    #FALLO DE PARÉNTESIS INCONCLUSOS
    parentesisiz = re.findall('[(]',expresion)
    parentesisder = re.findall('[)]',expresion) 
    if len(parentesisiz) != len(parentesisder):
      print("¡ERROR! Expresión inválida (paréntesis inconclusos)")
      expresion = ""
      break
    #FALLO DE PARÉNTESIS SOLOS
    parentesis_solos = re.findall('[(]{1}[]{1}[)]{1}',expresion)
    if parentesis_solos != []:
      print('¡ERROR! Expresión inválida (No se permiten paréntesis solos "()")')
      expresion = ""
      break 
    #FALLO DE RAÍZ NEGATIVA
    raizdeNeg = re.findall('[(]{1}[s]{1}[q]{1}[r]{1}[o]{1}[o]{1}[t]{1}[ ]{1}[-]{1}\d+[.]*\d*[)]{1}',expresion)
    if raizdeNeg != []:
      print('¡ERROR! Expresión inválida (No se permite la raíz cuadrada de un negativo")')
    #PATRONES
    patron1 = patronSuma.search(expresion)
    patron2 = patronResta.search(expresion)
    patron3 = patronMultiplicacion.search(expresion)
    patron4 = patronDivision.search(expresion)
    patron5 = patronRaíz.search(expresion)
    patron6 = patronCuadrado.search(expresion)
    patron7 = patronSeno.search(expresion)
    patron8 = patronCoseno.search(expresion)
    patron9 = patronTangente.search(expresion)
    patron10 = patronDivisionEntera.search(expresion)
    patron11 = patronResiduo.search(expresion)
    patron12 = patronFactorial.search(expresion)
    patron13 = patronSolo.fullmatch(expresion)
    
    
    #SENO
    if patron7 != None:
      nuevaExpresion.append(patron7.group())
      nuevaExpresion[0] = seno(nuevaExpresion[0])
      ubicacion = patron7.span()
      expresion = expresion.replace(patron7.group(),"")
    
    #COSENO
    elif patron8 != None:
      nuevaExpresion.append(patron8.group())
      nuevaExpresion[0] = coseno(nuevaExpresion[0])
      ubicacion = patron8.span()
      expresion = expresion.replace(patron8.group(),"")

    #TANGENTE
    elif patron9 != None:
      nuevaExpresion.append(patron9.group())
      nuevaExpresion[0] = tangente(nuevaExpresion[0])
      ubicacion = patron9.span()
      expresion = expresion.replace(patron9.group(),"")

    #RAIZ CUADRADA
    elif patron5 != None:
      nuevaExpresion.append(patron5.group())
      nuevaExpresion[0] = raíz_cuadrada(nuevaExpresion[0])
      ubicacion = patron5.span()
      expresion = expresion.replace(patron5.group(),"")
   
    #CUADRADO
    elif patron6 != None:
      nuevaExpresion.append(patron6.group())
      nuevaExpresion[0] = cuadrado(nuevaExpresion[0])
      ubicacion = patron6.span()
      expresion = expresion.replace(patron6.group(),"")

    #FACTORIAL
    elif patron12 != None:
      nuevaExpresion.append(patron12.group())
      nuevaExpresion[0] = factorial(nuevaExpresion[0])
      ubicacion = patron12.span()
      expresion = expresion.replace(patron12.group(),"")

    #DIVISIÓN
    elif patron4 != None:
      #Identificador de Errores (División entre 0)
      divisionCero = re.search('[(]{1}[/]{1}[ ]{1}\d+[ ]{1}[0]+[.]?[0]*[)]{1}',expresion)
      if divisionCero != None:
        print("!ERROR! Expresión inválida (No se permite la división entre cero")
        expresion = ""
        break
      #Proceso
      else:
        nuevaExpresion.append(patron4.group())
        nuevaExpresion[0] = division(nuevaExpresion[0])
        ubicacion = patron4.span()
        expresion = expresion.replace(patron4.group(),"")

    #DIVISIÓN ENTERA
    elif patron10 != None:
      # Identificador de Errores (División entre 0)
      divisionCero = re.search('[(]{1}[d]{1}[i]{1}[v]{1}[ ]{1}\d+[ ]{1}[0]+[.]{1}[0]*[)]{1}',expresion)
      if divisionCero != None:
        print("!ERROR! Expresión inválida (No se permite la división entre cero)")
        expresion = ""
        break
      # Proceso 
      else:
        nuevaExpresion.append(patron10.group())
        nuevaExpresion[0] = divisionEntera(nuevaExpresion[0])
        ubicacion = patron10.span()
        expresion = expresion.replace(patron10.group(),"")
      
    #RESIDUO
    elif patron11 != None:
      #Identificador de Errores
      divisionCero = re.search('[(]{1}[%]{1}[ ]{1}\d+[ ]{1}[0]+[.]{1}[0]*[)]{1}',expresion)
      if divisionCero != None:
        print("!ERROR! Expresión inválida (No se permite la división entre cero")
        expresion = ""
        break
      #Proceso
      else:
        nuevaExpresion.append(patron11.group())
        nuevaExpresion[0] = residuo(nuevaExpresion[0])
        ubicacion = patron11.span()
        expresion = expresion.replace(patron11.group(),"")
        
    #MULTIPLICACIÓN
    elif patron3 != None:
      nuevaExpresion.append(patron3.group())
      nuevaExpresion[0] = multiplicacion(nuevaExpresion[0])
      ubicacion = patron3.span()
      expresion = expresion.replace(patron3.group(),"")
      
    #SUMA
    elif patron1 != None:
      nuevaExpresion.append(patron1.group())
      nuevaExpresion[0] = suma(nuevaExpresion[0])
      ubicacion = patron1.span()
      expresion = expresion.replace(patron1.group(),"")
    
    #RESTA
    elif patron2 != None:
      nuevaExpresion.append(patron2.group())
      nuevaExpresion[0] = resta(nuevaExpresion[0])
      ubicacion = patron2.span()
      expresion = expresion.replace(patron2.group(),"")

    #Numero solo
    elif patron13 != None:
      expresion = expresion.replace("(","")
      expresion = expresion.replace(")","")
      break
      
    #FALLO EXPRESIÓN INCORRECTA
    else:
      print("¡ERROR! No existe tal operación")
      expresion = ""
      break
      
    expresion = expresion[:ubicacion[0]] + str(nuevaExpresion) + expresion[ubicacion[0]:]
    expresion = expresion.replace("[","")
    expresion = expresion.replace("]","")

    #Repetidor
    #REFRESCAR BUSQUEDA
    patron1 = patronSuma.search(expresion)
    patron2 = patronResta.search(expresion)
    patron3 = patronMultiplicacion.search(expresion)
    patron4 = patronDivision.search(expresion)
    patron5 = patronRaíz.search(expresion)
    patron6 = patronCuadrado.search(expresion)
    patron7 = patronSeno.search(expresion)
    patron8 = patronCoseno.search(expresion)
    patron9 = patronTangente.search(expresion)
    patron10 = patronDivisionEntera.search(expresion)
    patron11 = patronResiduo.search(expresion)
    patron12 = patronFactorial.search(expresion)
    
    if patron1 != None:
      repetir = True
    elif patron2 != None:
      repetir = True
    elif patron3 != None:
      repetir = True
    elif patron4 != None:
      repetir = True
    elif patron5 != None:
      repetir = True
    elif patron6 != None:
      repetir = True
    elif patron7 != None:
      repetir = True
    elif patron8 != None:
      repetir = True
    elif patron9 != None:
      repetir = True
    elif patron10 != None:
      repetir = True
    elif patron11 != None:
      repetir = True
    elif patron12 != None:
      repetir = True
    elif patron13 != None:
      repetir = True
    else:
      repetir = False

  return(expresion)
  

#FIN PROCESO MADRE

print("           Inicio del programa         ")
print("Gabriel Álvarez    -   Github: galv2003")

#Función Principal#
def main():
  while True:
    expresion = input("Calculadora >> ")
    if expresion == "quit":
      print("Saliendo...")
      print("Gracias por haber usado el programa calculadora")
      break
    else:
      print("Respuesta >> ", procesoMadre(expresion))

main()
