

/*app.controller('AboutController', ['$scope', 'AboutFactory',
 function($scope, AboutFactory) {
        $scope.tests        = 'waiting';
        $scope.hello = "hello world";

        //$scope.runUnittests = function () {
        //    $http.get('/test').success(function(data) {
        //        $scope.tests = 'waiting'
        //};
        //)};
}]);*/
app.controller('AboutController', function($scope) {
        $scope.tests = 'waiting';
        $scope.hello = "hello world";
        $scope.print = function() {
        	return $scope.hello;
        };
});
