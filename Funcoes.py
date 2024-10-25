def calcular_inss(salario_bruto):
 
    if salario_bruto <= 1412:
        inss = salario_bruto*0.075
    elif salario_bruto > 1412 and salario_bruto <= 2666.68:
        inss = salario_bruto*0.09
        inss = inss - 21.18
    elif salario_bruto > 2666.68 and salario_bruto <= 4000.03:
        inss = salario_bruto*0.12
        inss = inss - 101.18
    else:
        inss = salario_bruto*0.14
        inss = inss - 181.18

    return round (inss,2)

def calcular_ir(salario_bruto):

    inss = calcular_inss(salario_bruto)

    salario_descontado = salario_bruto - inss

    if salario_descontado <= 2259.20:
        ir = 0
    elif salario_descontado > 2259.20 and salario_descontado <= 2826.65:
        ir = salario_descontado*0.075 - 169.44
    elif salario_descontado > 2826.65 and salario_descontado <= 3751.05:
        ir = salario_descontado*0.15 - 381.44
    elif salario_descontado > 3751.05 and salario_descontado <= 4664.68:
        ir = salario_descontado*0.225 - 662.77
    else:
       ir = salario_descontado*0.275 - 896.00

    return round (ir,2)



def utilizacaoContrato(valorContrato, valorRetencao, valorMedicao):

    saldoContrato = valorContrato - valorRetencao

    saldoResidual = saldoContrato - valorMedicao

    usoPercentual = (valorRetencao + valorMedicao) / valorContrato*100


    if usoPercentual >= 95:
        print('Solicitar Encerramento do Contrato, 95% utilizado')
    elif usoPercentual < 90 and usoPercentual > 5:
        print('Contrato em Andamento, uso entre 5% e 90%')
    else:
        print('Solicitar Status do Contrato, menos de 90% utilizado')

    return usoPercentual, saldoResidual
