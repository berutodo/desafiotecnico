import json
with open('dados.json', 'r') as file:
    mesAgosto = json.load(file)

def menorFaturamento(mes):
    menorValor = min(dia["valor"] for dia in mes)
    return menorValor
def maiorFaturamento(mes):
    maiorValor = max(dia["valor"] for dia in mes)
    return maiorValor
def diasFaturamentoMaiorMedia(mes):
    mesIgnorandoZeros = [dado for dado in mes if dado["valor"] != 0]
    media = sum(dia["valor"] for dia in mesIgnorandoZeros) / len(mesIgnorandoZeros)
    dias = []
    for index, dado in enumerate(mes):
        if dado["valor"] > media:
            dias.append(index)
            ### Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
            #Pede o numero de dias, que no caso foram 10, mas caso queira saber os dias esse codigo retorna um array seria só trocar index + 1 se quiser dias certos já que não existe dia 0
    return len(dias) 

print(menorFaturamento(mesAgosto))
print(maiorFaturamento(mesAgosto))
print(diasFaturamentoMaiorMedia(mesAgosto))
