# Desafio Backend
Repositório para o desafio backend

# Setup do Projeto
Após clonar e acessar a pasta raiz do repositório, crie o ambiente virtual usando o pipenv:
```
pipenv --python 3
```
Após isso, instale as dependências necessárias ao projeto:
```
pipenv install
```
Aplique as migrações:
```
pipenv run ./manage.py migrate
```
Se tudo tiver sido configurado com sucesso, executar a aplicação:
```
pipenv run ./manage.py runserver
```
E acessar o servidor local em `http://localhost/8000`.
