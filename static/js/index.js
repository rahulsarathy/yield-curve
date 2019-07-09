var chart_data = [{
  t: "2019-01-15",
  y: 12
}, {
  t: "2019-02-25",
  y: 21
}, {
  t: "2019-03-25",
  y: 32
}]

var yield_curve;

window.onload = function() {

  initDatePicker()
  initChart()



}

function initDatePicker() {
  var today = new Date();
  $(function() {
    $("#datepicker").datepicker({
      maxDate: '0',
      onSelect: function(date, datepicker) {
        var year = date.substring(6, 10)
        var day = date.substring(3, 5)
        var month = date.substring(0, 2)
        getBondData(year + month + day)
      }
    });
  });
}

function getBondData(date) {
  $.ajax({
      url: 'api/v1/bond_yield/' + date,
      success: function(data) {
        console.log(data)
        year = parseInt(date.substring(0, 4))
        month = parseInt(date.substring(4, 6))
        day = parseInt(date.substring(6, 8))
        var today = new Date(year, month, day)
        var proper_dates = {
          one_month: new Date(year, month + 1, day),
          two_month: new Date(year, month + 2, day),
          three_month: new Date(year, month + 3, day),
          six_month: new Date(year, month + 6, day),
          one_year: new Date(year + 1, month, day),
          two_year: new Date(year + 2, month, day),
          three_year: new Date(year + 3, month, day),
          five_year: new Date(year + 5, month, day),
          seven_year: new Date(year + 7, month, day),
          ten_year: new Date(year + 10, month, day),
          twenty_year: new Date(year + 20, month, day),
          thirty_year: new Date(year + 30, month, day)
        }


        var new_data = ['one_month', 'two_month', 'three_month', 'six_month', 'one_year', 'three_year',
          'five_year', 'seven_year', 'ten_year', 'twenty_year', 'thirty_year']

        var to_add = []

        new_data.forEach(function(element) {
          var wanted_date = proper_dates[element]
          var date_string = wanted_date.getFullYear() + '-' + (wanted_date.getMonth() + 1) + '-' + wanted_date.getDate();
          to_add.push(
          {
            t: date_string,
            y: data[element]
          })
        });

        addData(yield_curve, to_add)

      }

      // addData(yield_curve, {
      //   t: date_string,
      //   y: 10
      // })
  });
}

function addData(chart, data) {
  chart.data.datasets.forEach((dataset) => {
    dataset.data = data
  });
  chart.update()
}

function initChart() {
  yield_curve = new Chart(document.getElementById("chart"), {
    type: 'line',
    data: {
      datasets: [{
        label: 'Daily Treasury Yield Curve Rates',
        data: chart_data,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
        ],
        borderColor: [
          'rgba(255,99,132,1)',
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            unit: 'year'
          }
        }]
      }
    }
  });

  yield_curve.canvas.parentNode.style.height = '1000px';
  yield_curve.canvas.parentNode.style.width = '1000px';

}