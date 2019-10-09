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


OperationalError: (psycopg2.OperationalError) could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

(Background on this error at: http://sqlalche.me/e/e3q8)

ln -s /var/run/postgresql/.s.PGSQL.5432 /tmp/.s.PGSQL.5432

erro para reportar -> no advanced/parallel processing a var n_docs nao eh declarada



SÓ TEM 4 THREADS NA MAQUINA



Run jupyter kernelspec list to get the paths of all your kernels.
Then simply uninstall your unwanted-kernel

jupyter kernelspec uninstall unwanted-kernel


source activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
