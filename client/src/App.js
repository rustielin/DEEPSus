import React, { Component } from 'react';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';

// import electricity from './json/Activities and Recreation Center_Electricity_Demand.json';
// import water from './json/Activities and Recreation Center_ChilledWater_Demand.json';
// import wifi from './json/ARC_WiFi_TotalCount.json';

var electricity = null;
var water = null;
var wifi = null;

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

const API_ENDPOINT = 'https://hackdavis.appspot.com/api/'
// const API_ENDPOINT = 'http://localhost:8080/api/'

const axios = require('axios')

//-----------------REST API--------------------

// gets type and attribute and callback
const getARC = async (t, a) => {
  try {
    return await axios.get(API_ENDPOINT + 'getARC', {
      params: {
        type: t,
        attribute: a
      },
      headers: {
        'Access-Control-Request-Headers': ['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers'],
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type'
      }
    })
  } catch (error) {
    // console.error(error)
    alert(error)
  }
}


let dps = [];
let dps2 = [];
let dps3 = [];

// console.log(electricity['Timestamp']);
class App extends Component {
  constructor() {
    super();

    //-----------------GET DATA--------------------

    var promise_1 = getARC('Electricity', 'Demand');
    var promise_2 = getARC('ChilledWater', 'Demand');
    var promise_3 = getARC('WiFi', 'TotalCount');
    
    Promise.all([promise_1, promise_2, promise_3]).then(function(values) {
      electricity = values[0].data;
      console.log(electricity);
      water = values[1].data;
      console.log(water);
      wifi = values[2].data;
      console.log(wifi);

      //-----------------PROCEED--------------------

      console.log("PLOTTTINGGG");
      for (let i = 0; i < Object.keys(water['Points']).length; i++) {
        dps.push({
          x : new Date(electricity['Points'][i]['x']),
          y: electricity['Points'][i]['y'] / electricity['Normalization']
        });
  
        dps2.push({
          x : new Date(wifi['Points'][i]['x']),
          y: wifi['Points'][i]['y'] / wifi['Normalization']
        });
  
        dps3.push({
          x : new Date(water['Points'][i]['x']),
          y: water['Points'][i]['y'] / water['Normalization']
        });
      }

    });
    
  }

  render() {
   
    const options = {
      animationEnabled: true,	
      title:{
        text: "Electricity Usage Over Time"
      },
      theme: "light2",
      axisY : {
        title: "Usage Percentage (%)",
        includeZero: false,
        minimum: 0
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
      }
    ]
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
