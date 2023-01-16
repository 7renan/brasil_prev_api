## Brasil Prev API

### instruções
 - criar arquivo '.env' de acordo com o arquivo '.env.example'

### iniciando o projeto

```shell
# criando máquina virtual
python -m venv .venv
# ativando máquina virtual
.venv\Scripts\activate
# instalando as dependências do projeto
pip install -r requirements.txt
# executando projeto
python manage.py runserver

```

### migrações

```shell
# preparar migrações
python manage.py makemigrations
# executando as migrações
python manage.py migrate
```

### executando testes

```shell
python manage.py test
```

### rotas

```shell
# root API
localhost:8000/api/v1/
# documentação da API
localhost:8000/api/v1/docs
```

### iniciando o projeto com docker

```shell
docker-compose up --build -d
```


