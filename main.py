from flask import Flask 
from database import criar_tabelas

app = Flask(__name__)
criar_tabelas()

from views import *

if __name__ == '__main__':
    app.run(debug=True)

    