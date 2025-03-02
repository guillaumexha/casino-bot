function playCoinflip() {
    fetch('/coinflip', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({"bet": 10, "choice": "Pile"})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `Résultat: ${data.result} - ${data.status}`;
    });
}

function playBlackjack() {
    fetch('/blackjack', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({"bet": 10})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `Votre main: ${data.player} - Croupier: ${data.dealer} - ${data.status}`;
    });
}

function playRoulette() {
    fetch('/roulette', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({"bet": 10, "choice": "Rouge"})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `Numéro: ${data.winning_number} - Couleur: ${data.winning_color} - ${data.status}`;
    });
}