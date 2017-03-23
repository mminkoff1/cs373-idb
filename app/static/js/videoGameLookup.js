$(document).ready(function(){
  $(function () {
      $('a[href="#search"]').on('click', function(event) {
	  event.preventDefault();
	  $('#search').addClass('open');
	  $('#search > form > input[type="search"]').focus();
          $('#but').hide();
          $('#start-text').hide();
      });
      
      $('#search, #search button.close').on('click keyup', function(event) {
	  if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
	      $(this).removeClass('open');
              $('#but').show();
	      $('#start-text').show();  
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
      $('#but').hide();
      $('#start-text').hide();
    });
  });

});
