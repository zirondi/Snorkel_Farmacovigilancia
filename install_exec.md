
## Instalação 
1. Baixar o [Anaconda](https://www.anaconda.com/distribution/)
    - O anaconda não possui um repositório para o apt-get, então o curl será necessário para baixar o .sh do site (```sudo apt-get update && sudo apt-get install curl```)(**sudo**).
  
2. cd para o folder onde o arquivo foi baixado.
    - ```sudo bash Anaconda3-201X.XX-Linux-x86_64.sh```

3. Caso o comando ```conda``` não seja adicionado ao PATH:
    - ```sudo nano .bashcr ```
      Adicionar "./home/*user*/anaconda3/etc/profile.d/conda.sh" ou "export PATH=~/anaconda3/bin:$PATH
" ao fim do arquivo de texto. (**sudo**)
      
4. Baixar o .zip do [Snorkel](https://github.com/HazyResearch/snorkel) pelo curl
	- ```unzip \*.zip```

5. cd para "/snorkel-master"
	- ``` conda env -f environment.yml``` (Não precisa de sudo)

6. Ative o environment usando:```conda activate snorkel```

7. Instale o snorkel como dependência:``` pip install . ```

~~8. Instalar o treedlib e o numbskull```pip install treedlib && pip install numbskull``` (Dois módulos dado como missing no tutorial 2). ~~ (Resolvido na última atualização)

## Acessar o Jupyter Notebook

FAÇA ISSO NO HOME, por algum motivo o session do os não gosta quando ele não esta no home.

| where  | using    | command                                          |
| ------ | -------- | ------------------------------------------------ |
| spica | terminal | `jupyter notebook --no-browser --port=8888`      |
| local  | terminal | `ssh -p 49186 -v -NL 8888:localhost:8888 lzirondi@spica.eic.cefet-rj.br` |
| local  | browser  | `localhost:8888`                                 |


