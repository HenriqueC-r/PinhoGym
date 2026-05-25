from main import app
from flask import render_template, request, redirect
from database import conectar_bd
from datetime import date, datetime, timedelta


<<<<<<< HEAD
=======
def fetchall_dict(cursor):
    return [dict(row) for row in cursor.fetchall()]


def fetchone_dict(cursor):
    row = cursor.fetchone()
    return dict(row) if row else None


>>>>>>> df9122e (initial commit - Academia Pinho system)
def calcular_status(data_pagamento, status_atual):
    hoje = date.today()

    if status_atual == 'fechado':
        return 'fechado'

    if isinstance(data_pagamento, str):
        data_pagamento = datetime.strptime(data_pagamento, "%Y-%m-%d").date()

    if status_atual == 'pago':
        return 'pago'

    if data_pagamento + timedelta(days=60) <= hoje:
        return 'fechado'

    if status_atual == 'pendente':
        return 'pendente'

    return 'pendente' if data_pagamento < hoje else 'pago'


# 🏠 HOME
@app.route('/')
def homepage():
    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
=======
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = fetchall_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)

    cursor.close()
    conexao.close()

    total_clientes = len(clientes)
    total_pago = 0.0
    total_pendente = 0.0
    total_fechado = 0.0
    cadastros = [0] * 12

    faturamento = [0] * 12  # 12 meses

    for c in clientes:
        if isinstance(c['data_pagamento'], str):
            c['data_pagamento'] = datetime.strptime(c['data_pagamento'], "%Y-%m-%d").date()

        if c.get('data_pago') and isinstance(c['data_pago'], str):
            c['data_pago'] = datetime.strptime(c['data_pago'], "%Y-%m-%d").date()

        status = calcular_status(c['data_pagamento'], c['status'])
        valor = float(c['valor'])
        mes = c['data_pagamento'].month - 1
        cadastros[mes] += 1

        if status == 'pago':
            total_pago += valor

            # pega o mês do pagamento
            if c.get('data_pago'):
                mes = c['data_pago'].month - 1
                faturamento[mes] += valor

        elif status == 'pendente':
            total_pendente += valor

        elif status == 'fechado':
            total_fechado += valor

    return render_template(
    "inicio.html",
    total_clientes=total_clientes,
    total_pago=total_pago,
    total_pendente=total_pendente,
    total_fechado=total_fechado,
    cadastros=cadastros
)
    

# 📝 CADASTRO
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")


# 💰 CONTAS A PAGAR
@app.route('/contas-a-pagar')
def contas_a_pagar():
    q = request.args.get('q', '').strip()

    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)
=======
    cursor = conexao.cursor()
>>>>>>> df9122e (initial commit - Academia Pinho system)

    sql = "SELECT * FROM contas_pagar"
    params = ()
    if q:
<<<<<<< HEAD
        sql += " WHERE descricao LIKE %s OR forma LIKE %s OR parcela LIKE %s"
=======
        sql += " WHERE descricao LIKE ? OR forma LIKE ? OR parcela LIKE ?"
>>>>>>> df9122e (initial commit - Academia Pinho system)
        like = f"%{q}%"
        params = (like, like, like)

    cursor.execute(sql, params)
<<<<<<< HEAD
    contas = cursor.fetchall()
=======
    contas = fetchall_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)
    cursor.close()
    conexao.close()

    for c in contas:
        if isinstance(c.get('data_vencimento'), str):
            c['data_vencimento'] = datetime.strptime(c['data_vencimento'], "%Y-%m-%d").date()

    total_pendente = sum(float(c['valor']) for c in contas if c['status'] == 'pendente')
    total_pago = sum(float(c['valor']) for c in contas if c['status'] == 'pago')
    total_geral = sum(float(c['valor']) for c in contas)

    return render_template(
        "contas_pagar.html",
        contas=contas,
        total_pendente=total_pendente,
        total_pago=total_pago,
        total_geral=total_geral,
        search_query=q
    )


