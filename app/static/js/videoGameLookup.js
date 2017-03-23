$(document).ready(function(){
  $(function () {
      $('a[href="#search"]').on('click', function(event) {
	  event.preventDefault();
	  $('#search').addClass('open');
	  $('#search > form > input[type="search"]').focus();
          $('#but').fadeOut();
          $('#start-text').fadeOut();
      });
      
      $('#search, #search button.close').on('click keyup', function(event) {
	  if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
	      $(this).removeClass('open');
              $('#but').fadeIn();
	      $('#start-text').fadeIn();  
	  }
      });

      $('form').submit(function(event) {
          var searchstring = $('searchfield');
   	  searchstring.focus();
 	  alert(searchstring.val());
      });
  });

  $(function () {
    $("#but").click(function () {
      $('#search').trigger('click');
      $('#but').fadeOut();
      $('#start-text').fadeOut();
    });
  });

});
