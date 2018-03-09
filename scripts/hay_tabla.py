def hay_tabla(texto):
    out=False
    puntos=texto.find('.....')
    if puntos != -1:
        bloque="".join(texto[:puntos].split(' '))
        if bloque.find('CONTENTS')!=-1:
            out=True
    return out
        