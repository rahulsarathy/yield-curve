window.onload = function () {
    
}

// $("#datepicker").datepicker();

var chart = new Chart(document.getElementById("chart"), {
    type: 'line',
    data: {
    labels: ["2019-01-01T13:03:00Z", "2019-01-01T14:12:00Z"],
    datasets: [{
      label: 'Daily Treasury Yield Curve Rates',
      data: [{
          t: "2019-01-15",
          y: 12
        },
        {
          t: "2019-02-25",
          y: 21
        },
        {
          t: "2019-03-25",
          y: 32
        }
      ],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
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