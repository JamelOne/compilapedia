
def combine(lista):
    for i in range(len(lista)):
        j=i
        if(lista[i]=="NOME"):
            while(lista[j]==lista[j+1]):
                j+=1
            print(j)
        elif(lista[i]=="ADJETIVO"):
            while(lista[j]==lista[j+1]):
                j+=1
            print(j)    

lst=['NOME', 'NOME', 'NOME', 'VERBO', 'ARTIGO', 'ADJETIVO', 'SEPARADOR', 'ADJETIVO', 'ADJETIVO', 'SEPARADOR', 'ADJETIVO', 'ADJETIVO', 'FINAL']
combine(lst)