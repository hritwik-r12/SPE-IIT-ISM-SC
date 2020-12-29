//current position
var pos5 = 0;
//number of slides
var totalSlides5 = $('#slider-wrap5 ul li').length;
//get the slide width
var sliderWidth5 = $('#slider-wrap5').width();


$(document).ready(function(){


	/*****************
	 BUILD THE SLIDER
	*****************/
	//set width to be 'x' times the number of slides
	$('#slider-wrap5 ul#slider5').width(sliderWidth5*totalSlides5);

    //next slide
	$('#next5').click(function(){
		slideRight5();
	});

	//previous slide
	$('#previous5').click(function(){
		slideLeft5();
	});



	/*************************
	 //*> OPTIONAL SETTINGS
	************************/
	//automatic slider
	var autoSlider5 = setInterval(slideRight5, 3000);

	//for each slide
	$.each($('#slider-wrap5 ul li'), function() {
	   //set its color
	   var c5 = $(this).attr("data-color");
	   $(this).css("background",c5);

	   //create a pagination
	   var li5 = document.createElement('li');
	   $('#pagination-wrap5 ul').append(li5);
	});

	//counter
	countSlides5();

	//pagination
	pagination5();

	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap5').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider5); },
	  function(){ $(this).removeClass('active'); autoSlider5 = setInterval(slideRight5, 3000); }
	);



});//DOCUMENT READY



/***********
 SLIDE LEFT
************/
function slideLeft5(){
	pos5--;
	if(pos5==-1){ pos5 = totalSlides5-1; }
	$('#slider-wrap5 ul#slider5').css('left', -(sliderWidth5*pos5));

	//*> optional
	countSlides5();
	pagination5();
}


/************
 SLIDE RIGHT
*************/
function slideRight5(){
	pos5++;
	if(pos5==totalSlides5){ pos5 = 0; }
	$('#slider-wrap5 ul#slider5').css('left', -(sliderWidth5*pos5));

	//*> optional
	countSlides5();
	pagination5();
}




/************************
 //*> OPTIONAL SETTINGS
************************/
function countSlides5(){
	$('#counter5').html(pos5+1 + ' / ' + totalSlides5);
}

function pagination5(){
	$('#pagination-wrap5 ul li').removeClass('active');
	$('#pagination-wrap5 ul li:eq('+pos5+')').addClass('active');
}