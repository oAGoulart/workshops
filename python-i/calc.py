# Atividade para praticar sintaxe do Python
# Autor: Augusto Goulart
# Objetivo:
#   Organizar o código para que utilize uma função para cada operação
#   Utilizar o módulo 'argparse' para receber os argumentos da linha de comando
#   Utilizar o módulo 'logging' para gerar logs
# Observações:
#   Em Python, a indentação é obrigatória e é utilizada para definir blocos de código
#   Em Python, não há chaves '{' e '}' para definir blocos de código
#   Em Python, não há ponto e vírgula ';' para finalizar instruções

# Abaixo podemos ver a importação de módulos
# A palavra-chave 'import' é utilizada para importar módulos
import argparse
import logging

# Abaixo podemos ver a definição de funções
# A palavra-chave 'def' é utilizada para definir funções
def soma(a, b):
  # Aqui, 'a' e 'b' podem ser números inteiros 'int' ou números de ponto flutuante 'float'
  # Bem como, podem ser strings 'str' ou qualquer outro tipo de dado
  return a + b

# Em Python não há função 'main' padrão, abaixo será explicado o porquê
def main():
  # Aqui estamos definindo o nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  logging.basicConfig(level=logging.DEBUG)
  # Em Python, variáveis podem ser declaradas sem tipo, algo similar ao 'var' do JavaScript
  # ou o 'auto' do C++11
  parser = argparse.ArgumentParser()
  # O objeto 'parser' é uma instância da classe 'ArgumentParser' do módulo 'argparse'
  # Esta classe é utilizada para definir argumentos de linha de comando
  # Como no exemplo abaixo, o argumento '-a' é definido como um número flutuante
  parser.add_argument('a', type=float, help='Primeiro número')
  parser.add_argument('b', type=float, help='Segundo número')

  # Aqui será extraído os valores da linha de comando
  args = parser.parse_args()
  # O objeto 'args' é uma instância da classe 'Namespace'
  # Esta classe é utilizada para armazenar os valores dos argumentos
  # Como no exemplo abaixo, o valor do argumento '-a' é acessado através de 'args.a'
  logging.info('Valor de a: %s', args.a)
  operation = '+' # Operação padrão, utilize o 'argparse' para definir esta variável

  # Em Python não há switch/case, mas podemos utilizar o 'if' para verificar valores
  result = None # O valor 'None' é utilizado para representar um valor nulo
  if operation == '+':
    # Aqui é chamada a função 'soma' definida acima
    # O valor retornado pela função é armazenado na variável 'result'
    result = soma(args.a, args.b)
  elif operation == '-':
    result = args.a - args.b
  elif operation == '*':
    result = args.a * args.b
  elif operation == '/':
    result = args.a / args.b
  else:
    logging.error('Operação inválida: %s', operation)
    return
  
  # Aqui é exibido o resultado
  logging.info('Resultado: %s', result)

# Em Python, o código que está fora de funções é executado quando o arquivo é executado
# Por exemplo, ao executar o arquivo 'calc.py' no terminal, o código abaixo seria executado
# print(soma(1, 2)) # o resultado seria 3
# Para definir o que deve ser executado quando o arquivo é chamado, é necessário utilizar
# a sintaxe abaixo
if __name__ == '__main__':
  # Todo o código dentro do bloco 'if' será executado quando o arquivo for chamado
  main()
