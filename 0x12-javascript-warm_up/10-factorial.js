#!/usr/bin/node
function fact(n) {
	if (n === 0)
		return 1;
	console.log(n * fact(n - 1));
}

let n = parseInt(process.argv[2]);
fact(n);
