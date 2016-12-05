// send the page title as a chrome message
// Question - document.getElementsByClassName('QuestionText')[0].getElementsByClassName('rendered_qtext')[0].innerHTML
// Answer - document.getElementsByClassName('Answer')[0].getElementsByClassName('answer_permalink')[0].href

var sendData = function(answer) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://localhost:5000/classify",false);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.send(
		JSON.stringify({body:answer})
	);
	return JSON.parse(xhr.response).task.response
}


var message = '';
var q1 = document.getElementsByClassName('Answer');
for(var i = 0;i<q1.length;i+=4) {
	q2 = q1[i].getElementsByClassName('answer_permalink');

	if(q2.length==0)
		continue	
	q3 = q2[0].href
	var m = ''
	//get answer
	a = q1[i].getElementsByClassName('rendered_qtext')
	for(var j=a.length-1;j>=0;j--) {
		var para_array = a[j].getElementsByClassName('qtext_para')
		var answer = ''
		for(var k = 0;k<para_array.length;k++)
			answer += para_array[k].innerHTML
		m += ('<br>' + sendData(answer) + '<br>')
		break;
	}

	url=q1[i].previousSibling.getElementsByClassName('QuestionText')
	console.log("url",url)
	if(url.length) {
		url = url[0].getElementsByClassName('rendered_qtext')[0].innerHTML
		m += '<a href="'+q3+'"'+' target="_blank"'+'>'+url+'</a>'
		m += '<br><br>'
		message += m
	}


}

chrome.runtime.sendMessage(message);