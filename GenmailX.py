### GENERADOR DE CORREOS ELECTRONICOS #####
import os, random
cg='correos_generados.txt'
def limpiar_consola():
	so=os.name
	if so == 'nt':
		os.system("cls")
	else:
		os.system("clear")

def generador_de_correos():
 if os.path.exists(cg):
 	os.remove(cg)
 limpiar_consola()
 ccorreo=int(input(" CANTIDAD DE CORREOS A GENERAR -> "))
 print("")
 for i in range(0, ccorreo):
  names=[]
  na0=[]
  cx='@gmail.com'
  
  nombres=[
  'juan', 'pedro', 'elias', 'ramon', 'david', 'karol', 'carmen', 'snake', 'killah', 'Alcohon', 'dinora', 'josefina', 'jennifer', 'cesar', 
  'alejandra', 'alejandro', 'marcos', 'mirna', 'erick', 'venesia', 'emily', 'alberto', 'eibar', 'ivan', 'roberto',
  'junior', 'lacra', 'miguel', 'agustin', 'ghost', 'ryder', 'ranyer', 'pepe', 'argelia', 'miranda', 'cilia', 'anonymous',
  'mus', 'mickey', 'lorena', 'ardiente', 'darkfire', 'dark', 'black', 'nirvana', 'marduk', 'lmentrix', 'humano', 'perro',
  'gato', 'kat', 'cat', 'dog', 'pitbull', 'doberman', 'zone', 'mustang', 'cadillac', 'xxx', 'kawasaki', 'puma', 'leon',
  'jaguar', 'oso', 'india', 'xaomi', 'samsung', 'cristian', 'cristos', 'kripton', 'luxec', 'rat', 'penelope', 'kbron',
  'lebron', 'denzel', 'hanset', 'onichan', 'goku', 'veggeta', 'sayayin', 'pandora', 'kylian', 'messi', 'cristiano',
  'ronaldo', 'cr7ronaldo', 'damian', 'engel', 'demond', 'daemon', 'xnxx', 'oro', 'metal', 'metalero', 'rockero', 
  'kiss', 'dorks', 'azazel', 'belcebu', 'crack', 'libertad', 'anarquia', 'power', 'block', 'electrico', 'android',
  'robot', 'pc', 'cpu', 'software', 'axel', 'shemblack', 'alcohonwhite', 'kasper', 'atom', 'viajero', 'p443', 'puerto80_',
  'puerto8080_', 'puta', 'perrisimo', 'perrisima'
  ]
  for i in nombres:
  	n=random.randint(0,9)
  	if n > 6:
  		names.append(i[0].upper() + i[1:])
  	else:
  		names.append(i)
  rango=random.randint(3,6) + 1
  for i in range(1, rango):
  	na=random.randint(0,9)
  	na0.append(na)
  numeros_aleatorios=''.join(str(na0).replace('[', '').replace(']', '').replace(', ', ''))
  cantidad=len(names) - 1
  nal=random.randint(0, cantidad)
  posicion=random.randint(1,2)
  if posicion == 1:
   correo=f"{names[nal]}{numeros_aleatorios}{cx}"
  elif posicion == 2:
  	correo=f"{numeros_aleatorios}{names[nal]}{cx}"
  print(f" {correo}")
  with open(cg, 'a') as f:
  	f.write(correo + '\n')
  	f.close()

 print(f'\n {ccorreo} (gmail) Guardados en [correos_generados.txt]\n SI PRESIONA ENTER SE BORRARAN ESTOS CORREOS DEL .TXT')
 input()
 generador_de_correos() 
generador_de_correos()
 