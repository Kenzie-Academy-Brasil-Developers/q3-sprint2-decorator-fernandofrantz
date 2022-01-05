from flask import Flask

app = Flask(__name__)
if (__name__ == '__main__'):
    app.run()

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# Desenvolva suas rotas abaixo

#Rota de login
#Status Code: 200 - OK, 400 - Bad Request ou 401 - Unauthorized;

def verify_keys(trusted_keys: list[str]):
    return ''

@app.post('/login')
@verify_keys([])
def login():
    return ''