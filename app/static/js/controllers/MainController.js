app.controller('MainController', ['$scope', function($scope) {
	$scope.games = [ 
	  { 
	    title: 'Halo 5', 
	    publisher: 'MOVE', 
	    theme: 'MOVE, Inc.', 
	    published_year: 0.99,
	    avg_score: 93 
	  },
	  
	  { 
	    title: 'Halo 6', 
	    publisher: 'MOVE', 
	    theme: 'MOVE, Inc.', 
	    published_year: 0.99,
	    avg_score: 93 
	  }
	];
	$scope.greeting = "Hello World!"; 
}]);