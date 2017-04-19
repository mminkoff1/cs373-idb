app.controller('AboutController', function($scope, $http) {
        $scope.tests = 'Running tests...';
        $scope.runUnittests = function () {
            $http.get('/test').success(function(data) {
                $scope.tests = data
            });
        };
});
