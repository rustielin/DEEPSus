import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';

import electricity from './json/Activities and Recreation Center_Electricity_Demand.json';
import water from './json/Activities and Recreation Center_ChilledWater_Demand.json';
import wifi from './json/ARC_WiFi_TotalCount.json';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

let dps = [];
let dps2 = [];
let dps3 = [];

console.log(electricity['Timestamp']);
class App extends Component {
  constructor() {
    super();
    for (let i = 0; i < Object.keys(electricity['Value']).length; i++) {
      dps.push({
        x : new Date(electricity['Timestamp'][i]),
        y: electricity['Value'][i]
      });

      dps2.push({
        x: new Date(wifi['Timestamp'][i]),
        y: wifi['Value'][i]
      });

      dps3.push({
        x: new Date(wifi['Timestamp'][i]),
        y: water['Value'][i]
      });
    }
  }

  render() {
   
    const options = {
      animationEnabled: true,	
      title:{
        text: "Electricity Usage Over Time"
      },
      theme: "light2",
      axisY : {
        title: "Electricity Usage (kWH)",
        includeZero: false
      },
      toolTip: {
        shared: true
      },
      data: [{
        type: "area",
        name: "Electricity",
        showInLegend: true,
        dataPoints: dps
      },
      {
        type: "area",
        name: "WiFi",
        showInLegend: true,
        dataPoints: dps2
      },
      {
        type: "area",
        name: "Steam",
        showInLegend: true,
        dataPoints: dps3


      }]
  }
  
  return (
  <div>
    <CanvasJSChart options = {options} 
      /* onRef={ref => this.chart = ref} */
    />
    {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
  </div>
  );
  }
}

export default App;
