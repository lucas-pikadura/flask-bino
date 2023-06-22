from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)

    def _repr_(self):
        return f"item{self.nome}"

@app.route('/')
def hello_world():
    return render_template("home.html")
    
@app.route('/produtos')
def page_produtos():
    itens = Item.query.all()
    return render_template("produtos.html",itens = itens)


@app.route('/home')
def page_home():
    return render_template("home.html")