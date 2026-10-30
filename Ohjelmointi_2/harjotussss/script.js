let syote = prompt("Kivi (1), Paperi (2) vai Sakset (3)");
let vastaus = Math.floor(Math.random() * 3) + 1;

        if (syote == 1) {
            if (vastaus == 1) {
            console.log("Tasapeli!");
            }
            if (vastaus == 2) {
            console.log("Hävisit!");
            }
            if (vastaus == 3) {
            console.log("Voitit!");
            }
        }

        if (syote == 2) {
            if (vastaus == 1) {
            console.log("Voitit!");
            }
            if (vastaus == 2) {
            console.log("Tasapeli!");
            }
            if (vastaus == 3) {
            console.log("Hävisit!");
            }
        }

        if (syote == 3) {
            if (vastaus == 1) {
            console.log("Hävisit!");
            }
            if (vastaus == 2) {
            console.log("Voitit!");
            }
            if (vastaus == 3) {
            console.log("Tasapeli!");
            }
        }
        
        console.log("Tietokone valitsi: " + vastaus);