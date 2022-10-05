# Atividade para praticar sintaxe do Python
# Autor: Augusto Goulart
# Objetivo:
#   Organizar o código para que possa gerar nomes femininos e masculinos
#   Permitir o usuário escolher qual opção
#   Utilizar o módulo 'random' para selecionar os nomes

import logging
import random

def get_names(file):
  # Em Python, 'with' cria um contexto de execução que permite executar um grupo de instruções sob um gerenciador
  # Aqui estamos executando 'open' e armazenando o resultado em 'f'
  # Então, se não houver erros, o código dentro do bloco de código identado é executado
  # Ao finalizar o bloco, 'with' normalmente fornece a lógica de desmontagem ou o código de limpeza
  # Ou seja, chamar o método '.close()' em um objeto de arquivo aberto
  # É por isso que a instrução 'with' é tão útil, pois facilita a aquisição e liberação de recursos adequadamente
  with open(file) as f:
    names = []
    
    # Agora podemos utilizar o laço 'for' para iterar cada linha do arquivo 'f'
    for line in f:
      # A variável 'names' é uma lista, essas contém o método 'append', usado para acrescentar itens nela
      # A variável 'line' é uma string, aqui estamos usando o método 'strip' para remover espaços extras
      names.append(line.strip())
    
    # Retornamos a lista criada
    return names

def main():
  logging.basicConfig(level=logging.DEBUG)

  # Aqui devemos utilizar a função definida acima para carregar os nomes a serem utilizados
  male_names = get_names("male_first_names.txt")
  female_names = get_names("female_first_names.txt")
  last_names = get_names("last_names.txt")

  # Em Python, 'try' permite testar um bloco de código quanto a erros
  # Quando ocorre um erro, ou exceção, como chamamos, o Python normalmente para e gera uma mensagem de erro
  # Porém se utilizamos 'try' é possível gerenciar o quê será feito em caso de uma exceção
  # Aqui, as instruções dentro do bloco 'try' serão executadas e se houver uma exceção, pulamos para o 'except'
  # O 'except' aceita especificar o tipo de exceção e se essa for do tipo esperado então o código dentro do bloco é executado
  try:
    while True:
      # Aqui estamos usando a função 'input' para ler da interface da linha de comando
      gender = input("Masculino ou feminino: ")

      # Aqui estamos gerando um name aleatório e imprimindo no terminal
      # O módulo 'random' possui uma função que permite selecionar um item aleatório de uma lista
      print(random.choice(male_names))

  except KeyboardInterrupt:
    logging.info('\nFim do programa')

if __name__ == '__main__':
  main()
