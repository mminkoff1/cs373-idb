mainApp.controller('AboutCtrl',
    ['$scope', '$http', 'GithubFetchFactory', 'IssueFetchFactory', 'MetadataFetchFactory',
    function($scope, $http, GithubFetchFactory, IssueFetchFactory, MetadataFetchFactory) {
        stats               = {issues:0, tests:0, commits:0};
        refineData          = {};
        totalCommit         = 0;

        GithubFetchFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                author = data[i]['author']
                refineData[author.login] = {};
                refineData[author.login].avatar_url    = author.avatar_url;
                refineData[author.login].url           = author.html_url;
                refineData[author.login].contributions = data[i].total;
                refineData[author.login].issues        = 0;
                stats.commits   += data[i].total;
            }
        });

        IssueFetchFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                refineData[data[i].user.login].issues += 1;
                stats.issues   += 1;
            }
        });

        $scope.members      = MetadataFetchFactory.fetchMember();
        for(var i = 0; i < $scope.members.length; i++) {
            stats.tests     += $scope.members[i].tests;
        }

        $scope.tools        = MetadataFetchFactory.fetchTool();
        $scope.dataUsed     = MetadataFetchFactory.fetchAPI();
        $scope.information  = MetadataFetchFactory.fetchInformation();
        $scope.sites        = MetadataFetchFactory.fetchSite();
        $scope.github       = refineData;
        $scope.stats        = stats;
        $scope.tests        = null;

        $scope.runUnittests = function () {
            $http.get('/test').success(function(data) {
                $scope.tests = data
            });
        }
}]);