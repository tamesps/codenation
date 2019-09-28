# Desafio de programação orientada a testes

Dark sky é um serviço de previsão do tempo por API. Temos uma função que faz uma requisição para a api
do Dark sky passando a latitude e a longitude de algum lugar no planeta e a api retorna a temperatura. Nossa função
converte para celsius e retorna o valor da temperatura.


Escreva um teste que seja possível testar off-line a chamada para api do Dark sky e a conversão para celsius.
Use a bibliteca Pytest e os seguntes dados para testar a função **get_temperature**.

    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16

A função a ser testada esta no arquivo **main.py** implemente o teste no arquivo **test_main.py**

## Tópicos

Neste desafio você vai aprender:

- Testes unitários
- Mock
- Pytest
- Monkeypatch

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`
