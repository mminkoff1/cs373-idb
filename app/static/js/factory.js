app.factory('GameFactory', function($http) { 
  return {
    fetch: function () {
      return $http.get('/api/games');
     } 
    // },
    // fetchAt: function (x) {
    //   return $http.get('/api/cuisines/' + x);
    // },
    // fetchRecipes: function (x) {
    //   return $http.get('/api/cuisine/' + x + '/recipes/');
    // },
  };
});