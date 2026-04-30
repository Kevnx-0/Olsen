renda = float(input('Informe o Salario Bruto Anual: ')) 
retido = float(input('Informe o Quanto de Imposto foi Descontado Anual: '))

renda = 0
isento = 0



if renda <= 29145.60:
    aliquota = 0.0
    deducao = 0.0
    devido = (renda * aliquota) - deducao

elif renda <= 33919.80:
    aliquota = 0.075
    deducao = 2185.92
    devido = (renda * aliquota) - deducao

elif renda <= 45012.60:
    aliquota = 0.15
    deducao = 4729.91
    devido = (renda * aliquota) - deducao

elif renda <= 55976.16:
    aliquota = 0.225
    deducao = 8105.85
    devido = (renda * aliquota) - deducao

else:
    aliquota = 0.275
    deducao = 10904.85
    devido = (renda * aliquota) - deducao

diferenca = retido - devido



print(devido)
print(diferenca)




 ##       if diferenca < 0:
    ##        restituicao = -diferenca
    ##        print(restituicao)

    ##    elif diferenca > 0:
    ##        print(f'Voce tem que pagar {diferenca}')    

   ##     else:
  ##          print('inexistente')        
 ##
