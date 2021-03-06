app.directive('navBar',function(){
  return {
    // restict: 'E',
    // scope: {},
    // templateUrl: 'js/directives/navBar.html'
    template: "  <nav class="navbar navbar-default navbar-inner" style="margin-bottom: 0px; z-index: 9999;">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse-ex"> <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
            <a class="navbar-brand" href="/">Game Lookup</a>
      </div>
      <div class="navbar-collapse collapse" id="navbar-collapse-ex">
        <ul class="nav navbar-nav">
          <li><a href="/genre">Genre</a></li>
          <li><a href="/publisher">Publisher</a></li>
          <li><a href="/games">Games</a></li>
          <li><a href="/about">About us</a></li>
        </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#search">Search</a></li>
      </ul>
      </div>
    </div>
  </nav>
"
  };
});