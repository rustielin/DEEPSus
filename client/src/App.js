import React, { Component } from 'react';
import './App.css';
import CanvasJSReact from './canvasjs/canvasjs.react';
import { Parallax, ParallaxProvider } from 'react-scroll-parallax';

import electricity from './json/Activities and Recreation Center_Electricity_Demand.json';
import steam from './json/Activities and Recreation Center_Steam_Demand.json';
import water from './json/Activities and Recreation Center_ChilledWater_Demand.json';
import wifi from './json/ARC_WiFi_TotalCount.json';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

const data = [electricity, steam, water, wifi];

// console.log(electricity['Timestamp']);
class App extends Component {
  createGraph(freq, type) {
    let dps = [];
    for (let i = 0; i < Object.keys(data[type]['Points']).length; i+=15) {
      dps.push({
        x : new Date(data[type]['Points'][i]['x']),
        y: data[type]['Points'][i]['y'] / data[type]['Normalization']
      });
    }
    return dps;
  }

  // changeState(){
  //   if(this.state.animationClass === 'test'){
  //     this.setState({
  //       animationClass: 'test paused'
  //     });
  //   }else{
  //     this.setState({
  //       animationClass: 'test'
  //     });
  //   }
  // }

  constructor(props) {
    super(props);
    this.state = {
      sampleFreq : 15,
    };
    for (let i = 0; i < 3; i++) {
      this.createGraph(this.state.sampleFreq, i);
    }

    // this.changeState = this.changeState.bind(this);
  }

  render() {
    const options = {
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
  
  return (
    <ParallaxProvider>
      <Parallax>
        <div className = "test">
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options} 
            // onRef={ref => this.chart = ref}
          />
          {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
        </div>
      </Parallax>
    </ParallaxProvider>


  );
  }
}

export default App;
