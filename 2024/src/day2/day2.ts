const { open } = require('node:fs/promises');

async function parseReports(filename: string): Promise<string[][]> {
	let reports = [];
	let file = await open(filename);
	for await (const line of file.readLines()) {
		let report = line.split(" ");
		reports.push(report);
	}
	return reports;
}

function countSafeReports(reports: string[][], tolerate: boolean) {
	let safeReports = 0;
	for (let i = 0; i < reports.length; i++) {
		let increasing;
		let decreasing;
		let safe;
		let previous_level;
		for (let j = 0; j < reports[i].length; j++) {
			let level = Number(reports[i][j]);
			if (previous_level === undefined) {
				previous_level = level;
				continue
			}
			if ((increasing != undefined) && (increasing === decreasing)) {
				safe = false;
				break;
			}
			if ((Math.abs(level - previous_level) > 3) || level === previous_level) {
				safe = false;
				break;
			}
			if (level - previous_level > 0) {
				increasing = true;
			} else {
				decreasing = true;
			}
			previous_level = level;
		}
		if ((safe != false) && increasing != decreasing) {
			safeReports += 1;
		}
	}
	return safeReports;
}

parseReports("src/day2/training_set").then((reports) => {
	let safeReports = countSafeReports(reports);
	console.assert(safeReports === 2);
});

parseReports("src/day2/puzzle_input").then((reports) => {
	let safeReports = countSafeReports(reports);
	console.log(`Day2 part1: ${safeReports}`);
})
