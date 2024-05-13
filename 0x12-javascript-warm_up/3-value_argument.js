#!/usr/bin/node

const argument = process.argv;

argument.shift();
argument.shift();

if (argument[0] === undefined) {
	console.log('No argument');
} else {
	console.log(arg[0])
}
