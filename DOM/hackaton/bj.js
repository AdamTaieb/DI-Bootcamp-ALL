let blackjackGame = {
	you: {
		scoreSpan: "#your-blackjack-result", 
		div: "#your-box",
		boxSize : ".flex-blackjack-row-2 div",
		score: "0",
	}, 

	dealer: {
		scoreSpan: "#dealer-blackjack-result", 
		div: "#dealer-box",
		boxSize : ".flex-blackjack-row-2 div",
		score: "0",
	},

	'cards': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q', 'A'],

	cardsMap: {
		2: 2, 
		3: 3, 
		4: 4, 
		5: 5, 
		6: 6, 
		7: 7, 
		8: 8, 
		9: 9, 
		10: 10, 
		K: 10, 
		J: 10, 
		Q: 10, 
		A: [1,11],
	},

	wins: 0,
	losses: 0,
	draws: 0,
	isStand: false,
	isTurnsOver: false,
	pressOnce: false,
}

const YOU = blackjackGame['you'];
const DEALER = blackjackGame['dealer'];
const hitSound = new Audio("");
const winSound = new Audio("");
const loseSound = new Audio("");

let windoWidth = window.screen.width;
let windowHeight = window.screen.height;
let winner;

document.querySelector("#blackjack-hit-button").addEventListener("click", blackjackHit);

document.querySelector('#blackjack-stand-button').addEventListener('click', blackjackStand())

function blackjackHit() {
	if(blackjackGame['isStand']===false){
		let card = randomCard();
		showCard(card, YOU);
		updateScore(card, YOU);
		showScore(YOU);
	}
}

function randomCard(){
	let randomIndex = Math.floor(Math.random() * 13);
	return blackjackGame["cards"][randomIndex];
}

function showCard(card, activePlayer){
	if(activePlayer['score'] <= 21){
		let cardImage = document.createElement("img")
		cardImage.src = `images/${card}.png`;
		cardImage.style = `width: ${widthSize()}; height:${heightSize()};`;
		document.querySelector(activePlayer["div"]).appendChild(cardImage);
		hitSound.play();

	}
}

function widthSize() {
	if(windoWidth > 1000){
		let newWidthSize = window.screen.width * 0.1;
		return newWidthSize
	}
	else{
		return window.screen.width * 0.18;
	}
}

function heightSize() {
	if(windoHeight > 700){
		let newHeightSize = window.screen.height * 0.18;
		return newHeightSize
	}
	else{
		return window.screen.height * 0.15;
	}
}

function updateScore(card, activePlayer){
	if(card === 'A'){
		if(activePlayer["score"] + blackjackGame["cardsMap"][card][1] <= 21){
			activePlayer["score"] += blackjackGame["cardsMap"][card][1];
		}
		else{
			activePlayer["score"] += blackjackGame["cardsMap"][card][0];
		}
	}
	else {
		activePlayer["score"] += blackjackGame["cardsMap"][card];
	}
	
}

function showScore(activePlayer){
	if(activePlayer["score"] > 21){
		document.querySelector(activePlayer['scoreSpan']).textContent = "BUST";
		document.querySelector(activePlayer['scoreSpan']).style.color = "red";
	}

	else{
		document.querySelector(activePlayer['scoreSpan']).textContent = activePlayer["score"]
	}
}


function blackjackStand(){
	if(blackjackGame.pressOnce === false){
		blackjackGame['isStand']=true;
		let yourImages = document.querySelector("#your-box").querySelectorAll("img");
	

	for(let i = 0; i < yourImages.length; i++){
		let card = randomCard();
		showCard(card, DEALER);
		updateScore(card, DEALER);
		showScore(DEALER);

		blackjackGame['isTurnsOver'] = true;

		computeWinner();
		showWinner(winner);

	}
}
    blackjackGame.pressOnce = true;
}

function computeWinner(){
	if(YOU['score'] <= 21) {
		if(YOU['score'] > DEALER['score'] || DEALER['score'] > 21){
			winner = YOU;
		}
		else if(YOU['score'] < DEALER['score']){
			winner = DEALER;
		}
		else if(YOU['score'] === DEALER['score']) {
			winner = "draw"
		}
	
	else if(YOU['score'] > 21 && DEALER['score'] <=21){
		winner = DEALER
	}
	else if(YOU['score'] > 21 && DEALER['score'] >21){
		winner = "None"


}
return winner
}

function showWinner(){
	let message , messageColor;

	if(winner === YOU){
		message = 'You Won'
		messageColor = '#00e676'
		document.querySelector('#wins').textContent = blackjackGame['wins']+=1;
		winSound.play()
	}

	if(winner === DEALER){
		message = 'You Lost'
		messageColor = 'red'
		document.querySelector('#losses').textContent = blackjackGame['losses']+=1;
		loseSound.play()
	}

	if(winner === 'Draw'){
		message = 'You drew'
		messageColor = 'yellow'
		document.querySelector('#draws').textContent = blackjackGame['draws']+=1;
		loseSound.play()
	}

	if(winner === 'None'){
		message = 'you both busted'
		messageColor = 'orange'
		loseSound.play()
	}

document.querySelector('#blackjack-result').textContent = message;
document.querySelector('#blackjack-result').style.color = messageColor;

}

