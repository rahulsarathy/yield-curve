var chart;

window.onload = function() {
  compoundChart();
}

function compoundChart() {
  chart = new Chart(document.getElementById("compound_chart"), {
    type: 'bar',
    data: {
      labels: ["1 year", "10 years", "30 years"],
      datasets: [{
        label: 'Deposits',
        data: [10, 19, 3],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(255, 99, 132, 1)',
            'rgba(255, 99, 132, 1)'
          ],
          borderWidth: 2
        },
        {
          label: 'Return',
          data: [15, 19, 3],
          backgroundColor: [
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 159, 64, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(255, 159, 64, 1)'
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
  chart.canvas.parentNode.style.height = '750px';
  chart.canvas.parentNode.style.width = '750px';
}
