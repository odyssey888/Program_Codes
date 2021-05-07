//Lesson 1: Display to console
console.log("Hello World"); // Can use " " or ' '
console.log('This is my first JS attempt');
console.log("We can mix the quotes, it's OK");

//Lesson 2: Variables & Constants - let, const
let score=0;
const name='James'; //eg a player's name
let age = 21;
const reward=true;
score = 6720120;  // Numeric values do not need quotes

console.log(name);
console.log(score);
console.log(typeof age); //Types of variable: string, Numeric, boolean, null

//Lesson 3: Working with strings, place-holder
console.log('My name is '+ name + " and I am " + age + ' old.');
const greeting = `My name is ${name} and I am ${age} years old.`;//use the `, which is on the key below the Esc key

//Arrays - a container for variables; use [ , ]
const fruits = ['apples', 'oranges', 'pears', 'bananas'];
console.log(fruits[1]); // index within brackets; starts from 0