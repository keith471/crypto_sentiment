angular.module('Visualizer')
.controller('HomeController', function ($scope, Data) {
	$scope.data = [];
	$scope.series = [];
	$scope.datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  	$scope.options = {
	    scales: {
			yAxes: [
				{
					id: 'y-axis-1',
					type: 'linear',
					display: true,
					position: 'left'
				},
				{
					id: 'y-axis-2',
					type: 'linear',
					display: true,
					position: 'right'
				}
			]
	    }
	};

	Data.getCoins().then((data) => {
		$scope.coinStr = data.map((coin) => coin.name).reduce((acc, val) => val);
	});
	Data.getTextSummariesForCoin('BTC').then((data) => {
		$scope.labels = data.map((point) => new Date(point.posted_at));
		$scope.data.push(data.map((point) => point.sentiment));
		$scope.series.push('Text Summary Sentiment');
		Data.getPricesForCoin('BTC').then((data) => {
			$scope.data.push(data.map((point) => point.sentiment));
			$scope.series.push('Price in USD');
		});
	});
});
