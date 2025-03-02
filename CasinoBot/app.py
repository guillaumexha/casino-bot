from flask import Flask, request, jsonify, render_template  
import random  

app = Flask(__name__)  

@app.route("/")
def home():
    return render_template("app.html")  # Affiche la page HTML principale

@app.route('/coinflip', methods=['POST'])  
def coin_flip():  
    data = request.json  # Récupère les données envoyées (mise + choix du joueur)  
    if not data or "bet" not in data or "choice" not in data:  
        return jsonify({"error": "Données invalides"}), 400  

    bet = data["bet"]  
    choice = data["choice"].capitalize()  # Convertir en "Pile" ou "Face"  
    result = random.choice(["Pile", "Face"])  

    if choice not in ["Pile", "Face"]:  
        return jsonify({"error": "Choix invalide, utilisez 'Pile' ou 'Face'"}), 400  

    if choice == result:  
        return jsonify({"result": result, "status": "Gagné", "payout": bet * 2})  
    else:  
        return jsonify({"result": result, "status": "Perdu", "payout": 0})  

@app.route('/blackjack', methods=['POST'])
def blackjack():
    data = request.json
    if not data or "bet" not in data:
        return jsonify({"error": "Données invalides"}), 400

    bet = data["bet"]

    # Simulation d'un jeu simple : l'utilisateur reçoit une main, le croupier aussi
    import random
    player_hand = random.randint(12, 21)  # Main du joueur entre 12 et 21
    dealer_hand = random.randint(15, 21)  # Main du croupier entre 15 et 21

    if player_hand > 21:  # Si le joueur dépasse 21, il perd
        return jsonify({"player": player_hand, "dealer": dealer_hand, "status": "Perdu", "payout": 0})
    elif dealer_hand > 21 or player_hand > dealer_hand:  # Le joueur gagne
        return jsonify({"player": player_hand, "dealer": dealer_hand, "status": "Gagné", "payout": bet * 2})
    elif player_hand == dealer_hand:  # Égalité
        return jsonify({"player": player_hand, "dealer": dealer_hand, "status": "Égalité", "payout": bet})
    else:  # Le croupier gagne
        return jsonify({"player": player_hand, "dealer": dealer_hand, "status": "Perdu", "payout": 0})

@app.route('/roulette', methods=['POST'])
def roulette():
    data = request.json
    if not data or "bet" not in data or "choice" not in data:
        return jsonify({"error": "Données invalides"}), 400

    bet = data["bet"]
    choice = data["choice"]  # Peut être un numéro (0-36) ou une couleur (Rouge/Noir)

    # Simulation du lancer de roulette
    import random
    winning_number = random.randint(0, 36)
    winning_color = "Rouge" if winning_number % 2 == 0 else "Noir"

    if choice.isdigit():  # Pari sur un numéro
        choice = int(choice)
        if choice == winning_number:
            return jsonify({"winning_number": winning_number, "winning_color": winning_color, "status": "Gagné", "payout": bet * 35})
        else:
            return jsonify({"winning_number": winning_number, "winning_color": winning_color, "status": "Perdu", "payout": 0})
    elif choice in ["Rouge", "Noir"]:  # Pari sur une couleur
        if choice == winning_color:
            return jsonify({"winning_number": winning_number, "winning_color": winning_color, "status": "Gagné", "payout": bet * 2})
        else:
            return jsonify({"winning_number": winning_number, "winning_color": winning_color, "status": "Perdu", "payout": 0})
    else:
        return jsonify({"error": "Choix invalide, utilisez un numéro entre 0 et 36 ou 'Rouge'/'Noir'"}), 400

if __name__ == '__main__':  
    app.run(debug=True)