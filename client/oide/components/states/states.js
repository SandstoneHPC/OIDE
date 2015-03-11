'use strict';

angular.module('oide.states', [])
.factory('StateService', ['$http', '$log', function($http,$log) {
  var state = {'state': {}};
  var storeState = function () {
    $http({
      url: '/a/state',
      method: 'POST',
      params: {
        _xsrf: getCookie('_xsrf')
      },
      data: JSON.stringify(state.state)
    })
    .success(function (data, status, headers, config) {
      $log.debug('Stored state for user.');
    })
    .error(function (data, status, headers, config) {
      $log.error('Failed to store state for user.');
    });
  };
  var getState = function () {
    return $http
    .get('/a/state')
    .success(function (data, status, headers, config) {
      $log.debug('Retrieved state for user: ', data);
      return data;
    })
    .error(function (data, status, headers, config) {
      $log.error('Failed to retrieve state for user.');
    });
  };
  var initializeState = function () {
    return $http
    .get('/a/state')
    .success(function (data, status, headers, config) {
      $log.debug('Retrieved state for user: ', data);
      state.state = data;
    })
    .error(function (data, status, headers, config) {
      $log.error('Failed to retrieve state for user.');
    });
  };
  var statePromise = initializeState();
  return {
    state: state.state,
    // state: function () {
    //   return state.state;
    // },
    statePromise: statePromise,
    storeState: function () {
      storeState();
    },
    getState: function () {
      return state.state;
    }
    // getState: function () {
    //   getState();
    // }
  };
}]);
