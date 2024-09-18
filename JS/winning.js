var chart = am4core.create("chartdiv", am4charts.XYChart);

/* Add data */
chart.data = [{
  "year": "1994",
  "cars": 1587,
  "motorcycles": 650,
  "bicycles": 121
}, {
  "year": "1995",
  "cars": 1567,
  "motorcycles": 683,
  "bicycles": 146
}, {
  "year": "1996",
  "cars": 1617,
  "motorcycles": 691,
  "bicycles": 138
}, {
  "year": "1997",
  "cars": 1630.0,
  "motorcycles": 642,
  "bicycles": 127
}, {
  "year": "1998",
  "cars": 1660,
  "motorcycles": 699,
  "bicycles": 105
}, {
  "year": "1999",
  "cars": 1683,
  "motorcycles": 721,
  "bicycles": 109
}, {
  "year": "2000",
  "cars": 1691,
  "motorcycles": 737,
  "bicycles": 112
}, {
  "year": "2001",
  "cars": 1298,
  "motorcycles": 680,
  "bicycles": 101
}, {
  "year": "2002",
  "cars": 1275,
  "motorcycles": 664,
  "bicycles": 97
}, {
  "year": "2003",
  "cars": 1246,
  "motorcycles": 648,
  "bicycles": 93
}, {
  "year": "2004",
  "cars": 1218,
  "motorcycles": 637.9,
  "bicycles": 101
}, {
  "year": "2005",
  "cars": 1213,
  "motorcycles": 633,
  "bicycles": 87
}, {
  "year": "2006",
  "cars": 1199,
  "motorcycles": 621,
  "bicycles": 79
}, {
  "year": "2007",
  "cars": 1110,
  "motorcycles": 210,
  "bicycles": 81
}, {
  "year": "2008",
  "cars": 1165,
  "motorcycles": 232,
  "bicycles": 75
}, {
  "year": "2009",
  "cars": 1145,
  "motorcycles": 219,
  "bicycles": 88
}, {
  "year": "2010",
  "cars": 1163.8,
  "motorcycles": 201,
  "bicycles": 82
}, {
  "year": "2011",
  "cars": 1180,
  "motorcycles": 285,
  "bicycles": 87
}, {
  "year": "2012",
  "cars": 1159,
  "motorcycles": 277,
  "bicycles": 71
}];

/* Create axes */
var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "year";

/* Create value axis */
var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
 valueAxis.numberFormatter.numberFormat = {
  "style": "decimal",
  "minimumFractionDigits": 0
};  

/* Create series */
var series1 = chart.series.push(new am4charts.LineSeries());
series1.dataFields.valueY = "cars";
series1.dataFields.categoryX = "year";
series1.name = "Cars";
series1.strokeWidth = 3;
series1.tensionX = 0.7;
series1.bullets.push(new am4charts.CircleBullet());
series1.tooltipText = "{categoryX}: [bold]{valueY}[/]";


/* Add legend */
chart.legend = new am4charts.Legend();

/* Create a cursor */
chart.cursor = new am4charts.XYCursor();

/* Configure axis tooltip */
var axisTooltip = categoryAxis.tooltip;
axisTooltip.background.fill = am4core.color("#07BEB8");
axisTooltip.background.strokeWidth = 0;
axisTooltip.background.cornerRadius = 3;
axisTooltip.background.pointerLength = 0;
axisTooltip.dy = 5;

var dropShadow = new am4core.DropShadowFilter();
dropShadow.dy = 1;
dropShadow.dx = 1;
dropShadow.opacity = 0.5;
axisTooltip.filters.push(dropShadow);



let exportData = [{
 "year": "2000",
 "car": "BMW"
  
},
{
 "year": "2001",
 "car": "Audi"
  
}];


chart.exporting.menu = new am4core.ExportMenu();

chart.exporting.adapter.add('data', (data => {
                    data.data = [];
                    data.data = exportData;
                    return data;
                }));
