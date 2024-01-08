#!/usr/bin/node
const {argv } = require('node:process');

let passed_args = argv.slice(2);

if (passed_args.length === 0)
{
	console.log('No argument');
}else{
	console.log('Arguments found');
}
