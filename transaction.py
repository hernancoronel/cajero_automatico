import random  # Importamos el módulo random para generar números aleatorios

# Definimos la clase Transaccion
class Transaccion:
  
  # Constructor de la clase, inicializa el saldo con un valor aleatorio entre 1 y 10000
  def __init__(self):
    self.saldo = random.randint(1, 10000)  # Inicializa el saldo con un número aleatorio entre 1 y 10000

  # Método para depositar dinero en la cuenta
  def depositar_dinero(self, monto):
    if monto <= 0:  # Verifica si el monto a depositar es menor o igual a cero
      raise ValueError("El monto a depositar debe ser mayor que cero.")  # Levanta una excepción si el monto es inválido
    self.saldo += monto  # Incrementa el saldo con el monto depositado
    return self.saldo  # Devuelve el saldo actualizado después del depósito

  # Método para retirar dinero de la cuenta
  def retirar_dinero(self, monto):
    if monto <= 0:  # Verifica si el monto a retirar es menor o igual a cero
      raise ValueError("El monto a retirar debe ser mayor que cero.")  # Levanta una excepción si el monto es inválido
    if monto > self.saldo:  # Verifica si el monto a retirar es mayor que el saldo disponible
      raise ValueError("Fondos insuficientes.")  # Levanta una excepción si no hay suficientes fondos para el retiro
    self.saldo -= monto  # Reduce el saldo con el monto retirado
    return self.saldo  # Devuelve el saldo actualizado después del retiro