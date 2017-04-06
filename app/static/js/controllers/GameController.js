app.controller('GameController', ['$scope', 'GameFactory',
 function($scope, GameFactory) {

	$scope.sortType = 'name';
	$scope.sortReverse = false;

	// GameFactory.fetch().success(function(data) {
	// 	$scope.games = data["games_list"];
	// }); 

}]);