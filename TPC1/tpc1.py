
def soma(texto):
    i = 0
    activo = True
    soma = 0
    number = ""
    while len(texto) > i:

        if texto[i] =="o" or texto[i] == "O":
            i +=1
            if texto[i] == "f" or texto[i] == "F":
                i+=1
                if texto[i] == "f" or texto[i] == "F":
                    i += 1
                    activo = False
            elif texto[i] == "n" or texto[i] == "N":
                    i += 1
                    activo = True
        elif activo:
            while texto[i].isdigit():
                  number += texto[i]
                  i +=1
            if number:
                soma += int(number)
                number = ""
        if texto[i] == "=":
             i += 1
             print(soma)
        else:
             i += 1

texto = "AJBHDAY=GH!674hnghbYH=GSVFS1hb4h67njk=Offczhbch16666=cjdsnjhcbs12bjbonhjbshb=2000000000000="

soma(texto)