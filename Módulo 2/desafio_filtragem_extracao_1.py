def extrair_anos(datas):
    lista_datas = datas.split(", ")
    anos = [ano[:4] for ano in lista_datas]
    return ", ".join(anos)

entrada = input()
saida = extrair_anos(entrada)
print(saida)