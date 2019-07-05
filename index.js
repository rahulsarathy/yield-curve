

window.onload = function () {
    
}

new Chart(document.getElementById("chart"), {
  type: 'line',
  data: {
    labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
    datasets: [{ 
        data: [86,114,106,106,107,111,133,221,783,2478],
        label: "Yield Curve",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'US Treasury Yield Curve'
    }
  }
});

var chart2 = new Chart(document.getElementById("chart2"), {
    type: 'line',
    data: {
    labels: ["2019-01-01T13:03:00Z", "2019-01-01T13:02:00Z", "2019-01-01T14:12:00Z"],
    datasets: [{
      label: 'Demo',
      data: [{
          t: "2019-01-15T13:03:00Z",
          y: 12
        },
        {
          t: "2019-02-25T13:02:00Z",
          y: 21
        },
        {
          t: "2019-03-25T14:12:00Z",
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