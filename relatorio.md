# Semana ??/??/??
-Resolvi os problemas do banco de dados (documentado)
  ## Novos problemas
  * Bug da variavel do nome do banco nao atualizando.Ao definir o nome do banco em `os.environ['SNORKELDB'] = 'postgres:///NOMEDOBANCO'` pela primeira vez, essa var não será atualizada até reiniciar o kernel.
    
  * Erro estranho do snorkel nao terminando de executar no tuto 1, o CorpusParser fica executando ad infinitum.

# Semana 12/09/2019

  ### Erro estranho do snorkel nao terminando de executar no tuto 1, o CorpusParser fica executando ad infinitum.
  
  **Att**: O snorkel termina o processamento das sentenças e escreve no banco, mas por algum motivo nao finaliza a execução.
      
   **Resolução temp**-> esperar o 100%, reiniciar o kernel, re-executar as 2 ultimas cells, continuar a execução pulando a cell do parser
   
_______________________________________________________________________________________________________________________________

- Descobri que a Spica só tem 4 threads.

# Semana 10/10/2019

  (Re)comecei a criar um All in one para poder criar o fluxograma.
  Recomecei pois a primeira vez que eu fiz foi complicada de fazer debug. Estou agora copiando as células de uma maneira que elas ainda fiquem separadas por contexto.
  Farei o fluxograma no powerpoint ou no http://dia-installer.de/
  
  Coisas estranhas a se notar:
    Parece que o número de artigos no corpus (2591) é pequeno para justificar o uso do paralelismo do psql.
    
| SGBD          | Threads | Tempo |
|:--------------|:--------|:------|
| PSQL          | 1       | 9m 20s|
| PSQL          | 4       | 8m 56s|
| PSQL          | 16      | 6m 52s (Snorkel) / 9m 22s (lzirondi) |
| SQLite        | 1?      | 4m 45s |



>Erro estranho do snorkel nao terminando de executar no tuto 1, o CorpusParser fica executando ad infinitum.

Resolvi isso executando algum comando após o comando do parser (```print()```) 

>Descobri que a Spica só tem 4 threads.

Errado também, 4 por núcleo, 16 no total. A dúvida reside se a var do parser (parallelism=int) é relacionada a threads (Imagino que sim).

Para limpar o db usar:
```
drop table candidate cascade; 
drop table context cascade; 
drop table document cascade; 
drop table feature cascade; 
drop table feature_key cascade; 
drop table gold_label cascade; 
drop table gold_label_key cascade; 
drop table label cascade; 
drop table label_key cascade; 
drop table marginal cascade; 
drop table prediction cascade; 
drop table prediction_key cascade; 
drop table sentence cascade; 
drop table span cascade; 
drop table spouse cascade; 
drop table stable_label cascade;
```


# Semana 07/11/2019

Terminei o All in one; Terminei o Fluxograma.

## Datasets necessários:
    1. O corpus
    2. O dicionrário de sintomas
    3. O dicionário de remédios
    4. As relações explicitadas
    5. As gold_labels
    
   


Entender e documentar como a classe DictionaryMatch funciona!

matchers.html#DictionaryMatch

# Férias e semana 02/03/2020


Vamo lá que faz um tempo:

Nas férias eu me preocupei em preparar os datasets do Alexandre para a execução do snorkel.

A preparação dos Corpus foi a mais fácil, usei o arquivo "Tweets Anotados.txt", processei ele e exportei para um .tsv.

Agora para definir nossos matchers a situação foi um pouco mais complicada:

Primeiro defininos o uso do DictionaryMatcher do Snorkel como o método que vamos usar.

Para isso precisamos também definir uma relação entre os matchers, no momento definimos a relação substância->causa.

Pra cada matcher da relação é necessário definir um dicionário (conjunto de palavras NÃO estrutura de dados do python, a estrutura em si é uma lista).

O dicionário de substâncias veio dos arquivos 'Remédios-br-gazette.txt', 'Substâncias-br-gazette.txt', 'Remédios2-br-gazette.txt', 'Substâncias2-br-gazette.txt'. Tratei esses txts, agrupei todos, ordenei e salvei como outro txt.

O dicionário de eventos veio dos arquivos 'Eventos.txt', 'EventosAdversos-gazette.txt'. Tratei esses txts, agrupei todos, ordenei e salvei como outro txt.

Com isso eu já consegui extrair os candidatos.

Problema 1 -> Os dicionários estão meio poluidos, palavras com "e", "um", "anti" (?) e "sene" (?) foram marcadas como substâncias. Preciso limpar os dicionarios.

Problema 2 -> Como os matcher me permitem ignorar caixa alta, eu não precisei normalizar texto algum. (Pra facilitar a minha vida no futuro, eu quis extrair esses candidatos para um TSV, o fato de eu ter chars com acento acabou com a formatação toda.). Preciso normalizar TODAS as linhas agora. (usar unidecode.unidecode(str))

Futuro -> Normalizar o texto, discutir sobre as golden_labels, estrutura dos candidatos para as Labeling Functions e inverter a relação.
