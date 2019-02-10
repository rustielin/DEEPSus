import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

var dps = []; // dataPoints
var dps2 = [];
var dps3 = [];
var xVal = 0;
var yVal = 100; 
var yVal2 = 100;
var yVal3 = 100;
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
      yVal = Math.round(5 + Math.random() *(-10));
      yVal2 = Math.round(5 + Math.random() *(-10));
      yVal3 = Math.round(5 + Math.random() *(-10));
      dps.push({
        x: xVal,
        y: yVal
      });
      dps2.push({
        x: xVal,
        y: yVal2
      });
      dps3.push({
        x: xVal,
        y: yVal3
      });
      xVal++;
    }
  
    if (dps.length > dataLength) {
      dps.shift();
    }
    if (dps2.length > dataLength) {
      dps2.shift();
    }
    if (dps3.length > dataLength) {
      dps3.shift();
    }
    this.chart.render();
    this.chart2.render();
    this.chart3.render();
  };

  render() {
    const options = {
      title :{
        text: "Electricity Usage"
      },
      axisX:{
        crosshair: {
          enabled: true,
          snapToDataPoint: true
        }
      },
      axisY: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      },
      axisY2: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      },
      height: 300,
      width: 800,
      data: [{
        markerColor: "red",
        lineColor: "red",
        type: "line",
        dataPoints: dps
      }]

    };
    const options2 = {
      title :{
        text: "Wifi Usage"
      },
      axisX:{
        crosshair: {
          enabled: true,
          snapToDataPoint: true
        }
      },
      axisY: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      }, 
      axisY2: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      },   
      height: 300,
      width: 800,
      data: [{
        markerColor: "purple",
        lineColor: "purple",
        type: "line",
        dataPoints: dps2
      }]
    };
    const options3 = {
      title :{
        text: "Chilled Water Usage"
      },
      axisX:{
        crosshair: {
          enabled: true,
          snapToDataPoint: true
        },
        title:"Seconds since start" 
      },
      axisY: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      }, 
      axisY2: {
        includeZero: true,
        crosshair: {
        enabled: true,
        snapToDataPoint: true
        }
      },  
      height: 300, 
      width: 800,
      data: [{
        type: "line",
        dataPoints: dps3
      }]
    };
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <CanvasJSChart options = {options} onRef = {ref => this.chart = ref}/>
          <CanvasJSChart options = {options2} onRef = {ref => this.chart2 = ref}/>
          <CanvasJSChart options = {options3} onRef = {ref => this.chart3 = ref}/>
        </header>
      </div>
    );
  }
}

export default App;
