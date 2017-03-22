$(document).ready(function(){
  $('#myModal').modal('show');

  $(function () {
      $('a[href="#search"]').on('click', function(event) {
	  event.preventDefault();
	  $('#search').addClass('open');
	  $('#search > form > input[type="search"]').focus();
      });
      
      $('#search, #search button.close').on('click keyup', function(event) {
	  if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
	      $(this).removeClass('open');
	  }
      });

      $('form').submit(function(event) {
          var searchstring = $('searchfield');
   	  searchstring.focus();
 	  alert(searchstring.val());
      });
  });
});
