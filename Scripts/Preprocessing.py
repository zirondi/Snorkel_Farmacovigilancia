#os: getFiles, toEventsDicio
import os
#shutil: getFiles
from shutil import copy
#nltk.corpus: toSubsDicio, toEventosDicio
from nltk.corpus import stopwords

class Util:
    

    def __init__(self, inPath, outPath, command):

        
        self.inPath = inPath
        self.outCopyPath = outPath + '/toBeProcessed'
        self.outPath = outPath + '/Processed'

        if(command == True):
            #Ordem dos nomes importa aqui.
            self.whiteList = ['Eventos.txt', 'EventosAdversos-gazette.txt', 'Remédios-br-gazette.txt', 'Substâncias-br-gazette.txt', 'Tweets Anotados.txt', 'Remédios2-br-gazette.txt', 'Substâncias2-br-gazette.txt']
            self.getFiles()
            self.toTSV()
            self.toSubsDicio()
            self.toEventosDicio()


    #Copiando os arquivos que estão na whitelist, de inPath para outPath
    def getFiles(self):
        #r=root, d=directory, f=file

        if not os.path.exists(self.outCopyPath):
            os.mkdir(self.outCopyPath)
        
        if not os.path.exists(self.outPath):
            os.mkdir(self.outPath)
        
        for r, d, f in os.walk(self.inPath, topdown=True):
            for files in f:
                if files in self.whiteList:
                    copy(os.path.join(r, files), self.outCopyPath)
                    print('Arquivo %s copiado com sucesso.' % files)


    #Criando o TSV do Tweets Anotados.txt
    def toTSV(self):
        txt = open(self.outCopyPath + '/' + self.whiteList[4], 'r', encoding='UTF-8')
        tsv = open(self.outPath + '/' + self.whiteList[4].replace('txt', 'tsv'), 'w', encoding='UTF-8')
        
        tsv.write("Índice" + '\t' + "Tweet" + '\n')
        i = 0

        for line in txt:
            
            tsv.write(str(i) + '\t' + line.lower().replace('\n', '').replace(' ', '', 1) + '\n')
            i += 1

        tsv.close()
        txt.close()
        print('Tsv do Corpus criado com sucesso.')

    #Gerando o .txt do dicionário de substâncias
    def toSubsDicio(self):
        
        diciosSubstancia = [self.whiteList[2], self.whiteList[3], self.whiteList[5], self.whiteList[6]]
        limiteDicios = {self.whiteList[2]:6701, self.whiteList[3]:1778, self.whiteList[5]:5904, self.whiteList[6]:815}

        finalSet = set()

        for d in diciosSubstancia:
            if(d==self.whiteList[5]):
                f = open(self.outCopyPath + '/' + d, 'r', encoding='UTF-16le')
            else:
                f = open(self.outCopyPath + '/' + d, 'r', encoding='UTF-8')
            s = f.read()
            f.close()

            s = s.replace('DRUG\t', '')
            s = s.replace('\t', ' ')
            s = s.splitlines()            

            for i in range(0, limiteDicios[d]):
                finalSet.add(s[i].lower())
            
        stop_words = set(stopwords.words("portuguese"))
        finalSet.difference_update(stop_words)    
        finalList = sorted(finalSet)

        txt = open(self.outPath + '/Dicionario_de_Substancias.txt', 'w', encoding='UTF-8')

        for line in finalList[:-1]:
            txt.write(line + '\n')     
        txt.close()
        print('Dicionário de Substâncias gerado com sucesso.')

    #Gerando o .txt do dicionário de substâncias
    def toEventosDicio(self):        

        finalSet = set()        

        f = open(self.outCopyPath + '/' + self.whiteList[0], 'r', encoding='UTF-8')
        s = f.read()
        f.close()
        
        s = s.splitlines()

        for line in s:
            finalSet.add(line.lower())

        
        f = open(self.outCopyPath + '/' + self.whiteList[1], 'r', encoding='UTF-8')
        s = f.read()
        f.close()

        s = s.replace('Event	', '')
        s = s.splitlines()

        for i in range (0, 11561):
            finalSet.add(s[i].lower())

        finalSet.add('sono')

        stop_words = set(stopwords.words("portuguese"))
        finalSet.difference_update(stop_words) 
        finalList = sorted(finalSet)

        txt = open(self.outPath + '/Dicionario_de_Eventos.txt', 'w', encoding='UTF-8')
        
        for line in finalList:
            txt.write(line + '\n')
        txt.close()
        print('Dicionário de Eventos gerado com sucesso.')


    #Retornando os dicionarios como Lista
    def subsToList(self):

        f = open(self.outPath + '/Dicionario_de_Substancias.txt', 'r', encoding='UTF-8')
        s = f.read()
        f.close()
        s = s.splitlines()

        return s

    def eventosToList(self):
        f = open(self.outPath + '/Dicionario_de_Eventos.txt', 'r', encoding='UTF-8')
        s = f.read()
        f.close()
        s = s.splitlines()

        return s
    

    #Retornando o caminho do Corpus
    def getTsvPath(self):
        return self.outPath + '/' + self.whiteList[4].replace('txt', 'tsv')