altura=float(input('Qual é sua altura?'))
peso=float(input('Qual é o seu peso?'))
#calculo do IMC
imc= peso/altura**2
print(f'Seu IMC é equivalente a {imc:.2f}.\nlogo você está: ')
#classificação do IMC 
if imc <= 18.5:
    print('abaixo do peso.')
elif imc > 18.5 and imc <= 24.9:
    print('no peso ideal.')
elif imc > 24.9 and imc <= 29.9:
    print('levemente acima do peso.')
elif imc > 29.9 and imc <= 34.9:
    print('com obesidade grau I.')
elif imc > 34.9 and imc <= 39.9:
    print('com obesidade grau II(severa).')
else:
    print('com obesidade de grau III(mórbita).')