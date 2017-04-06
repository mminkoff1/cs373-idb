var mainApp = angular.module('mainApp', [
	'ngRoute',
	'angularUtils.directives.dirPagination',
	]);
	
mainApp.config(['$routeProvider', '$locationProvider',
	function($routeProvider, $locationProvider) {
		$routeProvider.
		when('/', {
			templateUrl: '../static/partials/splash.html',
		}).
		when('/game', {
			templateUrl: '../static/partials/games.html'
		}).
		when('/genre', {
			templateUrl: '../static/partials/genre.html'
		}).
		when('/publisher', {
			templateUrl: '../static/partials/publisher.html'
		when('/about', {
			templateUrl: '../static/partials/about.html'
		}).
		otherwise({ redirectTo: '/' });

		// http://stackoverflow.com/questions/14771091/removing-the-fragment-identifier-from-angularjs-urls-symbol
		// Removing the fragment identifier from AngularJS urls (# symbol)
		if(window.history && window.history.pushState){
			$locationProvider.
			html5Mode({
				enabled: true,
				requireBase: false
			});
		}
	}]);
