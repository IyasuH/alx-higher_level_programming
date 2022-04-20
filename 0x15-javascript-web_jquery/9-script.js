$(document).ready(function(){
	$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => 
		{
			const hello = data.hello;
			$('DIV#hello').text(hello);
		});
});
