#aca en esta parte estamos importando una clase que trae ya python instalada que se llama basicamente clases base abstracta
from abc import ABC, abstractmethod
#aca en esta parte estamos trayendo una herramienta de python que sirve para obtener fechas y horas.
from datetime import datetime

#creamos las excepciones personalizadas que pide el sistema de gestion
#esto es para un error general del sistema
class ErrorSistema(Exception):
 pass
 #esto es para cuando un dato no cumple con las reglas
class DatoInvalidoError(ErrorSistema):
 pass
 #esto es para cuando hay algun problema con la reserva
class ReservaInvalidaError(ErrorSistema):
 pass
 #esto es para cuando el servicio no esta disponible
class ServicioNoDisponibleError(ErrorSistema):
 pass

  # creamos la clase cliente con sus atributos
# creamos la opcion de que si no  escribe algun nombre salga un aviso que diga identificacion y nomnre son obligatorios
class Cliente:
 def __init__ (self,identificacion,nombre,correo,telefono):
  if not identificacion or not nombre:
   raise DatoInvalidoError("identificacion y nombre son obligatorios")
#aca estamos almacenando los datos de cliente dentro de la clase cliente
#el guion bajo, significa que los datos son privados y no se pueden modificar desde afuera, solo la propia clase cliente lo puede cambiar
  self._identificacion = identificacion
  self._nombre = nombre
  self._correo = correo
  self._telefono = telefono
#en esta parte de abajo, como los datos estan protegidos necesitamos como un acceso para poder leerlos, solo se lee la informacion, no se puede modificar nada

 def obtener_nombre(self):
   return self._nombre

 def obtener_identificacion(self):
   return self._identificacion

 def obtener_correo(self):
   return self._correo

 def obtener_telefono(self):
   return self._telefono

# en esta parte estamos diciendo que nos imprima o nos muestre el nombre  y el id de la persona que registramos
 def __str__(self):
   return f"{self.obtener_nombre()}|{self.obtener_identificacion()}"

#creamos la clase abstracta de servicio
#(ABC) significa clase abstracta 

class Servicio(ABC):

#creamos el constructor que se ejecuta automaticamente cada ves que creamos una nueva clase

 def __init__ (self,nombre,descripcion,precio_base):

#aca se guarda la informacion de cada ciente de forma segura

   self._nombre = nombre
   self._descripcion = descripcion
   self._precio_base = precio_base

#que hace @abstractmethod? es una regla que dice que cualquier clase que herede d servicio debe crear su propio metodo de calcular_costo()

 @abstractmethod

#aqui se declara la funcion calcular_costos() pero no dice como ira a funcionar
 def calcular_costos(self):
   pass
#aca creamos una funcion para mostrar los datos del servico que contratamos
 def mostrar_informacion(self):
   return f"{self._nombre}: {self._descripcion} | costos {self.calcular_costos():,.2f}"
 
#creamos las clases hijas con sus propios atributos
#creamos la clase hija llamada reserva sala que heredara todo lo que tiene la clase servicio
class ReservaDeSala(Servicio):
#creamos el constructor que se necesita para crear una reserva de sala, aparte tambien se necesita saber cuantas personas caben...
 def __init__ (self,nombre,descripcion,precio_base,capacidad_personas):
#aca lee estamos diciendo que valla a la clase padre y guarde los 3 datos, es el paso de herencia
  super().__init__(nombre,descripcion,precio_base)
#aca guardamos que es de la capacidad de las salas, cuantas personas pueden entrar.
  self._capacidad_personas = capacidad_personas
#aca calculamos el costo, el presio es fijo cada servicio de calcula su costo diferente
 def calcular_costos(self):
  return self._precio_base

  
#ahora creamos la 2da clase hija, que se llama alquiler de equipos, que tambien heredara de la clase servicio

class AlquilerDeEquipo(Servicio):
# aca creamos el constructor de este servicio  que nos dice cuantos dias se va a alquilar
 def __init__ (self,nombre,descripcion,precio_base,dias_alquiler):
  super().__init__(nombre,descripcion,precio_base)
