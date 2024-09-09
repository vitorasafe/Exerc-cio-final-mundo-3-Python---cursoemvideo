def leiaInt(texto):
  while True:
    try: 
      n = int(input(texto))
    except(ValueError, TypeError):
      print('\033[31mERRO:\033[m por favor digite um numero inteiro!')  
      continue
    except(KeyboardInterrupt):
      print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
      return 0
    else:
      return n 
def linha(tam=45):
  return '-' * tam
def cabeçalho(txt):
  print(linha())
  print(f'\033[32m{txt}\033[m'.center(45))
  print(linha())
def menu(lista):
  cabeçalho('MENU PRINCIPAL')
  c = 1
  for item in lista:
    print(f'{c} - \033[34m{item}\033[m')
    c += 1
  print(linha())
  opc = leiaInt('Sua Opção:')
  return opc