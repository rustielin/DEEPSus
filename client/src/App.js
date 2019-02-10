import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

var dps = []; // dataPoints

var xVal = 0;
var yVal = 100; 
var updateInterval = 1000;
var dataLength = 20; // number of dataPoints visible at any point

class App extends Component {
  constructor() {
    super();
    this.updateChart = this.updateChart.bind(this);
  }

  componentDidMount() {
    this.updateChart(dataLength);
		setInterval(this.updateChart, updateInterval);
  }

  updateChart (count) {

    count = count || 1;
  
    for (var j = 0; j < count; j++) {
      yVal = yVal +  Math.round(5 + Math.random() *(-10));
      dps.push({
        x: xVal,
        y: yVal
      });
      xVal++;
    }
  
    if (dps.length > dataLength) {
      dps.shift();
    }
  
    this.chart.render();
  };

  render() {
    const options = {
      title :{
        text: "Dynamic Data"
      },
      axisY: {
        includeZero: true
      },      
      data: [{
        type: "line",
        dataPoints: dps
      }]
    };

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <CanvasJSChart options = {options}
            onRef = {ref => this.chart = ref}
          />
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