# aca guardamos la cantidad de dias que se va a alquilar
  self.dias_alquiler = dias_alquiler

# aca calculamos el costo, multiplicamos el precio base por los dias que se va a usar
 def calcular_costos(self):
  return self._precio_base * self.dias_alquiler


#ahora creamos la 3ra clase hija, que se va a llamar asesoria especializada, que tambien heredara de la clase servico

class AsesoriaEspecializada(Servicio):
#aca creamos el constructor de este servico que nos dice cuantas horas durara el servicio
 def __init__ (self,nombre,descripcion,precio_base,horas_asesoria):
  super().__init__(nombre,descripcion,precio_base)
#aca guardamos las horas que va a tener la asesoria
  self._horas_asesoria = horas_asesoria
  
#aca calculamos el costo, y ponemos una condicion, si la asesoria pasa mas de 2 horas aplicamos el 10% de descuento, si no, no se aplica
 def calcular_costos(self):
  descuento = 0.10 if self._horas_asesoria > 2 else 0
#aca seria el calculo del precio final menos el descuento si llega a aplicar
  return self._precio_base * self._horas_asesoria * (1 - descuento)

#creamos una nueva clase llamada reserva, que basicamente es el vicnulo entre los clientes y el servicio
#sin la esta clase solo se tendrian clientes por un lado y servicion por otro sin ninguna conexion.

class Reserva:
#aca se crea el constructor ya que para hacer una reserva se necesita saber quien fue y que servicio esta reservando y cuando.
 def __init__ (self,cliente,servicio,fecha_reserva):
  if not isinstance(cliente, Cliente):
   raise DatoInvalidoError("el cliente no es valido")
  if not isinstance(servicio, Servicio):
    raise DatoInvalidoError("el servicio no es valido")
#aca se verifica que real realmente la fecha sea del presente, o sino el sistema lanza un error  
  if fecha_reserva < datetime.now():
   raise ReservaInvalidaError("no puede reservarse en una fecha que ya paso")
#aca si todo esta bien, guarda la informacion suministrada
  self.cliente = cliente
  self.servicio = servicio
  self.fecha_reserva = fecha_reserva

#aca mostramos un detallado de la informacion suministrada en la pantalla para que el cliente la vea y verifique que todo este bien
 def obtener_informacion(self):
#aca se llama al metodo del cliente para obtener su nombre
  return (f"====RESERVA====\n"
  f"cliente: {self.cliente.obtener_nombre()}\n"
#aca cambiamos el formato de la fecha para que se pueda ver mejor, dia,mes,año,hora y minutos
  f"fecha: {self.fecha_reserva.strftime('%d/%m/%Y %H:%M:%S')}\n"
#aca usamos el metodo calcular_costos de cada servicio para saber cuanto cuesta
  f"servicio: {self.servicio.mostrar_informacion()}\n"
  f"costo total: {self.servicio.calcular_costos():,.2f}\n"
  f"===============")

#creamos la clase llamada sistema de gestion, que nos permite organizar toda la infomacion, los clientes, servicio y reservas
#tambien nos la muestra cada que la necesitamos

class SistemaDeGestion:
#aca creamos 3 listas vacias, una para cada cosa, ademas aca se guarda la informacion de clientes, servicios y reservas
 def __init__ (self):
  self.Clientes = []
  self.Servicios = []
  self.Reservas = []

#agregamos un  servicio a la lista y se envia confirmacion
 def agregar_cliente(self,cliente):
  self.Clientes.append(cliente)
  print(f"Cliente {cliente.obtener_nombre()} agregado exitosamente.")

#agregamos una reserva a la lista y se envia confirmacion
 def agregar_servicio(self,servicio):
  self.Servicios.append(servicio)
  print(f"Servicio {servicio._nombre} agregado exitosamente.")

