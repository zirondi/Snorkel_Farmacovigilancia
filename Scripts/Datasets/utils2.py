#os: getFiles, toEventsDicio
import os
#shutil: getFiles
from shutil import copy

#Paths dos folders
inPath = '/home/lzirondi/Github/AlexandreMartins'
outCopyPath = '/home/lzirondi/Github/snorkel/Scripts/Datasets/toBeProcessed'
outPath = '/home/lzirondi/Github/snorkel/Scripts/Datasets/Processed'
#Ordem dos nomes importa aqui.
whiteList = ['Eventos.txt', 'EventosAdversos-gazette.txt', 'Remédios-br-gazette.txt', 'Substâncias-br-gazette.txt', 'Tweets Anotados.txt', 'Remédios2-br-gazette.txt', 'Substâncias2-br-gazette.txt']


#Copiando os arquivos que estão na whitelist, de inPath para outPath
#DONE
def getFiles():
    #r=root, d=directory, f=file

    if not os.path.exists(outCopyPath):
        os.mkdir(outCopyPath)
    
    if not os.path.exists(outPath):
        os.mkdir(outPath)
    
    for r, d, f in os.walk(inPath, topdown=True):
        for files in f:
            if files in whiteList:
                copy(os.path.join(r, files), outCopyPath)
                print('Arquivo %s copiado com sucesso.' % files)


#Criando o TSV do Tweets Anotados.txt
#DONE
def toTSV():
    txt = open(outCopyPath + '/' + whiteList[4], 'r', encoding='UTF-8')
    tsv = open(outPath + '/' + whiteList[4].replace('txt', 'tsv'), 'w', encoding='UTF-8')
    
    tsv.write("Índice" + '\t' + "Tweet" + '\n')
    i = 0

    for line in txt:
        
        tsv.write(str(i) + '\t' + line.lower().replace('\n', '').replace(' ', '', 1) + '\n')
        i += 1

    tsv.close()
    txt.close()



def toSubsDicio():
    
    diciosSubstancia = [whiteList[2], whiteList[3], whiteList[5], whiteList[6]]
    limiteDicios = {whiteList[2]:6701, whiteList[3]:1778, whiteList[5]:5904, whiteList[6]:815}

    txt = open(outPath + '/' + '/Dicionario_de_Substancias.txt', 'w', encoding='UTF-8')

    finalSet = set()

    for d in diciosSubstancia:
        if(d==whiteList[5]):
            f = open(outCopyPath + '/' + d, 'r', encoding='UTF-16le')
        else:
            f = open(outCopyPath + '/' + d, 'r', encoding='UTF-8')
        
        s = f.read()
        f.close()

        s = s.replace('DRUG\t', '')
        s = s.replace('\t', ' ')
        s = s.splitlines()
        

        for i in range(0, limiteDicios[d]):
            finalSet.add(s[i].lower())
        
    finalList = sorted(finalSet)

    #print(finalList)
    for line in finalList[:-1]:
        txt.write(line + '\n')

        
    txt.close()



def doIt():
    pass

getFiles()
toSubsDicio()

