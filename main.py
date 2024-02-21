def soma(x, y):
  return x + y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  return x / y

def main():

  numero_1 = float(input("Digite o primeiro número: "))
  numero_2 = float(input("Digite o segundo número: "))

  operacao = input("Digite a operação (+, -, *, /): ")

  resultado = None
  if operacao == "+":
    resultado = soma(numero_1, numero_2)
  elif operacao == "-":
    resultado = subtracao(numero_1, numero_2)
  elif operacao == "*":
    resultado = multiplicacao(numero_1, numero_2)
  elif operacao == "/":
    resultado = divisao(numero_1, numero_2)
  else:
    print("Operação inválida!")

  if resultado is not None:
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
  main()
