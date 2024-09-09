from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
  criarArquivo(arq)
while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'SAIR'])
  if resposta == 1:
    # Opção de listar o conteúdo de um arquivo!
    lerArquivo(arq)
  elif resposta == 2:
    # Opção de cadastrar uma nova pessoa.
    cabeçalho('NOVO CADASTRO')
    nome = str(input('nome: '))
    idade = leiaInt('Idade: ')
    cadastrar(arq, nome, idade)
  elif resposta == 3:
    cabeçalho('\033[34mAté logo!\033[m')
    break
  else:
    print('\033[31mERRO\033[m digite (1, 2 ou 3)')
  sleep(2)