@app.route('/contas-a-pagar/adicionar', methods=['POST'])
def contas_a_pagar_adicionar():
    descricao = request.form['descricao']
    forma = request.form['forma']
    parcela = request.form['parcela']
    valor = request.form['valor']
    data_vencimento = request.form['data_vencimento']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute(
<<<<<<< HEAD
        "INSERT INTO contas_pagar (descricao, forma, parcela, valor, data_vencimento) VALUES (%s, %s, %s, %s, %s)",
=======
        "INSERT INTO contas_pagar (descricao, forma, parcela, valor, data_vencimento) VALUES (?, ?, ?, ?, ?)",
>>>>>>> df9122e (initial commit - Academia Pinho system)
        (descricao, forma, parcela, valor, data_vencimento)
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/contas-a-pagar')


@app.route('/contas-a-pagar/editar/<int:id>')
def contas_a_pagar_editar(id):
    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contas_pagar WHERE id = %s", (id,))
    conta = cursor.fetchone()
=======
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas_pagar WHERE id = ?", (id,))
    conta = fetchone_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)
    cursor.close()
    conexao.close()

    if not conta:
        return redirect('/contas-a-pagar')

    return render_template("contas_pagar_edit.html", conta=conta)


@app.route('/contas-a-pagar/atualizar/<int:id>', methods=['POST'])
def contas_a_pagar_atualizar(id):
    descricao = request.form['descricao']
    forma = request.form['forma']
    parcela = request.form['parcela']
    valor = request.form['valor']
    data_vencimento = request.form['data_vencimento']
    status = request.form['status']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute(
<<<<<<< HEAD
        "UPDATE contas_pagar SET descricao=%s, forma=%s, parcela=%s, valor=%s, data_vencimento=%s, status=%s WHERE id=%s",
=======
        "UPDATE contas_pagar SET descricao=?, forma=?, parcela=?, valor=?, data_vencimento=?, status=? WHERE id=?",
>>>>>>> df9122e (initial commit - Academia Pinho system)
        (descricao, forma, parcela, valor, data_vencimento, status, id)
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/contas-a-pagar')


@app.route('/contas-a-pagar/pagar/<int:id>', methods=['POST'])
def contas_a_pagar_pagar(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()
<<<<<<< HEAD
    cursor.execute("UPDATE contas_pagar SET status='pago' WHERE id=%s", (id,))
=======
    cursor.execute("UPDATE contas_pagar SET status='pago' WHERE id=?", (id,))
>>>>>>> df9122e (initial commit - Academia Pinho system)
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/contas-a-pagar')

@app.route('/contas-a-pagar/excluir/<int:id>', methods=['POST'])
def contas_a_pagar_excluir(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()
<<<<<<< HEAD
    cursor.execute("DELETE FROM contas_pagar WHERE id=%s", (id,))
=======
    cursor.execute("DELETE FROM contas_pagar WHERE id=?", (id,))
>>>>>>> df9122e (initial commit - Academia Pinho system)
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/contas-a-pagar')


# 📌 CADASTRAR CLIENTE (sempre começa como pago se ainda não vence)
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    valor = request.form['valor']
    data_vencimento = request.form['data_pagamento']

    if isinstance(data_vencimento, str):
        data_vencimento_date = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    else:
        data_vencimento_date = data_vencimento

    if data_vencimento_date >= date.today():
        status = 'pago'
    elif data_vencimento_date + timedelta(days=60) <= date.today():
        status = 'fechado'
    else:
        status = 'pendente'

<<<<<<< HEAD
    data_pago = date.today() if status == 'pago' else None
=======
    data_pago = date.today().isoformat() if status == 'pago' else None
>>>>>>> df9122e (initial commit - Academia Pinho system)

    conexao = conectar_bd()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO clientes (nome, cpf, telefone, valor, data_pagamento, status, data_pago)
<<<<<<< HEAD
    VALUES (%s, %s, %s, %s, %s, %s, %s)
=======
    VALUES (?, ?, ?, ?, ?, ?, ?)
>>>>>>> df9122e (initial commit - Academia Pinho system)
    """

    cursor.execute(sql, (nome, cpf, telefone, valor, data_vencimento, status, data_pago))
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect('/clientes')
@app.route('/cliente/excluir/<int:id>', methods=['POST'])
def excluir_cliente(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()
<<<<<<< HEAD
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
=======
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
>>>>>>> df9122e (initial commit - Academia Pinho system)
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/clientes')

# 📋 LISTA DE CLIENTES (STATUS AUTOMÁTICO POR DATA)
@app.route('/clientes')
def clientes():
    q = request.args.get('q', '').strip()

    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
=======
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = fetchall_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)

    cursor.close()
    conexao.close()

    for c in clientes:

        # 🔥 garante que data é DATE de verdade
        if isinstance(c['data_pagamento'], str):
            c['data_pagamento'] = datetime.strptime(c['data_pagamento'], "%Y-%m-%d").date()
        if c.get('data_pago') and isinstance(c['data_pago'], str):
            c['data_pago'] = datetime.strptime(c['data_pago'], "%Y-%m-%d").date()

        c['status'] = calcular_status(c['data_pagamento'], c['status'])

    total_pago = sum(float(c['valor']) for c in clientes if c['status'] == 'pago')

    if q:
        q_lower = q.lower()

        def cliente_key(c):
            nome = (c.get('nome') or '').lower()
            cpf = (c.get('cpf') or '').lower()
            match = 0 if q_lower in nome or q_lower in cpf else 1
            return (match, nome)

        clientes.sort(key=cliente_key)

    return render_template(
        "clientes.html",
        clientes=clientes,
        search_query=q,
        total_pago=total_pago
    )


# 🔍 DETALHE CLIENTE
@app.route('/cliente/<int:id>')
def cliente_detalhe(id):
    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()
=======
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = fetchone_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)

    cursor.close()
    conexao.close()

    if cliente:
        if isinstance(cliente['data_pagamento'], str):
            cliente['data_pagamento'] = datetime.strptime(cliente['data_pagamento'], "%Y-%m-%d").date()
        cliente['status'] = calcular_status(cliente['data_pagamento'], cliente['status'])

    return render_template("cliente_detalhe.html", cliente=cliente)


# ✏️ ATUALIZAR CLIENTE (manual: fechado / ajustes)
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar_cliente(id):
    if request.form.get('delete'):
        conexao = conectar_bd()
        cursor = conexao.cursor()
<<<<<<< HEAD
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
=======
        cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
>>>>>>> df9122e (initial commit - Academia Pinho system)
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect('/clientes')

    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    valor = request.form['valor']
    data_vencimento = request.form['data_pagamento']
    status = request.form['status']

    conexao = conectar_bd()
<<<<<<< HEAD
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT data_pago FROM clientes WHERE id = %s", (id,))
    row = cursor.fetchone()
=======
    cursor = conexao.cursor()

    cursor.execute("SELECT data_pago FROM clientes WHERE id = ?", (id,))
    row = fetchone_dict(cursor)
>>>>>>> df9122e (initial commit - Academia Pinho system)
    existing_data_pago = row.get('data_pago') if row else None

    data_pago = existing_data_pago
    if status == 'pago' and not existing_data_pago:
<<<<<<< HEAD
        data_pago = date.today()

    sql = """
    UPDATE clientes 
    SET nome=%s, cpf=%s, telefone=%s, valor=%s, data_pagamento=%s, status=%s, data_pago=%s
    WHERE id=%s
=======
        data_pago = date.today().isoformat()

    sql = """
    UPDATE clientes 
    SET nome=?, cpf=?, telefone=?, valor=?, data_pagamento=?, status=?, data_pago=?
    WHERE id=?
>>>>>>> df9122e (initial commit - Academia Pinho system)
    """

    cursor.execute(sql, (nome, cpf, telefone, valor, data_vencimento, status, data_pago, id))
    conexao.commit()

    cursor.close()
    conexao.close()

<<<<<<< HEAD
    return redirect('/clientes')
=======
    return redirect('/clientes')
>>>>>>> df9122e (initial commit - Academia Pinho system)
