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


def criar_tabelas():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("""
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
