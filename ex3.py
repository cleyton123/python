frase=str(input('Digite uma frase: ')).strip().lower() #elimina os espaços e converte a frase para minúsculo.
print('Sua frase possui {} letras a.'.format(frase.count('a'))) #realiza a contagem da letra 'a' na frase.
print('a primeira letra a aparece na posição {}'.format(frase.find('a')+1))
print('a última letra a aparece na posição {}'.format(frase.rfind('a')+1)) #mostra a última posição de 'a' a partir da direita(r).