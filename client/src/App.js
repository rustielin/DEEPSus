import React, { Component } from 'react';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';

import electricity from './json/Activities and Recreation Center_Electricity_Demand.json';
import steam from './json/Activities and Recreation Center_Steam_Demand.json';
import water from './json/Activities and Recreation Center_ChilledWater_Demand.json';
import wifi from './json/ARC_WiFi_TotalCount.json';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;
const axios = require('axios')


const data = [electricity, steam, water, wifi];
console.log(data);
const API_ENDPOINT = 'https://hackdavis.appspot.com/api/';

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

// console.log(electricity['Timestamp']);
class App extends Component {
  createGraph(freq, type) {
    let dps = [];
    console.log(Object.keys(data[type]['Points']).length);
    for (let i = 0; i < Object.keys(data[type]['Points']).length; i+=15) {
      dps.push({
        x : new Date(data[type]['Points'][i]['x']),
        y: data[type]['Points'][i]['y'] / data[type]['Normalization']
      });
    }
    return dps;
  }

  constructor(props) {
    super(props);
    this.state = {
      sampleFreq : 15,
      options : {
        animationEnabled: true,
        zoomEnabled: true,
        title:{
          text: "Usage Over Time"
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
          dataPoints: this.createGraph(15, 0),
        },
        {
          type: "area",
          name: "Steam",
          showInLegend: true,
          dataPoints: this.createGraph(15, 1),
        },
        {
          type: "area",
          name: "Chilled Water",
          showInLegend: true,
          dataPoints: this.createGraph(15, 2),
        },
        {
          type: "area",
          name: "WiFi",
          showInLegend: true,
          dataPoints: this.createGraph(15, 3),
        }],
        legend: {
            cursor: "pointer", 
            itemclick: (e) => {
            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                e.dataSeries.visible = false;
            } else {
                e.dataSeries.visible = true;
            }
  
            e.chart.render();
          }
        }
      }
    };

    // for (let i = 0; i < 3; i++) {
    //   this.createGraph(this.state.sampleFreq, i);
    // }
    // this.changeState = this.changeState.bind(this);
  }

  render() {

    console.log("RENDERED");
    return (
      <div>
        <CanvasJSChart options = {this.state.options} 
          /* onRef={ref => this.chart = ref} */
        />
        {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
      </div>
      );
  }

  componentDidMount() {
    //-----------------GET DATA--------------------

    var promise_1 = getARC('Electricity', 'Demand');
    var promise_2 = getARC('ChilledWater', 'Demand');
    var promise_3 = getARC('WiFi', 'TotalCount');

    var currentComponent = this;

    // setInterval(()=> {this.setState(this.state); console.log(dps);}, 5000);


    // preserve value of this via arrow function
    Promise.all([promise_1, promise_2, promise_3]).then((values) => {
      data[0] = values[0].data;
      data[1] = values[1].data;
      data[2] = values[2].data;

      console.log(data);

      //-----------------PROCEED--------------------

      console.log("PLOTTTINGGG");

      // for (let i = 0; i < 3; i++) {
      //   this.createGraph(this.state.sampleFreq, i);
      // }

      const pts = [0, 1, 2].map((x) => this.createGraph(this.state.sampleFreq, x));

      console.log(pts);
      // for (let i = 0; i < Object.keys(water['Points']).length; i++) {
      //   dps.push({
      //     x : new Date(a['Points'][i]['x']),
      //     y: electricity['Points'][i]['y'] / electricity['Normalization']
      //   });

      //   dps2.push({
      //     x : new Date(wifi['Points'][i]['x']),
      //     y: wifi['Points'][i]['y'] / wifi['Normalization']
      //   });

      //   dps3.push({
      //     x : new Date(water['Points'][i]['x']),
      //     y: water['Points'][i]['y'] / water['Normalization']
      //   });
      // }
      
      currentComponent.setState({
        options: {
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
              dataPoints: pts[0]
            },
            {
              type: "area",
              name: "WiFi",
              showInLegend: true,
              dataPoints: pts[1]
            },
            {
              type: "area",
              name: "Steam",
              showInLegend: true,
              dataPoints: pts[2]
            },
            {
              type: "area",
              name: "WiFi",
              showInLegend: true,
              dataPoints: this.createGraph(15, 3)
            }
          ]
        }
      });
      
    });
  }
}

export default App;
