import React, { Component } from 'react';
import CanvasJSReact from './canvasjs/canvasjs.react';
import {Parallax} from 'react-parallax';

import electricity from './json/Activities-and-Recreation-Center_Electricity_Demand.json';
import steam from './json/Activities-and-Recreation-Center_Steam_Demand.json';
import water from './json/Activities-and-Recreation-Center_ChilledWater_Demand.json';
import wifi from './json/ARC_WiFi_TotalCount.json';
import predict from './json/prediction.json';

import Card from '@material-ui/core/Card'
import Grid from '@material-ui/core/Grid'
import { CardHeader, Typography } from '@material-ui/core';
import Button from '@material-ui/core/Button'

const CanvasJSChart = CanvasJSReact.CanvasJSChart;


const data = [electricity, steam, water, wifi, predict];
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
      if(type===0){
        dps1.push({
          x: new Date(data[type]['Points'][i1]['x']),
          y: data[type]['Points'][i1]['y']
        });
        i1+=1;
      }
      if(type===1){
        dps2.push({
          x: new Date(data[type]['Points'][i2]['x']),
          y: data[type]['Points'][i2]['y']
        });
        i2+=1;
      }
      if(type===2){
        dps3.push({
          x: new Date(data[type]['Points'][i3]['x']),
          y: data[type]['Points'][i3]['y']
        });
        i3+=1;
      }
      if(type===3){
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

    // this.chart.render();
    if(type===0){
      this.chart1.render();
    }
    if(type===1){
      this.chart2.render();
    }
    if(type===2){
      this.chart3.render();
    }
    if(type===3){
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

  predict() {

    let arr = this.createGraph(15, 4);
    let half = Math.ceil(arr.length / 2);
    let first = arr.splice(0, half);

    const options = {
        title:{
          text: "Predicted Electricity Demand"
        },
        axisY : {
          title: "Electricity Usage",
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
          name: "Electricty",
          showInLegend: true,
          dataPoints: first
        },
        {
          type: "area",
          name: "Predicted Electricity",
          showInLegend: true,
          dataPoints: arr
        }
      ]
    };

    this.setState({
      options: options
    });

    this.chart5.render();
  }


  constructor(props) {
    super(props);
    let arr = this.createGraph(15, 4);
    let half = Math.ceil(arr.length / 2);
    arr = arr.splice(0, half);
    this.state = {
      sampleFreq : 15,
      options: {
        title:{
          text: "Predicted Electricity Demand"
        },
        axisY : {
          title: "Electricity Usage",
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
          dataPoints: arr
        }]
      }
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
      // animationDuration: 50000,
      zoomEnabled: true,
      title:{
        text: "Utility Usage Over the Past Week"
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
      height: 650,
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
      title:{
        text: "Electricty Demand Over Past 24 Hours"
      },
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
        type: "spline",
        name: "Electricity",
        showInLegend: true,
        dataPoints: dps1
      }]
    }
    const options2 = {
      title:{
        text: "Steam Demand Over Past 24 Hours"
      },
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
        type: "spline",
        name: "Steam",
        showInLegend: true,
        dataPoints: dps2
      }]
    }
    const options3 = {
      title:{
        text: "Chilled Water Demand Over Past 24 Hours"
      },
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
        type: "spline",
        name: "Chilled Water",
        showInLegend: true,
        dataPoints: dps3
      }]
    }
    const options4 = {
      title:{
        text: "WiFi Usage Over Past 24 Hours"
      },
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
        type: 'spline',
        color: "teal",
        name: "Wifi",
        showInLegend: true,
        dataPoints: dps4
      }]
    }

  return (
        <div className>

          <Parallax
            blur = {10}
            bgImage = {require('./images/gray.jpg')}
            strength={200}
         >
          <Grid container
            spacing={40}
            alignItems="center"
            justify="center">

            <Grid item md={6}>
                <div>
                  <Typography align="center" component="hq" variant="h2" color="inherit" gutterBottom>
                    DEEPSus

                  </Typography>
                  <Typography align="center" component="hq" variant="h4" color="inherit" gutterBottom>
                    Davis Environmental and Energy Platform for Sustainability
                    
                  </Typography>
                  <Typography align="center" variant="h5" color="" paragraph>
                    The graph below is a normalized display of usage percentage of electricity, steam, chilled water, and Wi-Fi in the Arc Pavilion during the week of February 3, 2018 to February 10, 2018. 
                    Click on the legend labels to hide or show an individual utility and zoom/pan in order to see a more granular view of the data. 
                  </Typography>
                </div>
            </Grid>
            <Grid item xs = {8} padding = {20}>
              <Card>
                <CanvasJSChart options = {options} 
                  onRef={ref => this.chart = ref}
                />
              </Card>
            </Grid>

            <Grid item md={6}>
                <div>
                  <Typography align="center" component="hq" variant="h3" color="inherit" gutterBottom>
                    Live Data Analysis
                  </Typography>
                  <Typography align="center" variant="h5" color="inherit" paragraph>
                    The graphs below plot power consumption (in kilowatts), steam consumption (lbs/hour), chilled water consumption (tons), and total Wi-Fi connections in Arc Pavilion at every 10 minute interval throughout the week of February 3, 2018 to February 10, 2018. These graphs display data in a rolling fashion in order to provide a fine-grained view of hourly fluctuations in utility usage.
                    The data over the last 24 hours is progressively streamed in.
                  </Typography>
                </div>
            </Grid>
          </Grid>

          <Grid container
            spacing={40}
            alignItems="center"
            justify="center">
            <Grid item xs = {12} sm = {6} md = {5} padding = {10}>
              <Card padding = {20}> 
                <CanvasJSChart options = {options1} 
                    onRef={ref => this.chart1 = ref}
                />
             
              </Card>
            </Grid>

            <Grid item xs = {12} sm = {6} md = {5} padding = {10}>
              <Card padding={20}> 
                <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options2} 
                  onRef={ref => this.chart2 = ref}
                />
              </Card>
            </Grid>
          </Grid>          

          <Grid container
            spacing={40}
            alignItems="center"
            justify="center">
            <Grid item xs={12} sm = {6} md= {5} padding = {10} >
              <CardHeader>
                title="My Title"
              </CardHeader>
              <Card> 
                <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options3} 
                onRef={ref => this.chart3 = ref} />
              </Card>
            </Grid>

            <Grid item xs={12} sm = {6} md= {5} padding = {10} >
              <CardHeader>
                title="My Title"
              </CardHeader>
              <Card> 
                <CanvasJSChart style={{"height" : "50%", opacity: 0}} options = {options4} 
                onRef={ref => this.chart4 = ref} />
              </Card>
            </Grid>
          </Grid>

          <Grid container
            spacing={40}
            alignItems="center"
            justify="center">

            <Grid item md={6}>
                <div>
                  <Typography align="center" component="hq" variant="h3" color="inherit" gutterBottom>
                    Predictive Modeling
                  </Typography>
                  <Typography align="center" variant="h5" color="" paragraph>
                    In order to predict future trends in utility usage, we utilize an autoregressive integrated moving average model (ARIMA). This is a classical method for interpreting and predicting future values of times series data. Non-seasonal ARIMA models are generally denoted ARIMA(p,d,q) where parameters p, d, and q are non-negative integers, p is the order (number of time lags) of the autoregressive model, d is the degree of differencing (the number of times the data have had past values subtracted), and q is the order of the moving-average model. We chose to use a model with nonzero differencing because differencing removes the changes in the level of a time series, eliminating trend and seasonality and consequently stabilizing the mean of the time series.
                  </Typography>
                </div>

            </Grid>
            <Button variant="contained" color="primary" onClick = {this.predict.bind(this)}>
              Predict
            </Button> 
            <Grid item xs = {8} padding = {20}>
              <Card>
                <CanvasJSChart options = {this.state.options} 
                  onRef={ref => this.chart5 = ref}
                />
              </Card>
            </Grid>

          </Grid>
    
          </Parallax>

        </div>


  );
  }
}

export default App;
