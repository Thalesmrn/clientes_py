import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

clientes_bp = Blueprint("clientes", __name__)

@clientes_bp.route("/clientes")
def get_clientes():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@clientes_bp.route("/clientes/<id>")
def get_cliente_by_id(id):
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@clientes_bp.route("/clientes", methods=["POST"])
def novo_cliente():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cliente = request.json
        nome = cliente["nome"]
        email = cliente["email"]
        telefone = cliente["telefone"]
        endereco = cliente["endereco"]
        data_cadastro = cliente["data_cadastro"]

        cursor.execute("""INSERT INTO clientes (nome, email, telefone, endereco, data_cadastro)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (nome, email, telefone, endereco, data_cadastro))
        conn.commit()
        resp = jsonify({"message": "Cliente inserido com sucesso"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@clientes_bp.route("/clientes", methods=["PUT"])
def update_cliente():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cliente = request.json
        id = cliente["id"]
        nome = cliente["nome"]
        email = cliente["email"]
        telefone = cliente["telefone"]
        endereco = cliente["endereco"]
        data_cadastro = cliente["data_cadastro"]

        cursor.execute("""UPDATE clientes
                          SET nome = %s, email = %s, telefone = %s, endereco = %s, data_cadastro = %s
                          WHERE id = %s""",
                       (nome, email, telefone, endereco, data_cadastro, id))
        conn.commit()
        resp = jsonify({"message": "Cliente atualizado com sucesso"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@clientes_bp.route("/clientes/<id>", methods=["DELETE"])
def delete_cliente(id):
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()
        resp = jsonify({"message": "Cliente excluído com sucesso"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
