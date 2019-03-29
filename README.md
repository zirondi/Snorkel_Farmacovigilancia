# snorkel

## To do list.
- [ ] Documentação da instalação.
- [ ] Intro Tutorial 1.
- [ ] Marcar o que é sudo.
- [ ] Descobrir aonde o .db criado em cima do corpus é criado.


## Instalação 
1. Baixar o [Anaconda](https://www.anaconda.com/distribution/)
  - O anaconda não possui um repositório para o apt-get, então o curl será necessário para baixar o .sh do site (```sudo apt-get update && sudo apt-get install curl```).
  
2. cd para o folder onde o arquivo foi baixado.
  ```sudo bash Anaconda3-201X.XX-Linux-x86_64.sh```

3. Caso o comando ```conda``` não seja adicionado ao PATH:
  - ```sudo nano .bashcr ```
      Adicionar "./home/*user*/anaconda3/etc/profile.d/conda.sh" ao fim do arquivo de texto.
      
4. Baixar o .zip do [Snorkel](https://github.com/HazyResearch/snorkel) pelo curl
  -```unzip \*.zip```

5.
