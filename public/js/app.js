var changeStatus = function (status) {
  $('#status').text(status);
};

var changeStatusToAnalyzing = function () {
  changeStatus('Analyzing...');
};

var changeStatusToError = function () {
  changeStatus('Error');
};

var changeStatusToResult = function (result) {
  changeStatus('It looks like ' + (isVowel(result.charAt(0)) ? 'an' : 'a') + ' ' + result.replace('_', ' ').toLowerCase());
};

function isVowel(c) {
  return ['a', 'e', 'i', 'o', 'u'].indexOf(c.toLowerCase()) !== -1
}

$('.example-image').click(function (event) {
  var image = $(event.target);
  var url = image.attr('src');
  changeStatusToAnalyzing();
  $.post('/url', {url: url}).done(function (data) {
    changeStatusToResult(data);
  }).fail(function () {
    changeStatusToError();
  });
});

$("#url-form input").bind('input', function(event) {
  var form = $(event.target).parent();
  var url = form.find('input').val();
  changeStatusToAnalyzing();
  $.post('/url', {url: url}).done(function (data) {
    changeStatusToResult(data);
  }).fail(function () {
    changeStatusToError();
  });
  event.preventDefault();
});

$("#upload-form input").change(function (event) {
  event.preventDefault();
  var form = $(event.target).parent();
  var fileInput = form.find('input');

  var formData = new FormData();
  formData.append(fileInput.attr('name'), fileInput[0].files[0]);
  var request = new XMLHttpRequest();

  request.onreadystatechange = function () {
    if (request.readyState == 4) {
      if (request.status == 200) {
        changeStatusToResult(request.responseText);
      } else {
        changeStatusToError();
      }
    }
  };
  
  changeStatusToAnalyzing();
  request.open("POST", form.attr('action'));
  request.send(formData);
});
