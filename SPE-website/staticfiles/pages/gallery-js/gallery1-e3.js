//current position
var pos3 = 0;
//number of slides
var totalSlides3 = $('#slider-wrap3 ul li').length;
//get the slide width
var sliderWidth3 = $('#slider-wrap3').width();


$(document).ready(function(){


	/*****************
	 BUILD THE SLIDER
	*****************/
	//set width to be 'x' times the number of slides
	$('#slider-wrap3 ul#slider3').width(sliderWidth3*totalSlides3);

    //next slide
	$('#next3').click(function(){
		slideRight3();
	});

	//previous slide
	$('#previous3').click(function(){
		slideLeft3();
	});



	/*************************
	 //*> OPTIONAL SETTINGS
	************************/
	//automatic slider
	var autoSlider3 = setInterval(slideRight3, 3000);

	//for each slide
	$.each($('#slider-wrap3 ul li'), function() {
	   //set its color
	   var c3 = $(this).attr("data-color");
	   $(this).css("background",c3);

	   //create a pagination
	   var li3 = document.createElement('li');
	   $('#pagination-wrap3 ul').append(li3);
	});

	//counter
	countSlides3();

	//pagination
	pagination3();

	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap3').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider3); },
	  function(){ $(this).removeClass('active'); autoSlider3 = setInterval(slideRight3, 3000); }
	);



});//DOCUMENT READY



/***********
 SLIDE LEFT
************/
function slideLeft3(){
	pos3--;
	if(pos3==-1){ pos3 = totalSlides3-1; }
	$('#slider-wrap3 ul#slider3').css('left', -(sliderWidth3*pos3));

	//*> optional
	countSlides3();
	pagination3();
}


/************
 SLIDE RIGHT
*************/
function slideRight3(){
	pos3++;
	if(pos3==totalSlides3){ pos3 = 0; }
	$('#slider-wrap3 ul#slider3').css('left', -(sliderWidth3*pos3));

	//*> optional
	countSlides3();
	pagination3();
}




/************************
 //*> OPTIONAL SETTINGS
************************/
function countSlides3(){
	$('#counter3').html(pos3+1 + ' / ' + totalSlides3);
}

function pagination3(){
	$('#pagination-wrap3 ul li').removeClass('active');
	$('#pagination-wrap3 ul li:eq('+pos3+')').addClass('active');
}