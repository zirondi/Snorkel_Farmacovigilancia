# Semana ??/??/??
-Resolvi os problemas do banco de dados (documentado)
  ## Novos problemas
  * Bug da variavel do nome do banco nao atualizando.Ao definir o nome do banco em `os.environ['SNORKELDB'] = 'postgres:///NOMEDOBANCO'` pela primeira vez, essa var não será atualizada até reiniciar o kernel.
    
  * Erro estranho do snorkel nao terminando de executar no tuto 1, o CorpusParser fica executando ad infinitum.

# Semana 12/09/2019

  * Erro estranho do snorkel nao terminando de executar no tuto 1, o CorpusParser fica executando ad infinitum.
  
  **Att**: O snorkel termina o processamento das sentenças e escreve no banco, mas por algum motivo nao finaliza a execução.
      **Resolução temp**-> esperar o 100%, reiniciar o kernel, re-executar as 2 ultimas cells, continuar a execução pulando a cell do parser
