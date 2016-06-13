var data = [55, 44, 30, 23, 17, 14, 16, 25, 41, 61, 85,
                    101, 95, 105, 114, 150, 180, 210, 125, 100, 71,
                    75, 72, 67];

var maxValue = d3.max(data);

var width = 500, height = 500;

var svg = d3.select('body').append('svg').attr({
  width:width,height:height
});

var scale = d3.scale.linear().domain([0,maxValue]).range([0,width]);

var axisGroup = svg.append('g');

var axis = d3.svg.axis().scale(scale);

axisGroup.call(axis);
