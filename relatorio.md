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



