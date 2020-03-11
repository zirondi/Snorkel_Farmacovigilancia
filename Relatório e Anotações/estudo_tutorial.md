## Intro Tutorial 1
O tutorial é bem explicativo, porém no item 7, na linha ```from util import number_of_people``` este ```util``` é um util.py que fica em "/snorkel-master/tutorials/intro".
Há um "utils.py" no root do snorkel, verificar.

O tutorial cria um snorkel.db no folder que o console for executado. (Por algum motivo tinha uma cópia de um .db antigo no ~/Documentos que eu não faço ideia de como foi parar lá.)

**Problemas do jupyter console ao usar um .py para carregar o código**
	A função %%time não funciona pois ela atua na célula toda, chamar ela no meio do código gera um erro

O snorkel.db é criado no folder que o console esta sendo usado. Não tenho como abrir ou investigar sem um sgbd.
(baixar o arquivo ```scp your_username@remotehost:foobar.txt /local/dir``` e dar uma olhada com o sqlite na minha máquina)

scp -P #### name@server:/home/foo.db ~/Desktop/


## Intro Tutorial 2

Uma lida rápida e nenhuma menção ao snorkel.db
Essa parte do tutorial monta um knowledge-database em cima de um arquivo no /data/ (cell 6)

"A labeling function is just a Python function that accepts a Candidate and returns 1 to mark the Candidate as true, -1 to mark the Candidate as false, and 0 to abstain from labeling the Candidate (note that the non-binary classification setting is covered in the advanced tutorials!)." Há uma table gold_label no snorkel.dp do intro 1, os valores variam entre -1 e 1. Não entendi como ela foi criada nesse tutorial 1, verificar se após o tutorial 2 algo muda. (cell 11 menciona isso, verificar.)

~Na cell 3 ele pede um import que eventualmente pede um import do treedlib, o que não instalou automaticamente com o snorkel. Procurando sobre o erro ele é bem constante então adicionar o ```pip install treedlib``` ao tutorial de instalação.~

~Ao executar a cell 4 eu recebi outro erro de módulo inexistente, dessa vez com o numbskull. ```pip install numbskull```. Adicionado ao tutorial de instalação.~

~cell 20 ele cria um plot do matplotlib que não funciona via ssh no jupyter console (não vital por enquanto)~

~cell 26 me da um erro de index out of range. Não consigo continuar a partir daqui.~
