def hay_statement_of(texto):
    out=False
    puntos=texto.find('STATEMENT OF')
    if puntos != -1:
        out=True
    return out