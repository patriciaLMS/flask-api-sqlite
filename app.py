from flask import Flask, request, jsonify
from db import create_table, insert_data, fetch_data,connect_db
from auth import login, verify_token
import sqlite3

app = Flask(__name__)



#


# Inicializa a tabela ao iniciar o aplicativo
create_table()

@app.route("/login", methods=["POST"])
def login_route():
    print(f"Request Method: {request.method}")  
    return login()




@app.route('/', methods=['POST', 'GET'])
def use_api():
    try:
        decoded_token = verify_token()
        if decoded_token is None:
            return jsonify({"error": "Invalid or missing token"}), 401
        
        if request.method == "POST":
            value = request.json.get('data')  # Recebe o valor do corpo da requisição JSON

            if not value or not isinstance(value,str):return jsonify({"error": "Invalid value provided"}), 400

            insert_data(value)
            
            return jsonify({"message": "Value added successfully"}), 201


        elif request.method == "GET":
           values = fetch_data()
           return jsonify(values), 200


    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
