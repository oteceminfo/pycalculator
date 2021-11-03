#variavel printada
calc = print("""
[+] - adição
{-] - subtração
[x] - multiplicação
[:] - divisão
""")

#varavel para inserção da opção
opcao = input('===> Insira a opção: ')

n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))

if opcao == '+':
  soma = n1 + n2
  print('Resultado: ', soma)
elif opcao == '-':
  soma2 = n1 - m2
  print('Resultado: ', soma2)
elif opcao == 'x':
  soma3 = n1 * n2
  print('Resultado: ', soma3)
elif opcao == ':':
  soma4 = n1 / n2
  peint('Resultado: ', soam4)
else:
  print('Opção invalida. Tente novamnete!')
