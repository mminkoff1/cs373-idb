app.controller('thronesController', [ '$scope','$http', function ($scope,$http) {

	$scope.data = {};
	$scope.hello = "Hello World";
	var url = 'http://www.youknownothing.fyi/api/houses';
	$http({
    	method: 'JSONP',
    	url: url
		}).
	success(function(response) {
    	//$scope.data = response.houses[0];
    	console.log(response);
	}).
	error(function(response) {
		console.log(response);
    	$scope.data = "Oh my we have an error";
	});

}])