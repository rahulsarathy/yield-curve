var data = [{

}]

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

function getBondData(date)
{
$.ajax({
  url: 'api/v1/bond_yield/' + date,
  success: function(data) {
    console.log(data)

  }
});
}

function initChart() {
  var chart = new Chart(document.getElementById("chart"), {
    type: 'line',
    data: {
      labels: ["2019-01-01T13:03:00Z", "2019-01-01T14:12:00Z"],
      datasets: [{
        label: 'Daily Treasury Yield Curve Rates',
        data: [{
          t: "2019-01-15",
          y: 12
        }, {
          t: "2019-02-25",
          y: 21
        }, {
          t: "2019-03-25",
          y: 32
        }],
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
            unit: 'day'
          }
        }]
      }
    }
  });
}

