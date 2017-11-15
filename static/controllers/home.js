angular.module('Visualizer')
.controller('HomeController', function ($scope, Data) {
	$scope.data = [];
	$scope.series = [];
	$scope.datasetOverride = [{yAxisID: 'y-axis-1'}, {yAxisID: 'y-axis-2'}];
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
		$scope.series.push('Text Summary Sentiment');
		var textSummaryMap = {};
		data.forEach((point) => {
			textSummaryMap[new Date(point.posted_at)] = point.sentiment;
		});

		Data.getPricesForCoin('BTC').then((data) => {
			$scope.series.push('Price in USD');
			var priceMap = {};
			data.forEach((point) => {
				priceMap[new Date(point.created_at)] = point.price;
			});

			var labels = Object.keys(textSummaryMap).concat(Object.keys(priceMap));
			labels.sort(function(a, b){
				return b - a;
			});
			$scope.labels = labels;

			var textSummaryData = [];
			var priceData = [];
			labels.forEach((date) => {
				textSummaryData.push(!!textSummaryMap[date] ? textSummaryMap[date] : null);
				priceData.push(!!priceMap[date] ? priceMap[date] : null);
			});
			$scope.data.push(textSummaryData);
			$scope.data.push(priceData);
		});
	});

	
});
