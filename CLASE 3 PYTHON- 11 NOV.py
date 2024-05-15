 # ACTIVIDAD 29: SE INGRESAN LAS MEDIDAS DE FRENTE Y FONDO DE UN TERRENO.
  # DETERMINAR SI ES CUADRADO O RECTANGULAR Y CALCULAR SU PERIMETRO Y SUPERFCIE.
  # A) IDENTIFICACION DE LOS COMPONENTES
  # B) DIAGRAMA DE FLUJO
  # C) CODIFICA LA SOLUCION
  
  
#ENTRADA
 
frente=float(input('Ingrese valor de frente del terreno: '))
fondo=float(input('Ingrese valor de fondo del terreno: '))
#PROCESO Y SALIDA
superrect= frente*fondo
perirect= (frente*2) + (fondo*2)

supercuad= frente*fondo
pericuad= frente*4

if frente == fondo:
    print('El terreno es cuadrado.')
    print('La superficie es de:',supercuad,'metros')
    print('El perímetro es de:', pericuad,'metros cuadrados')
else:
    print('El terreno es rectangular. La superficie es de:',superrect, 'metros y el perímetro es de:', perirect,'metros cuadrados')




        