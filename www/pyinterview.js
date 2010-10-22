// Docuemt event handler
$(document).ready(function () {
  var answer_toggle = $('#answer-toggle');
  var correct_answer = $('#correct-answer');

  // Hide answer by default, hide button if no question on the page
  if (correct_answer.length) {
    correct_answer.hide();
    answer_toggle.click(function () {
      correct_answer.toggle('fast');
    })
  } else {
    answer_toggle.hide();
  }
})
