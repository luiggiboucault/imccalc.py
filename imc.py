altura = float(input('Coloque sua altura em cm: '))
peso = float(input('Coloque seu peso em kg: '))

IMC = peso / (altura ** 2)
print('IMC: {:.1f} ' .format(IMC))
# :.1f formatacao pra 1 casa decimal 

if IMC < 18.5:
    print('Seu IMC e considerado Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print('Seu IMC  e considerado Normal')

elif IMC >= 25 and IMC < 29.9:
    print('Seu IMC  e considerado Sobrepeso')

elif IMC >= 30 and IMC < 39.9:
    print('Seu IMC  e considerado Obesidade')

elif IMC >= 40:
    print('Seu IMC e considerado Obesidade Morbida, cuidado!')



