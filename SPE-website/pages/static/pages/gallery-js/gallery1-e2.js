//current position
var pos2 = 0;
//number of slides
var totalSlides2 = $('#slider-wrap2 ul li').length;
//get the slide width
var sliderWidth2 = $('#slider-wrap2').width();


$(document).ready(function(){


	/*****************
	 BUILD THE SLIDER
	*****************/
	//set width to be 'x' times the number of slides
	$('#slider-wrap2 ul#slider2').width(sliderWidth2*totalSlides2);

    //next slide
	$('#next2').click(function(){
		slideRight2();
	});

	//previous slide
	$('#previous2').click(function(){
		slideLeft2();
	});



	/*************************
	 //*> OPTIONAL SETTINGS
	************************/
	//automatic slider
	var autoSlider2 = setInterval(slideRight2, 3000);

	//for each slide
	$.each($('#slider-wrap2 ul li'), function() {
	   //set its color
	   var c2 = $(this).attr("data-color");
	   $(this).css("background",c2);

	   //create a pagination
	   var li2 = document.createElement('li');
	   $('#pagination-wrap2 ul').append(li2);
	});

	//counter
	countSlides2();

	//pagination
	pagination2();

	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap2').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider2); },
	  function(){ $(this).removeClass('active'); autoSlider2 = setInterval(slideRight2, 3000); }
	);



});//DOCUMENT READY



/***********
 SLIDE LEFT
************/
function slideLeft2(){
	pos2--;
	if(pos2==-1){ pos2 = totalSlides2-1; }
	$('#slider-wrap2 ul#slider2').css('left', -(sliderWidth2*pos2));

	//*> optional
	countSlides2();
	pagination2();
}


/************
 SLIDE RIGHT
*************/
function slideRight2(){
	pos2++;
	if(pos2==totalSlides2){ pos2 = 0; }
	$('#slider-wrap2 ul#slider2').css('left', -(sliderWidth2*pos2));

	//*> optional
	countSlides2();
	pagination2();
}




/************************
 //*> OPTIONAL SETTINGS
************************/
function countSlides2(){
	$('#counter2').html(pos2+1 + ' / ' + totalSlides2);
}

function pagination2(){
	$('#pagination-wrap2 ul li').removeClass('active');
	$('#pagination-wrap2 ul li:eq('+pos2+')').addClass('active');
}