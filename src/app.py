# Importa las bibliotecas necesarias
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

# Inicializa la aplicación y habilita CORS
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crea la estructura de la familia
jackson_family = FamilyStructure("Jackson")

# Maneja errores y los serializa como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Genera un sitemap con todos los endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtiene todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    response_body = {
        "members": members
    }
    return jsonify(response_body), 200

# Obtiene un miembro específico de la familia
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Agrega un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.get_json()
    jackson_family.add_member(new_member)
    return jsonify({}), 200

# Elimina un miembro de la familia
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

# Ejecuta la aplicación solo si se ejecuta `$ python src/app.py`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
