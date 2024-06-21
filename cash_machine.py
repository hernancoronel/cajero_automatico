#Importando clases desde otros modulos
from datetime import datetime  
from auth import Autenticacion  
from transaction import Transaccion  
from user_interface import InterfazUsuario 

#Definimos la clase CajeroAutomatico
class CajeroAutomatico:
  def __init__(self, autenticacion, transaccion):
    self.autenticacion = autenticacion  # Inicializamos la instancia de Autenticacion
    self.transaccion = transaccion  # Inicializamos la instancia de Transaccion

  def iniciar_operaciones(self): 
    while True:
      if not self.autenticacion.sesion_iniciada:  # Verificamos si la sesión no está iniciada
        self.iniciar_sesion()  # Llamamos al método para iniciar sesión
        
      if not self.menu_principal():  # Verificamos si el usuario no ha elegido salir del menú principal
        break  # Salimos del ciclo principal si no se desea continuar

  def iniciar_sesion(self):
    while not self.autenticacion.sesion_iniciada:  # Mientras la sesión no esté iniciada
      dni = input("Ingrese su DNI: ")
      contraseña = input("Ingrese su contraseña: ")
      if not self.autenticacion.iniciar_sesion(dni, contraseña):  # Intentamos iniciar sesión con el DNI y contraseña ingresados
        print("DNI o contraseña incorrectos. Por favor, inténtelo de nuevo.")
      else:
        print("Sesión iniciada correctamente.")

  def menu_principal(self):
    while True:
      print("Bienvenido al cajero automático, ¿desea realizar alguna operación?")
      opcion_principal = InterfazUsuario.seleccionar()  # Mostramos el menú de opciones y obtenemos la selección del usuario
      
      if opcion_principal == "1":
        self.realizar_operacion()  # Llamamos al método para realizar una operación
      elif opcion_principal == "2":
        print("Sesión cerrada. ¡Hasta luego!")
        self.autenticacion.sesion_iniciada = False  # Marcamos la sesión como no iniciada al salir
        return False  # Salimos del menú principal y terminamos la ejecución
      else:
        print("Opción inválida. Por favor, intente de nuevo.")

  def realizar_operacion(self):
    while True:
      InterfazUsuario.mostrar_menu()  # Mostramos el menú de operaciones disponibles
      opcion = InterfazUsuario.obtener_opcion()  # Obtenemos la opción elegida por el usuario

      if opcion == "1":
        self.depositar_dinero()  # Llamamos al método para depositar dinero
      elif opcion == "2":
        self.retirar_dinero()  # Llamamos al método para retirar dinero
      elif opcion == "3":
        self.ver_saldo()  # Llamamos al método para ver el saldo
      elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        return  # Salimos del ciclo de operaciones si se elige salir
      else:
        print("Opción inválida. Por favor, intente de nuevo.")

      if not self.realizar_nueva_operacion():  # Preguntamos al usuario si desea realizar otra operación
        return  # Salimos del ciclo de operaciones si no se desea continuar

  def depositar_dinero(self):
    try:
      monto = float(input("Ingrese el monto que desea depositar: "))  # Solicitamos al usuario ingresar el monto a depositar
      nuevo_saldo = self.transaccion.depositar_dinero(monto)  # Llamamos al método para depositar dinero en la instancia de Transaccion
      print(f"Has depositado ${monto}, su saldo actual es ${nuevo_saldo}.")  # Mostramos el mensaje de confirmación
    except ValueError as e:
      print(f"Error: {e}")  # Capturamos y mostramos cualquier error de valor

  def retirar_dinero(self):
    try:
      monto = float(input("Ingrese el monto que desea retirar: "))  # Solicitamos al usuario ingresar el monto a retirar
      nuevo_saldo = self.transaccion.retirar_dinero(monto)  # Llamamos al método para retirar dinero en la instancia de Transaccion
      print(f"Has retirado ${monto}, su saldo actual es ${nuevo_saldo}.")  # Mostramos el mensaje de confirmación
      self.imprimir_ticket(monto)  # Llamamos al método para imprimir el ticket de la transacción
    except ValueError as e:
      print(f"Error: {e}")  # Capturamos y mostramos cualquier error de valor

  def ver_saldo(self):
    print(f"Su saldo actual es {self.transaccion.saldo}")  # Mostramos el saldo actual almacenado en la instancia de Transaccion

  def realizar_nueva_operacion(self):
    while True:
      respuesta = input("¿Desea realizar otra operación? (s/n): ")  # Preguntamos al usuario si desea realizar otra operación
      if respuesta.lower() == 's':
        return True  # Retornamos True si el usuario desea continuar
      elif respuesta.lower() == 'n':
        return False  # Retornamos False si el usuario no desea continuar
      else:
        print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")  # Mostramos un mensaje de error si la respuesta no es válida

  def imprimir_ticket(self, monto):
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtenemos la fecha y hora actual
    mensaje = f"El tipo de operación ha sido una extracción de dinero, usted ha extraído: {monto}$ y su saldo actual es igual a {self.transaccion.saldo}$\n"
    mensaje += f"Fecha y hora de la extracción: {fecha_hora_actual}\n"
    with open("ticket.txt", "a") as archivo:
      archivo.write(mensaje)  # Escribimos el mensaje en el archivo ticket.txt
      archivo.write('\n')  # Agregamos una línea en blanco después de cada mensaje

def main():
  dni_valido = "12345678"  # Definimos el DNI válido para la autenticación
  contraseña_valida = "MiPassword"  # Definimos la contraseña válida para la autenticación
  autenticacion = Autenticacion(dni_valido, contraseña_valida)  # Creamos una instancia de Autenticacion con los datos válidos
  transaccion = Transaccion()  # Creamos una instancia de Transaccion para las operaciones financieras
  cajero = CajeroAutomatico(autenticacion, transaccion)  # Creamos una instancia de CajeroAutomatico para gestionar el cajero automático
  cajero.iniciar_operaciones()  # Iniciamos las operaciones del cajero automático

# Punto de entrada principal del programa
if __name__ == "__main__":
  main()  # Llamamos a la función main para iniciar el programa