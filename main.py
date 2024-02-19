# Caso complicado
def str_endereco(endereco):
  parte_endereco = endereco.split()  # Divide o endereço
  nome_rua = ''
  numero_rua = ''

for i, parte in enumerate(parte_endereco):
  if parte.isdigit() or (parte[0].isdigit() and i > 0 and not parte_endereco[i-1].isdigit()):  # Espaço núm/letra
      if numero_rua and not parte.isdigit():  
          numero_rua += parte  