#!/usr/bin/node
/* Prints the command line argument passed using a format "is" */

const arg = process.argv;

arg.shift();
arg.shift();

let string = '';
const undef = undefined;

if (arg.length === 0) {
	console.log(`${undef} is ${undef}`);
} else {
	for (let i = 0; i < arg.length; i++) {
		string = string + arg[i];

		if (arg.length - i !== 1) {
			string = string + ' ' + 'is' + ' ';
		}
	}
	console.log(string);
}
