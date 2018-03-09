def quitar_tabla(texto):
    temp = texto
    finished = False
    while not finished:
        if temp.find('.....')!=-1:
            temp = temp[temp.find('.....')+6:]
        else:
            finished = True
    return temp