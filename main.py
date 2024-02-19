# Caso Complicado
def str_endereco(endereco):
    parte_endereco = endereco.split()  # Divide o endereço
    nome_rua = ''
    numero_rua = ''

    for parte in parte_endereco:
        if parte.isdigit() or (parte[0].isdigit() and not parte_endereco[parte_endereco.index(parte)-1].isdigit()):  #Espaço núm/letra
            if numero_rua: 
                numero_rua += parte  
            else:
                numero_rua = parte  
        else:  # Se não for um número
            nome_rua += parte + ' '

    return nome_rua.strip(), numero_rua.strip()


