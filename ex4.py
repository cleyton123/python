nome=str(input('digite seu nome completo: ')).strip()
a=nome.split() #divide o nome separadamente por palavras.
print('Seu primeiro nome é {}'.format(a[0]))
print('Seu último nome é {}'.format(a[len(a)-1]))  #len(a)-1 calcula o índice do último elemento na sequência a. Como os índices em Python começam em 0, subtrair 1 do comprimento da sequência nos dá o índice do último elemento. 