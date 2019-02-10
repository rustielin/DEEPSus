import React, { Component } from 'react';
import CanvasJSReact from './canvasjs/canvasjs.react';
import { Parallax, ParallaxProvider } from 'react-scroll-parallax';

import electricity from './json/Activities-and-Recreation-Center_Electricity_Demand.json';
import steam from './json/Activities-and-Recreation-Center_Steam_Demand.json';
import water from './json/Activities-and-Recreation-Center_ChilledWater_Demand.json';
import wifi from './json/ARC_WiFi_TotalCount.json';

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

const data = [electricity, steam, water, wifi];
var dps1=[];
var dps2=[];
var dps3=[];
var dps4=[];
var i1=0;
var i2=0;
var i3=0;
var i4=0;
// console.log(electricity['Timestamp']);
class App extends Component {

  updateChart(count,type) {
    count = count || 1;
    for (var j = 0; j < count; j++) {
      if(type==0){
        dps1.push({
          x: new Date(data[type]['Points'][i1]['x']),
          y: data[type]['Points'][i1]['y']
        });
        i1+=1;
      }
      if(type==1){
        dps2.push({
          x: new Date(data[type]['Points'][i2]['x']),
          y: data[type]['Points'][i2]['y']
        });
        i2+=1;
      }
      if(type==2){
        dps3.push({
          x: new Date(data[type]['Points'][i3]['x']),
          y: data[type]['Points'][i3]['y']
        });
        i3+=1;
      }
      if(type==3){
        dps4.push({
          x: new Date(data[type]['Points'][i4]['x']),
          y: data[type]['Points'][i4]['y']
        });
        i4+=1;
      }
      if (dps1.length > 20) {
      dps1.shift();
      }
      if (dps2.length > 20) {
      dps2.shift();
      }
      if (dps3.length > 20) {
      dps3.shift();
      }
      if (dps4.length > 20) {
      dps4.shift();
      }
    }

    this.chart.render();
    if(type==0){
      this.chart1.render();
    }
    if(type==1){
      this.chart2.render();
    }
    if(type==2){
      this.chart3.render();
    }
    if(type==3){
      this.chart4.render();
    }

  };
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

    setInterval(() => {this.updateChart(10,0);}, 1000);
    setInterval(() => {this.updateChart(10,1);}, 1000);
    setInterval(() => {this.updateChart(10,2);}, 1000);
    setInterval(() => {this.updateChart(10,3);}, 1000);

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
      crosshair: {
        enabled: true,
        snapToDataPoint: true
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
    const options1 = {
      axisY : {
        title: "Power (kW)",
        includeZero: false,
        minimum: 0
      },
      toolTip: {
        shared: true
      },
      crosshair: {
        enabled: true,
        snapToDataPoint: true
      },
      data: [{
        type: "line",
        name: "Electricity",
        showInLegend: true,
        dataPoints: dps1
      }]
    }
    const options2 = {
      axisY : {
        title: "Rate of consumption (lbs/hour)",
        includeZero: false,
        minimum: 0
      },
      toolTip: {
        shared: true
      },
      crosshair: {
        enabled: true,
        snapToDataPoint: true
      },
      data: [{
        color: "lime",
        type: "line",
        name: "Steam",
        showInLegend: true,
        dataPoints: dps2
      }]
    }
    const options3 = {
      axisY : {
        title: "Weight (tons)",
        includeZero: false,
        minimum: 0
      },
      toolTip: {
        shared: true
      },
      crosshair: {
        enabled: true,
        snapToDataPoint: true
      },
      data: [{
        color: "red",
        type: "line",
        name: "Chilled Water",
        showInLegend: true,
        dataPoints: dps3
      }]
    }
    const options4 = {
      axisY : {
        title: "Number of Users",
        includeZero: false,
        minimum: 0
      },
      toolTip: {
        shared: true
      },
      crosshair: {
        enabled: true,
        snapToDataPoint: true
      },
      data: [{
        color: "teal",
        type: "line",
        name: "Wifi",
        showInLegend: true,
        dataPoints: dps4
      }]
    }
  return (
        <div className = "test">
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options} 
            onRef={ref => this.chart = ref}
          />
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options1} 
            onRef={ref => this.chart1 = ref}
          />
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options2} 
            onRef={ref => this.chart2 = ref}
          />
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options3} 
            onRef={ref => this.chart3 = ref}
          />
          <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options4} 
            onRef={ref => this.chart4 = ref}
          />
          {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
        </div>


  );
  }
}

export default App;
