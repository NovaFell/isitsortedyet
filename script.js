"use strict";

function isItSortedYet() {
	const array = [4,3,5,2,6,8,7,9,1];
	let isSorted = false
	
	while(isSorted === false) {
		isSorted = checkIfSorted(array);
		renderList(array);
		document.getElementById("array").innerHTML = array;
	}
	if(isSorted === true) {
		document.getElementById("answer").innerHTML = "The array is sorted! :D";
	}
}

function checkIfSorted(array) {
	let len = array.length

	for(let i = 0; i < len - 1; i++) {
		if(array[i] > array[i+1]) {
			return false;
		}
	}
	return true;
}

function renderList(array) {
	let result = "";
	let len = array.length

	for(let i = 0; i < len; i++) {
		result += '<li>' + array[i] + '</li>'
	}
	document.getElementById("table").innerHTML = result
}

isItSortedYet();

