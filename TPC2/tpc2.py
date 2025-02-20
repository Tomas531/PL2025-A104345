import re

def tpc2():
    with open('obras.csv', 'r', encoding='utf-8') as file:
        next(file)
        conteudo = file.read()
        conteudo = re.sub("\n         ", " ", conteudo)
        conteudo += "\n"

        padrao = r'([^;]+);([^\n]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)\n'
        campos = re.findall(padrao, conteudo) 

        compositores = set() # Set para o nome dos Compositores
        dis_obras = {} # Dicionário para as distribuições das obras pelos periudos
        periodo_obras = {} # Dicionário para guardar as obras de cada periudo

        for elementos in campos:
            if len(elementos) > 6:
                compositores.add(elementos[4]) 

                periodo = elementos[3] 
                obra = elementos[0]

                if periodo in dis_obras:
                    dis_obras[periodo] += 1
                    periodo_obras[periodo].append(obra)
                else:
                    dis_obras[periodo] = 1
                    periodo_obras[periodo] = [obra]
        compositores = sorted(compositores)
            
        print("Compositores Musicais (ordenados alfabeticamente):")
        for compositor in compositores:
            print(f"- {compositor}")
        
        print("\n\n")
        
        print("Distribuição das obras por período:")
        for periodo, quantidade in dis_obras.items():
            print(f"{periodo}: {quantidade} obras")

        print("\n\n")

        print("Obras por período:")
        for periodo, obras in periodo_obras.items(): 
            print(f"\n{periodo}:")
            for obra in obras:
                print(f"  - {obra}")

tpc2()