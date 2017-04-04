app.directive('appInfo',function(){
  return {
    restict: 'E',
    scope: {
      info: '='
    },
    
    templateUrl: '../../templates/gameRow.html'
  };
});