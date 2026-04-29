rend_trib = float(input('Informe o Salario Bruto Anual: '))
rend_isent = float(input('Informe os Gastos Isento Anual: '))
imp_retid = float(input('Informe o Quanto de Imposto foi Descontado Anual: '))

rend_trib = 0
imp_retid = 0

if rend_trib <= 33912:
    aliquota = 0
    deducao = 0
    imp_devido = (rend_trib * aliquota) - deducao

elif rend_trib <= 45012:
    aliquota = 0.075
    deducao = 2543.40
    imp_devido = (rend_trib * aliquota) - deducao

elif rend_trib <= 67008:
    aliquota = 0.15
    deducao = 5919.30
    imp_devido = (rend_trib * aliquota) - deducao

elif rend_trib <= 88848:
    aliquota = 0.225
    deducao = 10944.90
    imp_devido = (rend_trib * aliquota) - deducao

else:
    aliquota = 0.275
    deducao = 15387.30
    imp_devido = (rend_trib * aliquota) - deducao

diferenca = imp_devido - rend_trib

