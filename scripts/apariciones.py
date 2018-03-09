def apariciones(texto):
    text=texto.read()
    return (re.findall('\nWITNESSES\n' | '\nWITNESS\n' | '\nSTATEMENT OF', text))

def decidir(texto):
    text=texto.read()
    out=False
    if len(re.findall('Statement of [W|w]itnesses' | 'WITNESSES', text))>0:
        out=True
    return(out)