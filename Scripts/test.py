def dicio():
    
    f = open('/home/lzirondi/Github/snorkel/Scripts/LIWC2015_pt.dic', 'r')
    s = f.readlines()
    f.close()

    causes = set()
    verbs = set()
    causes_and_verbs = set()


    for i in range(0, len(s)):
        aux = False
        if('20' in s[i]):
            verbs.add(s[i])
            if('52' in s[i]):
                causes.add(s[i])
                causes_and_verbs.add(s[i])
                aux = True

        if(aux):
            causes.add(s[i])

    nomes = {'Causas':causes, 'Verbos':verbs, 'Causas & Verbos':causes_and_verbs}
    for name in nomes:
        f = open('/home/lzirondi/Github/snorkel/Scripts/Dicts/' + name, 'w')
        for line in nomes.get(name):
            
            aux2 = line.split('\t')[0]            
            f.write(aux2 + '\n')


dicio()
        
            



    