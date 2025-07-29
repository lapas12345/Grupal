"""
Aplicación Flask simple para demostrar Shift-Left Security
"""
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Endpoint principal"""
    return jsonify({"message": "Hello, Secure World!"})

@app.route('/api/data')
def get_data():
    """Endpoint para obtener datos"""
    # Ejemplo de código que podría tener problemas de seguridad
    user_input = request.args.get('query', '')
    
    # Buena práctica: validar entrada
    if len(user_input) > 100:
        return jsonify({"error": "Query too long"}), 400
    
    return jsonify({
        "data": f"Processed: {user_input}",
        "status": "success"
    })

if __name__ == '__main__':
    # Buena práctica: no usar debug=True en producción
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='127.0.0.1')
