# Snorkel

[**To do list**](https://github.com/zirondi/snorkel/blob/master/README.md#to-do-list)
[**Instalação**](https://github.com/zirondi/snorkel/blob/master/README.md#instalacao)

## To do list
- [x] ~~Documentação da instalação.~~
- [ ] Descobrir como fazer o jupyter funcionar direito por ssh.
- [ ] Intro Tutorial 1.
- [ ] Descobrir aonde o .db criado após o processamento do corpus é criado.


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

8. (Temporário) Use ```jupyter console``` para abrir o console, ```%load file_name.py``` para carregar um .py direto no console.

## Intro Tutorial 1
O tutorial é bem explicativo, porém no item 7, na linha ```from util import number_of_people``` este ```util``` é um util.py que fica em "/snorkel-master/tutorials/intro"
