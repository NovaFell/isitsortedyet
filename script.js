function isItSortedYet() {
	const array = [4,3,5,2,6,8,7,9,1];
	let isSorted = false
	
	while(isSorted == false) {
		isSorted = checkIfSorted(array);
		renderList(array);
		document.getElementById("array").innerHTML = array;
	}
	if(isSorted == true) {
		document.getElementById("answer").innerHTML = "The array is sorted! :D";
	}
}

function checkIfSorted(array) {
	for(int i = 0; i < array.length - 1; i++) {
		if(array[i] > array[i+1]) {
			return false;
		}
	}
	return true;
}

function renderList(array) {
	let result = "";
	for(int i = 0; i < array.length; i++) {
		result += '<li>' + array[i] + '</li>'
	}
	document.getElementById("table").innerHTML = result
}