#agregamos una reserva a la lista y se envia su confirmacion
 def realizar_reserva(self, reserva):
  self.Reservas.append(reserva)
  print(f"Reserva realizada exitosamente")

#mostramos un titulo agradable y recorre la lista cliente y mostramos cada cliente
 def lista_clientes(self):
  print("===LISTA DE CLIENTES===")
  print(f"cantidad de clientes: {len(self.Clientes)}")
  if len(self.Clientes) == 0:
   print("No hay clientes registrados.")
   return
  for c in self.Clientes:
   print (f"- {c.obtener_nombre()} | {c.obtener_identificacion()} | {c.obtener_correo()} | {c.obtener_telefono()}")

#mostramos un titulo agradable y recorre la lista, usamos su metodo mostrar_informacion
 def lista_servicios(self):
  print("===LISTA DE SERVICIOS DISPONIBLES===")
  for s in self.Servicios:
   print (f"- {s.mostrar_informacion()}")

#aca se revisa la lista, si esta vacia muestra un mensaje 
 def lista_reservas(self):
  print("===LISTA DE RESERVAS===")
  if not self.Reservas:
   print("No hay reservas registradas.")

#si hay reservas se recorre la lista y muestra cada una de ellas con su formato completo
  else:
    for r in self.Reservas:
      print(r.obtener_informacion())

#aca estamos basicamente creando el menu principal del sistema de gestion de reservas, aca se va a mostrar todo lo que se registro, clientes, servicios y reservas
if __name__ == "__main__":
#aca creamos una instancia de la clase sistemadegestion, que es la que va a manejar todo el sistema de reservas
  sistema = SistemaDeGestion()
#aca creamos un ciclo que va a mostrar el menu principal del sistema de gestion de reservas, hasta que el usuario decida salir del sistema
  while True:
#aca muestra unas lineas de separacion y un mensaje de bienvenida al sistema de gestion de reservas junto con las opciones que el usuario puede elegir, registrar clientes, registrar servicios, realizar reservas, mostrar lista de clientes o salir del sistema
    print("\n"+ "="*50)
    print("Bienvenido al sistema de gestión de reservas")
    print("="*50)
    print("1. Registrar clientes")
    print("2. Registrar servicios")
    print("3. Realizar reservas")
    print("4. Mostrar lista de clientes")
    print("5. salir")
    opcion = input("Seleccione una opción: ")
#aca agregamos un bloque de condicionales para que el usuario pueda elegir la opcion que desea realizar, registrar clientes, registrar servicios, realizar reservas, mostrar lista de clientes o salir del sistema
    if opcion == "1":
#aca pedimos al usuario que ingrese la informacion del cliente, identificacion, nombre, correo y telefono
      identificacion = input("Ingrese la identificación del cliente: ")
      nombre = input("Ingrese el nombre del cliente: ")
      correo = input("Ingrese el correo del cliente: ")
      telefono = input("Ingrese el teléfono del cliente: ")

#aca inicia un bloque try para manejar posibles errores que puedan ocurrir durante la ejecución del código
      try:
          c = cliente(identificacion, nombre, correo, telefono)
#aca llamamos a la funcion registrar_cliente para agregar el cliente a la lista de clientes dentro del sistema de gestion de reservas
          sistema.agregar_cliente(c)
#aca manejamos el error de datos invalidos, si ocurre un error de este tipo, se muestra un mensaje de error al usuario
      except DatoInvalidoError as e:
          print(f"Error de datos: {e}")
#aca ejecutamos la opcion 2 si el cliente elige registrar servicios, aca pedimos al usuario que ingrese la informacion del servicio, tipo de servicio, nombre, descripcion y precio base
    elif opcion == "2":
#aca muestra un mensaje de que tipo de servicios hay disponibles y pide al usuario que ingrese el tipo de servicio, nombre, descripcion y precio base
      print("\ntipo de servicios: 1=Reserva de sala | 2=Alquiler de equipo | 3=Asesoría especializada\n")
      tipo_servicio = input("Ingrese el tipo de servicio (1, 2 o 3): ")
      nombre = input("Ingrese el nombre del servicio: ")
      descripcion = input("Ingrese la descripción del servicio: ")
      precio_base = float(input("Ingrese el precio base del servicio: "))
