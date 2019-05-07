$(document).ready(function(){
	// text scrolling logic //
	let textBox = $("#text-box");
	let speedCount;
	if (sessionStorage.getItem('speedCount')){
		speedCount = sessionStorage.getItem('speedCount');
	} else{
		speedCount = 5;
	}
	let paused = true;
	
	let textBoxHeight = textBox[0].scrollHeight;
	let scrollSpeed =  Math.floor(textBoxHeight/speedCount*400)
	textBox.animate({scrollTop: 0});
	
	textBox.on("click", function(){
		if (paused){
			paused = false;
			textBox.animate({scrollTop: textBoxHeight}, scrollSpeed, 'linear');
		} else{
			paused = true;
			textBox.stop();
		}
	});
	// MAKE SCROL SMOOTHER.
	$(".speed-button").on("click", function(){
		if($(this).attr("id") == 'increment-count'){
			if (speedCount < 10){
				speedCount++;
			}
		} else{
			if (speedCount > 1){
				speedCount--;
			}
		}
		sessionStorage.setItem('speedCount', speedCount);
		scrollSpeed =  Math.floor(textBoxHeight/speedCount*400)
		$("#current-speed").text(speedCount);
	});
	
	$("#current-speed").text(speedCount);
	// ****************************** //
	

	// theme settings //
	let theme = sessionStorage.getItem('theme');
	let color;
	let box_background_color;
	let background_color;
	if (theme == "day-button"){
		color = "black";
		box_background_color = "#ffffff";
		background_color = "#f5f5f5";
		$("i.button").removeClass("icon-night");
	} else if (theme == "night-button"){
		color = "#ffffff";
		box_background_color = "#283e4a";
		background_color = "#e1e9ee";
		$("i.button").addClass("icon-night");
	}
	$(".box").css({"background-color": box_background_color, "color": color});
	$("#body").css({"background-color": background_color});
	// $("#testtest").text(theme);

	$(".theme-button").on("click", function(){
		theme = $(this).attr("id");
		sessionStorage.setItem('theme', theme);
		if (theme == "day-button"){
			color = "black";
			box_background_color = "#ffffff";
			background_color = "#f5f5f5"
			$("i.button").removeClass("icon-night");

		} else if (theme == "night-button"){
			color = "#ffffff";
			box_background_color = "#283e4a";
			background_color = "#e1e9ee"
			$("i.button").addClass("icon-night");
		}
		$(".box").css({"background-color": box_background_color, "color": color});
		$("#body").css({"background-color": background_color});
	});
	// ****************************** //
		
	// font settings //
	let fontSize = 16;
	if (sessionStorage.getItem('font-size')){
		fontSize = sessionStorage.getItem('font-size');
	}
	$("#text-box").css({"font-size": fontSize});
	 $(".font-size-button").on("click", function(){
	 	if ($(this).attr("id") == "small"){
	 		fontSize = "16px";
	 	}else if ($(this).attr("id") == "medium"){
	 		fontSize = "18px";
	 	}else{
	 		fontSize = "21px";
	 	}
		sessionStorage.setItem('font-size', fontSize);
		$("#text-box").css({"font-size": fontSize});
	 });
	// ****************************** //

	// Toggle How/Tips sections //
	$("#tips-link").on("click", function(){
		$("#tips").toggle();
	});
	$("#guide-link").on("click", function(){
		$("#guide").toggle();
	});
	// ****************************** //

	// Toggle Settings/Profile sections //
	$("#settings-button").on("click", function(){
		$("#placeholder-box").toggle();
		$("#settings-box").toggleClass('display-none');
	});
	$("#profile-button").on("click", function(){
		$("#profile-box").toggleClass('display-none');
	});
	// ****************************** //

	// Repeat button logic //
	$("#repeat-button").on("click", function(){
		textBox.stop();
		textBox.animate({scrollTop: 0});
	});
	// ****************************** //
})