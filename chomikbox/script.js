"use strict"; // wytłumaczę tą linijkę kiedy lepiej poznasz JS

let chomikbox = {}; // tworzymy pudełko o nazwie chomikbox

chomikbox.czyMuzykaGra = false;
// dodajemy do pudełka informację
// że muzyka w obecnej chwili nie gra

chomikbox.pokazChomika = function() {
	h(".chomik").css("display", "block"); // pokazujemy pudełko z class="chomik"
	h("#startuj").css("display", "none"); // chowamy przycisk z id="startuj"
};

chomikbox.muzyka = function() {
	if (this.czyMuzykaGra) { // czy muzyka gra?
		// muzyka gra, zakończmy ją
		h("audio").getEl().pause();
		h("img").attr("src", "chomik.png"); /* muzyka
		już nie gra. Niech chomik zdjemie słuchawki*/
		this.czyMuzykaGra = false;
	} else {
		// jeśli muzyka nie gra, zacznijmy grać
		h("audio").getEl().play();
		h("img").attr("src", "chomikMuzyka.jpeg"); // niech chomik założy słuchawki
		this.czyMuzykaGra = true;
	};
	// po rozpoczęciu muzyki mówimy,
	// że muzyka gra
	// zmieniamy false na true
	// this oznacza "to pudełko"
};
