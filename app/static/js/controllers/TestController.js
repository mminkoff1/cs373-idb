app.controller('TestController', function($scope, $http) {
	    $scope.tests = null;

        $scope.runUnittests = function () {
            $http.get('/test').success(function(data) {
                $scope.tests = data
            });
        $scope.tests = "Hello";    
}
});