<<<<<<< HEAD
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_bd():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'Wasd1313@'),
        database=os.getenv('DB_NAME', 'academia'),
        port=int(os.getenv('DB_PORT', 3306))
    )
=======
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("academia.db")


def conectar_bd():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao


def coluna_existe(cursor, tabela, coluna):
    cursor.execute(f"PRAGMA table_info({tabela})")
    return coluna in [row["name"] for row in cursor.fetchall()]


def adicionar_coluna_se_faltar(cursor, tabela, coluna, definicao):
    if not coluna_existe(cursor, tabela, coluna):
        cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {definicao}")
>>>>>>> df9122e (initial commit - Academia Pinho system)


def criar_tabelas():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("""
<<<<<<< HEAD
    CREATE TABLE IF NOT EXISTS contas_pagar (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(255) NOT NULL,
        forma VARCHAR(100) NOT NULL,
        parcela VARCHAR(100) NOT NULL,
        valor DECIMAL(10,2) NOT NULL,
        data_vencimento DATE NOT NULL,
        status ENUM('pendente','pago') NOT NULL DEFAULT 'pendente',
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute(
        "SELECT COUNT(*) FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = 'clientes' AND COLUMN_NAME = 'data_pago'",
        ("academia",)
    )
    column_exists = cursor.fetchone()[0] > 0

    if not column_exists:
        cursor.execute("ALTER TABLE clientes ADD COLUMN data_pago DATE NULL")

    conexao.commit()
    cursor.close()
    conexao.close()
=======
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT,
        telefone TEXT,
        valor REAL NOT NULL,
        data_pagamento TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pendente',
        data_pago TEXT
    )
    """)

    adicionar_coluna_se_faltar(cursor, "clientes", "cpf", "TEXT")
    adicionar_coluna_se_faltar(cursor, "clientes", "telefone", "TEXT")
    adicionar_coluna_se_faltar(cursor, "clientes", "data_pago", "TEXT")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas_pagar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        forma TEXT NOT NULL,
        parcela TEXT NOT NULL,
        valor REAL NOT NULL,
        data_vencimento TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pendente',
        criado_em TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()
>>>>>>> df9122e (initial commit - Academia Pinho system)
