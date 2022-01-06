from flask import Flask

from decorators import verify_keys, verify_credentials

app = Flask(__name__)
if (__name__ == '__main__'):
    app.run()

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# Desenvolva suas rotas abaixo

#Rota de login
#Status Code: 200 - OK, 400 - Bad Request ou 401 - Unauthorized;


@app.post('/login')
@verify_credentials
@verify_keys(['username','password'])
def login():
    return ''