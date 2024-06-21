#Definimos la clase InterfazUsuario
class InterfazUsuario:
  
  # Método estático para mostrar las opciones de selección inicial
  @staticmethod
  def seleccionar():
    print("1. Mostrar menu")  # Imprime la opción para mostrar el menú
    print("2. Cerrar sesion")  # Imprime la opción para cerrar la sesión
    
    # Solicita al usuario que elija una opción (1 o 2)
    return input("Indique la operación que desea realizar (1, 2): ")  

  # Método estático para mostrar el menú principal de operaciones
  @staticmethod
  def mostrar_menu():
    print("1. Depositar dinero")  # Imprime la opción para depositar dinero
    print("2. Retirar dinero")  # Imprime la opción para retirar dinero
    print("3. Consultar saldo")  # Imprime la opción para consultar el saldo
    print("4. Salir")  # Imprime la opción para salir del programa

  # Método estático para obtener la opción seleccionada por el usuario
  @staticmethod
  def obtener_opcion():
    # Solicita al usuario que elija una opción (1, 2, 3, o 4)
    return input("Indique la operación que desea realizar (1, 2, 3, 4): ")  