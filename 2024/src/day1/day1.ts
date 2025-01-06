const { open } = require('node:fs/promises');

function pairUpList(leftList: number[], rightList: number[]): number {
	leftList.sort();
	rightList.sort();
	let total_distance = 0;
	if (leftList.length != rightList.length) {
			throw new Error("leftList and rightList can't be of different sizes");
	}
	for (let i = 0; i < leftList.length; i++) {
		total_distance += Math.abs(leftList[i]-rightList[i]);
	}
	return total_distance;
}

async function parseLists(filename: string): Promise<[ number[], number[] ]> {
	let leftList: number[] = [];
	let rightList: number[] = [];
	const file = await open(filename);
	for await (const line of file.readLines()) {
		let [leftElement, rightElement] = line.split("   ");
		leftList.push(leftElement);
		rightList.push(rightElement);
	}
	return [leftList, rightList];
}

function countOccurrences(list: number[]) {
	let occurrences: { [ index: string ] : number } = {};
	for (let i = 0; i < list.length; i++) {
		occurrences[list[i]] = occurrences[list[i]] ? occurrences[list[i]] + 1 : 1;
	}
	return occurrences;
}

let leftList: number[];
let rightList: number[];
parseLists("src/day1/training_set").then(([leftList, rightList]) => {
	let result = pairUpList(leftList, rightList);
	console.assert(result === 11);
	leftList = [];
	rightList = [];
});

parseLists("src/day1/puzzle_input").then(([leftList, rightList]) => {
	let result = pairUpList(leftList, rightList);
	console.log(`Day1 part1: ${result}`);
});

// day2

leftList = [];
rightList = [];

parseLists("src/day1/training_set").then(([leftList, rightList]) => {
	let occurrences = countOccurrences(rightList);
	let similarity = 0;
	for (let i = 0; i < leftList.length; i++) {
		if (occurrences[leftList[i]]) {
			similarity += Number(leftList[i]) * occurrences[leftList[i]];
		}
	}
	console.assert(similarity === 31);
});

leftList = [];
rightList = [];

parseLists("src/day1/puzzle_input").then(([leftList, rightList]) => {
	let occurrences = countOccurrences(rightList);
	let similarity = 0;
	for (let i = 0; i < leftList.length; i++) {
		if (occurrences[leftList[i]]) {
			similarity += Number(leftList[i]) * occurrences[leftList[i]];
		}
	}
	console.log(`Day1 part2: ${similarity}`);
});
