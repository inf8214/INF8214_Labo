// Commentaire sur une ligne

/*
Commentaire sur plusieurs lignes
*/


// Déclarations variables/constantes
/*
let allows you to declare variables that are limited to the scope of a block statement,
or expression on which it is used, unlike the var keyword, which declares a variable globally,
or locally to an entire function regardless of block scope.
*/
let a = 1     // Variable; portée du bloc
var b = 2     // Variable; portée de la fonction ou du module
const c = 3   // Constante; on ne pourra pas réassigner sans redéclarer

// Arrays (list) & Objects (key-value pairs)
let d = [1, 2, 3]
let e = {nom:"Doe", prenom:"John"}


// Conditionnel
if (x > 50) {
    // do something
} else if (x > 5) {
    // do something
} else {
    // do something
}


// Boucles; 3 exemples
for (let i = 0; i < 5; i++) {            // 3 parties. variable 'compteur'; condition pour continuer; incrémentation du compteur
    console.log("The number is " + i)
}

let animaux = ['chat', 'chien', 'lapin']
for (index in animaux) {                          // Itération sur l'index, qu'on utilise pour récupérer la valeur
    console.log(`Jai un ${animaux[index]}`)
}

animaux.forEach(myFunction);                      // Il y a une mécanique spéciale ici!
function myFunction(value, index, array) {
    console.log(`Jai un ${value}`)
}

for (let [index, value] of animaux.entries()) {   // Méthode alternative qui ressemble à enumerate() en Python
    console.log(`Jai un ${value}`)
}


// Fonctions
const parametre1 = 'Allo'
const parametre2 = 're-Allo'
function nomFonction(parametre1, parametre2) {
    console.log(parametre1)
    console.log(parametre2)
    return 're-re-Allo'
}

msg = nomFonction(parametre1, parametre2)     // Appel
console.log(msg)