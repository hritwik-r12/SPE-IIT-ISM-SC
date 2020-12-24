//current position
var pos4 = 0;
//number of slides
var totalSlides4 = $('#slider-wrap4 ul li').length;
//get the slide width
var sliderWidth4 = $('#slider-wrap4').width();


$(document).ready(function(){


	/*****************
	 BUILD THE SLIDER
	*****************/
	//set width to be 'x' times the number of slides
	$('#slider-wrap4 ul#slider4').width(sliderWidth4*totalSlides4);

    //next slide
	$('#next4').click(function(){
		slideRight4();
	});

	//previous slide
	$('#previous4').click(function(){
		slideLeft4();
	});



	/*************************
	 //*> OPTIONAL SETTINGS
	************************/
	//automatic slider
	var autoSlider4 = setInterval(slideRight4, 3000);

	//for each slide
	$.each($('#slider-wrap4 ul li'), function() {
	   //set its color
	   var c4 = $(this).attr("data-color");
	   $(this).css("background",c4);

	   //create a pagination
	   var li4 = document.createElement('li');
	   $('#pagination-wrap4 ul').append(li4);
	});

	//counter
	countSlides4();

	//pagination
	pagination4();

	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap4').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider4); },
	  function(){ $(this).removeClass('active'); autoSlider4 = setInterval(slideRight4, 3000); }
	);



});//DOCUMENT READY



/***********
 SLIDE LEFT
************/
function slideLeft4(){
	pos4--;
	if(pos4==-1){ pos4 = totalSlides4-1; }
	$('#slider-wrap4 ul#slider4').css('left', -(sliderWidth4*pos4));

	//*> optional
	countSlides4();
	pagination4();
}


/************
 SLIDE RIGHT
*************/
function slideRight4(){
	pos4++;
	if(pos4==totalSlides4){ pos4 = 0; }
	$('#slider-wrap4 ul#slider4').css('left', -(sliderWidth4*pos4));

	//*> optional
	countSlides4();
	pagination4();
}




/************************
 //*> OPTIONAL SETTINGS
************************/
function countSlides4(){
	$('#counter4').html(pos4+1 + ' / ' + totalSlides4);
}

function pagination4(){
	$('#pagination-wrap4 ul li').removeClass('active');
	$('#pagination-wrap4 ul li:eq('+pos4+')').addClass('active');
}