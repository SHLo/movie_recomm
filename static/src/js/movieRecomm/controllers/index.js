require('../services');

angular.module('MovieRecommApp')
    .controller(
	'MainCtrl',
	[
	    '$scope',
	    '$http',
	    '$uibModal',
	    'restSrv',
	    function ($scope, $http, $uibModal, restSrv) {
		$scope.listSizes = [
		    20,
		    60,
		    100,
		]
		$scope.historyMode = false;
		$scope.listMovies = listMovies;
		$scope.auth = window.auth;

		$scope.openRatingModal = function (item) {
		    console.log(item);
		    var modalInst = $uibModal.open(
			{
			    template: require('./modal.html'),
			    controller: 'ModalCtrl',
			    resolve: {
				item: function () {
				    return item;
				},
				historyMode: $scope.historyMode
			    }
			}
		    );
		    modalInst.result.then(function (rating) {
			if (typeof rating === 'undefined') return;
			$http.post(
			    '/rating/',
			    {item: item.id, rating: rating}
			)
			    .success(function (resp) {
				console.log('post suc:', resp);
			    })
			    .error(function (resp) {
				console.error('post err:', resp);
			    })
			;

			console.log(item.id, rating);
		    });
		};

		$scope.onModeChange = function () {
		    console.log('mode: ', $scope.historyMode);
		    if ($scope.historyMode) listHistory();
		    else listMovies(20);
		};

		$scope.listMovies(20);

		function listHistory () {
		    restSrv.listHistory()
			.success(function (resp) {
			    console.log(resp);
			    $scope.items = resp.items;
			})
		    ;
		}

		function listMovies (count) {
		    restSrv.listMovies(count)
			.success(function (resp) {
			    console.log(resp);
			    $scope.items = resp.items;
			})
		    ;
		}
	    }
	]
    )
    .controller('ModalCtrl',
	[
	    '$scope',
	    '$uibModalInstance',
	    'item',
	    'historyMode',
	    function ($scope, $uibModalInstance, item, historyMode) {
		$scope.item = item;
		$scope.auth = window.auth;
		$scope.historyMode = historyMode;
		$scope.rating = item.rating;
		$scope.ok = function () {
		    console.log('mode: ', historyMode);
		    console.log('rating: ', $scope.rating);
		    $uibModalInstance.close($scope.rating);
		};
		$scope.cancel = function () {
		    $uibModalInstance.dismiss('cancel');
		};
	    }
	]
    )
;
