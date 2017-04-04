app.controller('GameController', ['$scope', function($scope) {
	$scope.games = [ 
	  { 
	    title: 'Apple', 
	    publisher: 'C', 
	    theme: 'D', 
	    published_year: 2,
	    avg_score: 3 
	  },

	  { 
	    title: 'Bravo', 
	    publisher: 'A', 
	    theme: 'B.', 
	    published_year: 1,
	    avg_score: 4 
	  },
	    { 
	    title: 'Charlie', 
	    publisher: 'Z', 
	    theme: 'Y.', 
	    published_year: 10,
	    avg_score: 40 
	  },
	    { 
	    title: 'Delta', 
	    publisher: 'W', 
	    theme: 'X.', 
	    published_year: 500,
	    avg_score: 19 
	  }
	];
	$scope.sortType = 'name';
	$scope.sortReverse = false;

}]);