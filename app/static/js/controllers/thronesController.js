app.controller('thronesController', [ '$scope','$http', function ($scope,$http) {

	$scope.data = {};
	$scope.hello = "Hello World";
	var url = 'http://www.youknownothing.fyi/api/houses';
	$http({
    	method: 'JSONP',
    	url: url
		}).
	success(function(status) {
    	$scope.data = status;
	}).
	error(function(status) {
    	$scope.data = "Oh my we have an error";
	});

}])