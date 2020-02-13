# Desafio Backend
Repositório para o desafio backend

# Setup do Projeto
1 - Após clonar e acessar a pasta raiz do repositório, crie o ambiente virtual:
```
pipenv --python 3
```
2 - Instale as dependências necessárias ao projeto:
```
pipenv install
```
3 - Aplique as migrações:
```
pipenv run ./manage.py migrate
```

4 - Crie um usuário administrador:
```
pipenv run ./manage.py createsuperuser
```

Se tudo tiver sido configurado com sucesso, execute a aplicação:
```
pipenv run ./manage.py runserver
```
E acesse o servidor local em [`http://localhost/8000`](http://localhost/8000) utilizando qualquer navergador web.
