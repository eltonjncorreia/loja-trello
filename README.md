# loja-trello
A API a ser desenvolvida será de uma loja virtual de computadores

## Link do heroku

``` https://loja-pc.herokuapp.com/ ```


### Descrição do projeto


### Como rodar o projeto

``` git clone https://github.com/eltonjncorreia/loja-trello.git loja-trello ```

``` cd loja-trello ```

``` python -m venv .venv ```

``` source .venv/bin/activate ```

``` pip install -r requirements.txt ```


### Configure as instâncias

``` cp contrib/env-sample .env ```

``` python manage.py test ```

### Crie um super usuario para ter acesso a API

``` python manage.py migrate ```

``` python manage.py createsuperuser ```

``` python manage.py runserver```


```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configuraçoes para o heroku
3. Define uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

``` console
heroku apps:create minhainstancia
heroku config:push
heroku config:set SECRET_KEY
heroku config:set DEBUG=False

git push heroku master --force
```
