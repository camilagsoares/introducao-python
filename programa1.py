Largura_Garagem = float (input("Entre com a largura da garagem em metros:"))
Profundidade_Garagem = float (input("Entre com a profundidade da garagem em metros:"))

#abaixo,calculo da area da garagem

Area_Garagem = Largura_Garagem * Profundidade_Garagem

Largura_Terreno = float(input("Entre com a largura do terreno em metros: "))
Profundidade_Terreno = float(input("Entre com a profundidade do terreno em metros: "))


# Abaixo, cálculo da área do terreno
Area_Terreno = Largura_Terreno * Profundidade_Terreno
# Agora, cálculo do percentual de ocupação

Percentual = ((Area_Garagem)/(Area_Terreno))* 100
print("Percentual de ocupação:",Percentual)