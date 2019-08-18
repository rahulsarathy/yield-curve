var taxes_chart;

window.onload = function() {
  taxesChart();
}

$(function() {
  $('#taxes_form').on('submit', function(e) {
    e.preventDefault();  // Prevent form from submitting.
    var data = $('#taxes_form :input').serializeArray();
    request = {
      'income': data[0].value,
      'filing_status': data[1].value,
      'state': data[2].value,
    };
    // console.log(data);
    $.ajax({
      url: '/api/v1/taxes/',
      data: request,
      success: function(response) {
        addData(taxes_chart, response['After Tax Income'], response['Federal Taxes'],
        response['State Taxes']);
      }
    });
  });
});

function addData(chart, income, fed_tax, state_tax) {
  // Income must be the first element, followed by taxes.
  chart.data.labels = ['After Tax Income', 'Federal Taxes', 'State Taxes'];
  chart.data.datasets[0].data = [income, fed_tax, state_tax];
  chart.update();
}

function taxesChart() {
  taxes_chart = new Chart(document.getElementById('taxes_chart'), {
    type: 'doughnut',
    data: {
      labels: null,  // Will be added through addData()
      datasets: [{
        label: 'Taxes',
        data: null,  // Will be added through addData()
        backgroundColor: [
          'rgba(18, 163, 49, 0.4)',
          'rgba(255, 99, 132, 0.7)',
          'rgba(255, 99, 132, 0.4)',
        ],
      }]
    },
    options: {
    	responsive: true,
    	legend: {
    		position: 'top',
    	},
    	animation: {
    		animateScale: true,
    		animateRotate: true
    	}
    }
  });
  // taxes_chart.canvas.parentNode.style.height = '750px';
  // taxes_chart.canvas.parentNode.style.width = '750px';
}
