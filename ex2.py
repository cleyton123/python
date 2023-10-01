nome=str(input('digite seu nome completo:')).strip() #eliminará todos os espaços no início e fim da frase.
#irá verificar se existe o nome 'SILVA' independente da posição.
print('Seu nome existe Silva? {}'.format('silva'in nome.lower()))
#o operador 'in' irá verificar a existencia do nome 'silva',depois o método 'lower()' converterá para minúsculo.  