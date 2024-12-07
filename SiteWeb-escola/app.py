from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('SiteWeb-escola/escola.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods= ['GET', 'POST'])
def index():
    conn = get_db_connection()
    