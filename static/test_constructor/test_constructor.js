var x = 0;

function addInput() {
	if (x < 20) {
    var str = '<input autocomplete="off" name="option' + (x + 1) + '" type="text" class="mb-1 mr-1"><input name="correct' + (x + 1) +'" class="custom-checkbox" type="checkbox" id="correct' + (x + 1) +'"><label for="correct' + (x + 1) +'"></label><div id="input' + (x + 1) + '"></div>';
    document.getElementById('input' + x).innerHTML = str;
    x++;
  } else
  {
  	alert('Слишком много вариантов ответа');
  }
}

function removeInput() {
    document.getElementById('input' + (x - 1)).innerHTML = ' ';
    x--;
}

function deleteQuestion() {
    return confirm("Удалить этот вопрос?");
}
