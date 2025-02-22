import os
from flask import Flask, jsonify
from flask_cors import CORS  # Importer CORS pour éviter les erreurs CORS

app = Flask(__name__)
CORS(app)  # Active CORS pour permettre l'accès depuis ton site web

@app.route('/')  # Page d'accueil pour vérifier si l'API tourne bien
def home():
    return "Bienvenue sur l'API de Cryptomonnaies !"

@app.route('/recommend', methods=['GET'])  # Route pour afficher les cryptos
def recommend_cryptos():
    data = [
        {"name": "Bitcoin", "symbol": "BTC", "current_price": 50000},
        {"name": "Ethereum", "symbol": "ETH", "current_price": 3000},
        {"name": "Solana", "symbol": "SOL", "current_price": 150},
    ]
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Utilisation du port Railway
    app.run(debug=True, host="0.0.0.0", port=port)
