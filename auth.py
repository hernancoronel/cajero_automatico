# Definimos la clase Autenticacion
class Autenticacion:
  
  # Constructor de la clase, inicializa con DNI válido, contraseña válida y sesión no iniciada
  def __init__(self, dni_valido, contraseña_valida):
    self.dni_valido = dni_valido  # Almacena el DNI válido recibido como parámetro
    self.contraseña_valida = contraseña_valida  # Almacena la contraseña válida recibida como parámetro
    self.sesion_iniciada = False  # Inicializa la sesión como no iniciada

  # Método para iniciar sesión con un DNI y contraseña dados
  def iniciar_sesion(self, dni, contraseña):
    if dni == self.dni_valido and contraseña == self.contraseña_valida:  # Comprueba si las credenciales coinciden con las válidas
      self.sesion_iniciada = True  # Marca la sesión como iniciada si las credenciales son correctas
      return True  # Devuelve True para indicar que la sesión se inició correctamente
    else:
      return False  # Devuelve False si las credenciales son incorrectas