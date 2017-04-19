app.controller('AboutController', function($scope, $http) {
        $scope.tests = 'Running tests...';
        $scope.runUnittests;

        $scope.runUnittests = function ($scope, $http) {
            $http.get('/test').success(function(data) {
                $scope.tests = data
            });
        };
});
