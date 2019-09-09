$(document).ready(function(){
	console.log("-----------test 1 message-----------")
	//$( ".kave-btn" ).hover(function() {alert("hello")});
	$( ".kave-btn" ).click(function() {
		console.log("-----------test message-----------")
		droplets.send('{"method":"hello","args":{"msg":"stupid"}}');
	});
});