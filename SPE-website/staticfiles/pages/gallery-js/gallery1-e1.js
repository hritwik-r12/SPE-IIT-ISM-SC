//current position
var pos1 = 0;
//number of slides
var totalSlides1 = $('#slider-wrap1 ul li').length;
//get the slide width
var sliderWidth1 = $('#slider-wrap1').width();


$(document).ready(function(){


	/*****************
	 BUILD THE SLIDER
	*****************/
	//set width to be 'x' times the number of slides
	$('#slider-wrap1 ul#slider1').width(sliderWidth1*totalSlides1);

    //next slide
	$('#next1').click(function(){
		slideRight1();
	});

	//previous slide
	$('#previous1').click(function(){
		slideLeft1();
	});



	/*************************
	 //*> OPTIONAL SETTINGS
	************************/
	//automatic slider
	var autoSlider1 = setInterval(slideRight1, 3000);

	//for each slide
	$.each($('#slider-wrap1 ul li'), function() {
	   //set its color
	   var c1 = $(this).attr("data-color");
	   $(this).css("background",c1);

	   //create a pagination
	   var li1 = document.createElement('li');
	   $('#pagination-wrap1 ul').append(li1);
	});

	//counter
	countSlides1();

	//pagination
	pagination1();

	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap1').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider1); },
	  function(){ $(this).removeClass('active'); autoSlider1 = setInterval(slideRight1, 3000); }
	);



});//DOCUMENT READY



/***********
 SLIDE LEFT
************/
function slideLeft1(){
	pos1--;
	if(pos1==-1){ pos1 = totalSlides1-1; }
	$('#slider-wrap1 ul#slider1').css('left', -(sliderWidth1*pos1));

	//*> optional
	countSlides1();
	pagination1();
}


/************
 SLIDE RIGHT
*************/
function slideRight1(){
	pos1++;
	if(pos1==totalSlides1){ pos1 = 0; }
	$('#slider-wrap1 ul#slider1').css('left', -(sliderWidth1*pos1));

	//*> optional
	countSlides1();
	pagination1();
}




/************************
 //*> OPTIONAL SETTINGS
************************/
function countSlides1(){
	$('#counter1').html(pos1+1 + ' / ' + totalSlides1);
}

function pagination1(){
	$('#pagination-wrap1 ul li').removeClass('active');
	$('#pagination-wrap1 ul li:eq('+pos1+')').addClass('active');
}