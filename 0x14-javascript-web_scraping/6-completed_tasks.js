#!/usr/bin/node
/**
 * display the number of TODO completed by user
 */
const request = require('request');
const todoUrl = process.argv[2];

request(todoUrl, (err, response, body) => {
	if (err) {
		console.log(err);
		return
	}
	const data = JSON.parse(body)
	let done = {};
	for (let i = 0; i < Object.keys(data).length; i++) {
		let job = 0;
		userId = 1
		data.forEach(task => {
			if (task.userID === userId) {
				if (task.completed) {
					job++;
				}
			}
		})
		done[userId] = job;
		userId++;
	}
	console.log(done)
			
});
