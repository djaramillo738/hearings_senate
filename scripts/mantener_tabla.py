def mantener_tabla(texto):
    temp = texto
    out=""
    finished = False
    while not finished:
        definidor=temp.find('.....')
        if definidor!=-1:
            out += temp[:temp.find('.....')+1]
            temp = temp[temp.find('.....')+1:]
        else:
            finished = True
    return out