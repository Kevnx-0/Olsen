texto = int(input("Texto:"))
resultado = ''

arquivo = open('/home/kvzzz/Kvz/Arquivos_Txts/Decifre.txt','w+')

for linha in arquivo:
    pass

for i in len(texto):
    if "A" <= i <= 'Z':
        resultado += chr((ord(i) - 65 + 25 ) % 26 + 65)
    elif 'a' <= i <= 'z':
        resultado += chr((ord(i) - 97 + 25) % 26 + 97)
    else:
        resultado += i


print(f'Criptografado: {resultado}\n')



