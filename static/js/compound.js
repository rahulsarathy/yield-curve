var compound_chart;

window.onload = function() {
  compoundChart();
}

$(function() {
  $('#compound_form').on('submit', function(e) {
    e.preventDefault();  // prevent form from submitting
    var data = $("#compound_form :input").serializeArray();

    // Collect parameters for compound calculation 
    var json = {};
    for (var i = 0; i < 3; i++) {
      json[data[i].name] = data[i].value;
    }
    
    $.ajax({
      url: '/api/v1/compound_calculator/',
      data: json,
      success: function(data) {
        var deposits = [];
        var returns = [];
        var labels = [];
        for (var i = 0; i <= 30; i++) {
          var label = i + ' years';
          labels.push(i);
          deposits.push(data[label]['Deposits']);
          returns.push(data[label]['Return']);
        }
        addData(compound_chart, labels, deposits, returns);
      }
    });
  });
});

function addData(chart, labels, deposits, returns) {
  chart.data.labels = labels;
  chart.data.datasets[0].data = deposits;
  chart.data.datasets[1].data = returns;
  chart.update();
}

function compoundChart() {
  compound_chart = new Chart(document.getElementById('compound_chart'), {
    type: 'line',
    data: {
      labels: null, // Will be added through addData()
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
            scaleLabel: {
              display: true,
              labelString: 'Value'
            },
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }],
          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Years'
            },
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
