app.factory('thronesFactory', [function ($http, $q) {
  var service = {};
  var baseUrl = 'http://www.youknownothing.fyi/api/houses';
  
  this.getData = function() {
    return $http.get(baseURL);
  };
  // service.callAPI = function () {
  //   var deferred = $q.defer();
  //   $http({
  //     method: 'JSONP',
  //     url: baseURL
  //   }).success(function (data) {
  //     deferred.resolve(data);
  //   }).error(function () {
  //     deferred.reject('There was an error');
  //   })

  //   return deferred.promise;
  // }

  // return service;
});