#aca si eligio 1 pide la capacidad de personas, si eligio 2 pide los dias de alquiler, si eligio 3 pide las horas de asesoria, si no eligio ninguna de estas opciones muestra un mensaje de error y vuelve a mostrar el menu principal,  y asi para las otras opciones, si el usuario ingresa un valor no valido para la capacidad, dias de alquiler o horas de asesoria, se muestra un mensaje de error y vuelve a mostrar el menu principal
      try:
          if tipo_servicio == "1":
              capacidad_personas = int(input("Ingrese la capacidad de personas: "))
              s = ReservaDeSala(nombre, descripcion, precio_base, capacidad_personas)
          elif tipo_servicio == "2":
              dias_alquiler = int(input("Ingrese la cantidad de días de alquiler: "))
              s = AlquilerDeEquipo(nombre, descripcion, precio_base, dias_alquiler)
          elif tipo_servicio == "3":
              horas_asesoria = int(input("Ingrese la cantidad de horas de asesoría: "))
              s = AsesoriaEspecializada(nombre, descripcion, precio_base, horas_asesoria)
          else:
              print("Tipo de servicio inválido.")
              continue
#aca llamamos a la funcion registrar_servicio para agregar el servicio a la lista de servicios dentro del sistema de gestion de reservas
          sistema.agregar_servicio(s)
#aca manejamos el error de datos invalidos, si ocurre un error de este tipo, se muestra un mensaje de error al usuario
      except ValueError:
          print("Error: Debe ingresar un número válido para la capacidad, días de alquiler o horas de asesoría.")
#aca ejecutamos la opcion 3 si el cliente elige realizar reservas, aca pedimos al usuario que seleccione un cliente y un servicio de las listas disponibles, y luego ingrese la fecha de la reserva
    elif opcion == "3":
      print ("\n---selecciona cliente (por numero)---\n")
      for i, cli in enumerate(sistema.Clientes):
          print(f"{i}. {cli}")
#aca pedimos al usuario que seleccione un cliente y un servicio de las listas disponibles, y luego ingrese la fecha de la reserva
      cliente_index = int(input("Seleccione el número del cliente: "))
      print("\n---selecciona servicio (por numero)---\n")
      for i, servicio in enumerate(sistema.Servicios):
          print(f"{i}. {servicio.mostrar_informacion()}")
#aca pedimos al usuario que seleccione un servicio de las listas disponibles, y luego ingrese la fecha de la reserva
      servicio_index = int(input("Seleccione el número del servicio: "))
      anio = int(input("año: "))
      mes = int(input("mes: "))
      dia = int(input("dia: "))
      hora = int(input("hora: "))
      minuto = int(input("minuto: "))
#aca intenta crear la fecha de la reserva y luego llama a la funcion realizar_reserva para agregar la reserva a la lista de reservas dentro del sistema de gestion de reservas, si ocurre un error de reserva o un error de indice invalido, se muestra un mensaje de error al usuario
      try:
          fecha_reserva = datetime(anio, mes, dia, hora, minuto)
          cliente = sistema.Clientes[cliente_index]
          servicio = sistema.Servicios[servicio_index]
          reserva = Reserva(cliente, servicio, fecha_reserva)
          sistema.realizar_reserva(reserva)
#aca manejamos el error de reserva invalida, si ocurre un error de este tipo, se muestra un mensaje de error al usuario
      except ReservaInvalidaError as e:
          print(f"Error de reserva: {e}")
      except IndexError:
          print("Error: Índice de cliente o servicio inválido.")
    elif opcion == "4":
        sistema.lista_clientes()
    elif opcion == "5":
      print("gracias por usar nuestro sistema :) hasta luego...")
      break
    else:
      print("Opción inválida. Por favor, seleccione una opción válida.")


          
