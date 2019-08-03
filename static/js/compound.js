var compound_chart;

window.onload = function() {
  compoundChart();
}

$(function() {
  $('#compound_form').on('submit', function(e) {
    e.preventDefault();  // prevent form from submitting
    var data = $("#compound_form :input").serializeArray();
    var json = {};
    for (var i = 0; i < 3; i++) {
      // console.log(form_elem);
      json[data[i].name] = data[i].value;
    }
    
    $.ajax({
        url: '/api/v1/compound_calculator/',
        data: json,
        success: function(data) {
          deposits = [
            data['1 year']['Deposits'],
            data['10 years']['Deposits'],
            data['30 years']['Deposits']
          ];
          returns = [
            data['1 year']['Return'],
            data['10 years']['Return'],
            data['30 years']['Return']
          ];
          addData(compound_chart, deposits, returns);
        }
    });
    console.log(json);
    console.log(data);
  });
});

function addData(chart, deposits, returns) {
  chart.data.datasets[0].data = deposits;
  chart.data.datasets[1].data = returns;
  chart.update();
}

function compoundChart() {
  compound_chart = new Chart(document.getElementById('compound_chart'), {
    type: 'bar',
    data: {
      labels: ['1 year', '10 years', '30 years'],
      datasets: [{
        label: 'Deposits',
        data: null,  // Will be added through addData()
          backgroundColor: [
            // Slatish blue
            'rgba(18, 95, 163, 0.2)',
            'rgba(18, 95, 163, 0.2)',
            'rgba(18, 95, 163, 0.2)'
          ],
          borderColor: [
            // Slatish blue
            'rgba(18, 95, 163, 1)',
            'rgba(18, 95, 163, 1)',
            'rgba(18, 95, 163, 1)'
          ],
          borderWidth: 2
        },
        {
          label: 'Return',
          data: null,  // Will be added through addData()
          backgroundColor: [
            // Tarragon
            'rgba(18, 163, 49, 0.2)',
            'rgba(18, 163, 49, 0.2)',
            'rgba(18, 163, 49, 0.2)'
          ],
          borderColor: [
            // Tarragon
            'rgba(18, 163, 49, 1)',
            'rgba(18, 163, 49, 1)',
            'rgba(18, 163, 49, 1)'
          ],
          borderWidth: 2
        }]
      },
      options: {
        title: {
          display: true,
          text: 'Investment Return Over Time'
        },
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }],
          xAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
  });

  // 750x750
  compound_chart.canvas.parentNode.style.height = '750px';
  compound_chart.canvas.parentNode.style.width = '750px';
}
