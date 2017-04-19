app.controller('thronesController', [ '$scope','$http', function ($scope,$http) {

	// $scope.houses = [];
	// $scope.data = "Populating please wait...";
	// // var url = 'http://www.youknownothing.fyi/api/houses';
	// // $http.jsonp(url)
	// // 	.success(function (response) {
	// // 		$scope.houses = data;
	// // 		console.log($scope.houses)
	// // 	})
	// // 	.error(function (response) {
	// // 		console.log("error");
	// // 	});;

	// $http.get("http://www.youknownothing.fyi/api/houses")
 //    .then(function(response) {
 //        $scope.houses = angular.fromJson(response.data.houses);
 //        var map = {};
 //        for(var i = 0; i < $scope.houses.length; i++)
 //        {
 //        	if(map[$scope.houses[i].region] == null)
 //        	{
 //        		map[$scope.houses[i].region] = 1;
 //        	}
 //        	else
 //        	{
 //        		map[$scope.houses[i].region]++; 
 //        	}
 //        	//console.log($scope.houses[i]);
 //        }
 //        console.log(map);
 //        $scope.data = map;
 //    });



}])