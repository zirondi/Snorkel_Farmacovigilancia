#to do: outpath - copy path, novo folder do ja processado, limpar sujeira, revisar os dois dicionarios

#os: getFiles, toEventsDicio
import os
#shutil: getFiles
from shutil import copy


#Paths dos folders
inPath = '/home/lzirondi/datasets/AlexandreMartins/'
outCopyPath = '/home/lzirondi/datasets/toBeProcessed'
outPath = '/home/lzirondi/datasets/Processed'
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
    
    i = 0

    for line in txt:
        
        tsv.write(str(i) + '\t' + line.lower())
        i += 1

    tsv.close()
    txt.close()

#Revisar e comentar, ta funcionando porem esta feio
def toEventosDicio():
    
    txt = open(outPath + '/Dicionario_de_Eventos.txt', 'w', encoding='UTF-8')

    f = open(outCopyPath + '/' + whiteList[0], 'r', encoding='UTF-8')

    s = f.read()
    f.close()
    s = s.splitlines()

    for i in range(0, len(s) - 1):
        txt.write(s[i].lower() + '\n')

    
    f = open(outCopyPath + '/' + whiteList[1], 'r', encoding='UTF-8')

    s = f.read()
    f.close()
    s = s.replace('Event	', '')
    s = s.splitlines()

    for i in range (0, 11561):
         txt.write(s[i].lower() + '\n')

    txt.write('sono\n')
    txt.close()

    os.system('sort /home/lzirondi/datasets/Processed/Dicionario_de_Eventos.txt -o /home/lzirondi/datasets/Processed/Dicionario_de_Eventos.txt')

def toSubsDicio():
    
    fontes = [whiteList[2], whiteList[3], whiteList[5], whiteList[6]]
    bagunça = {whiteList[2]:6701, whiteList[3]:1778, whiteList[5]:5904, whiteList[6]:815}

    txt = open(outPath + '/' + '/Dicionario_de_Substancias.txt', 'w', encoding='UTF-8')

    for d in fontes:
        if(d==whiteList[5]):
            f = open(outCopyPath + '/' + d, 'r', encoding='UTF-16le')
        else:
            f = open(outCopyPath + '/' + d, 'r', encoding='UTF-8')
        
        s = f.read()
        f.close()

        s = s.replace('DRUG\t', '')
        s = s.splitlines()

        for i in range(0, bagunça.get(d) - 1 ):
            pass
            #txt.write(unidecode.unidecode(s[i].lower()) + '\n')
        
    txt.close()

    os.system('sort /home/lzirondi/datasets/Processed/Dicionario_de_Substancias.txt -o /home/lzirondi/datasets/Processed/Dicionario_de_Substancias.txt')

def subsToList():

    f = open(outPath + '/Dicionario_de_Substancias.txt', 'r', encoding='UTF-8')
    s = f.read()
    f.close()
    s = s.splitlines()

    return s

def eventosToList():
    f = open(outPath + '/Dicionario_de_Eventos.txt', 'r', encoding='UTF-8')
    s = f.read()
    f.close()
    s = s.splitlines()

    return s


def test():
    pass








getFiles()
toTSV()
toEventosDicio()
toSubsDicio()
#test()






