def polozhit_chisla(elements):
    spisok = []
    for polozh in elements:
        if int(polozh) > 0:
            spisok.append(polozh)
    return spisok


kolvo_chisel = input('')
elements = kolvo_chisel.split(' ')

print(polozhit_chisla(elements))