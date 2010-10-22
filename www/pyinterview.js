// Docuemt event handler
$(document).ready(function () {
  var correct_answer = $('#correct-answer');
  correct_answer.hide();
  
  $('#answer-toggle').click(function () {
    correct_answer.toggle('fast');
  })
})
