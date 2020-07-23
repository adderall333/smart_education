var x = 0;

function addInput() {
	if (x < 20) {
    var str = '<input name="option' + (x + 1) + '" type="text"><input name="correct' + (x + 1) +'" type="checkbox"><div id="input' + (x + 1) + '"></div>';
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
