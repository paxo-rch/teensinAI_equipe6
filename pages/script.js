Highcharts.chart('container', {
  chart: {
    type: 'spline'
  },
  title: {
    text: 'Prévision de Production'
  },
  subtitle: {
    text: 'Source: www.services-rte.com/'
  },
  xAxis: {
    categories: ['00h', '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', '11h', '12h', '13h',
      '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h', '22h', '23h']
  },
  yAxis: {
    title: {
      text: 'Puissance (MW)'
    },
    labels: {
      formatter: function () {
        return this.value + 'MW';
      }
    }
  },
  tooltip: {
    crosshairs: true,
    shared: true
  },
  plotOptions: {
    spline: {
      marker: {
        radius: 4,
        lineColor: '#666666',
        lineWidth: 1
      }
    }
  },
  series: [{
    name: 'Énergie Solaire',
    marker: {
      symbol: 'circle'
    },
    data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 308, 1877, 3794, 5199, 6096, {
      y: 6399,
      marker: {
        symbol: 'url(https://www.highcharts.com/samples/graphics/sun.png)'
      }
    }, 5985, 4944, 3288, 1316, 85, 0, 0, 0]

  }, {
    name: 'Énergie Éolienne',
    marker: {
      symbol: 'diamond'
    },
    data: [1720, 1804, 1890, 1976, 1934, 1892, 1850, 1762, 1673, 1586, 1400, 1215, 1030, 928, 827, 727, 869, 1011, 1153, 1344, 1535, 1726, 1981,{
      y: 2236,
      marker: {
        symbol: 'url(https://www.highcharts.com/samples/graphics/sun.png)'
                   
      }
    },]
  }]
});