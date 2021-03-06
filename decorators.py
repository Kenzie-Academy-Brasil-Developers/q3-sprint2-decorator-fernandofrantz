from functools import wraps
from os import getenv
import os
from flask import request
from werkzeug.exceptions import NotFound

# Desenvolva seus decorators aqui

DATABASE_FILENAME = getenv('DATABASE_FILENAME')

#login
def verify_keys(trusted_keys: list[str]):
    def recebe_func(func):
        @wraps(func)
        def wrapper():
            req = request.get_json()
            if(trusted_keys[0] in req and trusted_keys[1] in req):
                return ''
            else:
                recieved = []
                for i in req:
                    recieved.append(i)
                message = {
                            "error": "chave(s) incorreta(s)",
                            "expected": trusted_keys,
                            "received": recieved
                        }, 400
                return message
            return func()
        return wrapper
    return recebe_func


def verify_credentials(func):
        @wraps(func)
        def wrapper():
            post_request = request.get_json()
            with open(f"./{DATABASE_FILENAME}", "r") as f:
                all_lines = f.readlines()
                for user_info in all_lines:
                    
                    splited = user_info.split(':')
                    username = splited[0]
                    password = ''

                    if(splited[1][len(splited[1]) -1] == '\n'):
                        password = splited[1][0:len(splited[1]) -1]
                    else:
                        password = splited[1]
                    
                    if(post_request['username'] == username and post_request['password'] == password):
                        message = {'msg': f'Bem vindo {username}'}, 200
                        return message
                    else:
                        message = {'error': 'not authorized'}, 401
                return message
            return func()
        return wrapper


def verify_username(func):
    @wraps(func)
    def wrapper():
        message = ''
        post_request = request.get_json()
        with open(f"./{DATABASE_FILENAME}", "r") as f:
            all_lines = f.readlines()
            for user_info in  all_lines:
                username = user_info.split(':')[0]
                if(post_request['username'] == username):
                    message = {"error": "usuario j?? cadastrado!"}, 422
            if(message == ''):
                 with open(f"./{DATABASE_FILENAME}", "a") as f:
                    formated_user = f'{post_request["username"]}:{post_request["password"]}'
                    f.write("\n")
                    f.write(formated_user)
                    message = {"msg": f"Usu??rio {post_request['username']} criado com sucesso!"}, 201

            return message
        return func()
    return wrapper