app.controller('GameController', ['$scope', 'GameFactory',
 function($scope, GameFactory) {

	$scope.sortType = 'name';
	$scope.sortReverse = false;

	// GameFactory.fetch().success(function(data) {
	// 	$scope.games = data["games_list"];
	// }); 

}]);

app.controller('PublisherController', ['$scope', 'PublisherFactory',
 function($scope, PublisherFactory) {

	$scope.sortType = 'name';
	$scope.sortReverse = false;

	// GameFactory.fetch().success(function(data) {
	// 	$scope.games = data["games_list"];
	// }); 

}]);

app.controller('CharacterController', ['$scope', 'CharacterFactory',
 function($scope, CharacterFactory) {

	$scope.sortType = 'name';
	$scope.sortReverse = false;

	// GameFactory.fetch().success(function(data) {
	// 	$scope.games = data["games_list"];
	// }); 

}]);