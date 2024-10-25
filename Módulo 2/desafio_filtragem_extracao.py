def filtrar_visuais(lista_visuais):
    visuais = lista_visuais.split(", ")
    lista_capitalizada = [item.title() for item in visuais]
    lista_capitalizada  = sorted(set(lista_capitalizada))

    return ", ".join(lista_capitalizada)

entrada_usuario = input()

saida = filtrar_visuais(entrada_usuario)
print(saida)