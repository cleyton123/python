def traco():
    a = 'BEM VINDO AO CONVERSOR DE MOEDAS'
    x = len(a) * '-'  # Cria uma linha de traços com base no comprimento da string 'a'
    print(x, '\n', a, '\n', x)

traco()  # Chama a função traco para imprimir a mensagem com traços

while True:

#menu de opções
 opçoês=input(('Digite as opções para conversão: \n1.Real(BR) para Dólar(USA)\n2.Dólar(USA) para Real(BR)\n3.sair'))

 if opçoês == '1':
   #taxa de câmbio brasileira
   taxacambioBR = 5.0807  
   valorBRA = float(input('Digite o valor em Real Brasileiro (BRL): '))
   #conversão USA
   valorUSA = valorBRA / taxacambioBR
   print('O valor em Dólar dos Estados Unidos (USD) é:', valorUSA)



 elif opçoês == '2':
   #taxa de câmbio USA
   taxacambioUSD = 5.0807  # Exemplo de uma taxa de câmbio (1 USD para BRL)
   valorUSA = float(input('Digite o valor em Dólar dos Estados Unidos (USD): '))
   #conversão BR
   valorBRA = valorUSA * taxacambioUSD
   print('O valor em Real Brasileiro (BRL) é:', valorBRA)


 elif opçoês == '3':
     print('OBRIGADO!') 
     break #sair do loop while(enquanto)
 
 
 else:
    print('ERRO.DIGITE AS OPÇÕES [1],[2] OU [3].')