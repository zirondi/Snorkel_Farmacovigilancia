# Snorkel

## Sumário

[**To do list**](https://github.com/zirondi/snorkel/blob/master/README.md#to-do-list)

[**Instalação**](https://github.com/zirondi/snorkel/blob/master/README.md#instalação)

[**Intro Tutorial 1**](https://github.com/zirondi/snorkel/blob/master/README.md#intro-tutorial-1)

[**Intro Tutorial 2**](https://github.com/zirondi/snorkel/blob/master/README.md#intro-tutorial-2)

## To do list
- [x] ~~Documentação da instalação.~~
- [x] Descobrir como fazer o jupyter funcionar direito por ssh.
- [x] ~~Intro Tutorial 1.~~
- [x] ~~Descobrir aonde o .db criado após o processamento do corpus é criado.~~
- [ ] Intro tutorial 2


## Instalação 
1. Baixar o [Anaconda](https://www.anaconda.com/distribution/)
    - O anaconda não possui um repositório para o apt-get, então o curl será necessário para baixar o .sh do site (```sudo apt-get update && sudo apt-get install curl```)(**sudo**).
  
2. cd para o folder onde o arquivo foi baixado.
    - ```sudo bash Anaconda3-201X.XX-Linux-x86_64.sh```

3. Caso o comando ```conda``` não seja adicionado ao PATH:
    - ```sudo nano .bashcr ```
      Adicionar "./home/*user*/anaconda3/etc/profile.d/conda.sh" ao fim do arquivo de texto. (**sudo**)
      
4. Baixar o .zip do [Snorkel](https://github.com/HazyResearch/snorkel) pelo curl
	- ```unzip \*.zip```

5. cd para "/snorkel-master"
	- ``` conda env -f environment.yml``` (Não precisa de sudo)

6. Ative o environment usando:```conda activate snorkel```

7. Instale o snorkel como dependência:``` pip install . ```

8. Instalar o treedlib e o numbskull```pip install treedlib && pip install numbskull``` (Dois módulos dado como missing no tutorial 2). 

## Acessar o Jupyter Notebook

| where  | using    | command                                          |
| ------ | -------- | ------------------------------------------------ |
| spica | terminal | `jupyter notebook --no-browser --port=8888`      |
| local  | terminal | `ssh -p 49186 -v -NL 8888:localhost:8888 lzirondi@spica.eic.cefet-rj.br` |
| local  | browser  | `localhost:8888`                                 |


## Intro Tutorial 1
O tutorial é bem explicativo, porém no item 7, na linha ```from util import number_of_people``` este ```util``` é um util.py que fica em "/snorkel-master/tutorials/intro".
Há um "utils.py" no root do snorkel, verificar.

O tutorial cria um snorkel.db no folder que o console for executado. (Por algum motivo tinha uma cópia de um .db antigo no ~/Documentos que eu não faço ideia de como foi parar lá.)

**Problemas do jupyter console ao usar um .py para carregar o código**
	A função %%time não funciona pois ela atua na célula toda, chamar ela no meio do código gera um erro

O snorkel.db é criado no folder que o console esta sendo usado. Não tenho como abrir ou investigar sem um sgbd.
(baixar o arquivo ```scp your_username@remotehost:foobar.txt /local/dir``` e dar uma olhada com o sqlite na minha máquina)

## Intro Tutorial 2

Uma lida rápida e nenhuma menção ao snorkel.db
Essa parte do tutorial monta um knowledge-database em cima de um arquivo no /data/ (cell 6)

"A labeling function is just a Python function that accepts a Candidate and returns 1 to mark the Candidate as true, -1 to mark the Candidate as false, and 0 to abstain from labeling the Candidate (note that the non-binary classification setting is covered in the advanced tutorials!)." Há uma table gold_label no snorkel.dp do intro 1, os valores variam entre -1 e 1. Não entendi como ela foi criada nesse tutorial 1, verificar se após o tutorial 2 algo muda. (cell 11 menciona isso, verificar.)

Na cell 3 ele pede um import que eventualmente pede um import do treedlib, o que não instalou automaticamente com o snorkel. Procurando sobre o erro ele é bem constante então adicionar o ```pip install treedlib``` ao tutorial de instalação.

Ao executar a cell 4 eu recebi outro erro de módulo inexistente, dessa vez com o numbskull. ```pip install numbskull```. Adicionado ao tutorial de instalação.

cell 20 ele cria um plot do matplotlib que não funciona via ssh no jupyter console (não vital por enquanto)

cell 26 me da um erro de index out of range. Não consigo continuar a partir daqui.

02/04














## rdstuff

print(session.__dict__) (me mostra aonde o .db esta localizado entre outras infos (sqlite etc etc)

dit(session) retorna atributos e outras infos do session

https://towardsdatascience.com/introducing-snorkel-27e4b0e6ecff

https://docs.sqlalchemy.org/en/13/orm/session_basics.html (ler melhor, explica sessions)


python use a cabeça 
sql select * from candidate where split=2 and type='husband'

in 1 -> inicializando a sessão e importando o necessário

in 2 -> define candidato e NOME da relação

in 3 -> ele usa gold labels criadas na ultima celula do tuto1, essas golds são criadas a partir do util.py. Nesse util.py existe o objeto load_external_labels onde é chamado na ultima celula do primeiro, entao o load_external_labels é um objeto generico para a criação dessas gold labels iniciais que procuram por candidato1 "relação"(Spouse = candidate_subclass('Spouse', ['person1', 'person2'])) candidato2


