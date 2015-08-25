
// svg.selectAll("rect")
//     .data(colore.range()).enter()
//     .append("rect")
//     .attr("fill", function (color){ return color; })
//     .attr("x", function (color, index){ return (index * 12) + "px"; })
//     .attr("y", margin - 8 + "px")
//     .attr("width", 8 + "px")
//     .attr("height", 8 + "px");

// Select the DIV container "D3line" then
// add an SVG element to it
 
// var width = 400;
// var height = 400;
 
// var lineGraph = d3.select("#D3lines")
//     .append("svg:svg")
//     .attr("width", width)    
//     .attr("height", height); 
 
// // To draw a line use the "svg:line" element.
// // "svg:line" element requires 4 attributes (x1, y1, x2, and y2)
// // (x1,y1) are coordinates of the starting point. 
// // (x2,y2) are coordinates of the end point.
// // You also need to specify the stroke color.
 
// // Using for loop to draw multiple horizontal lines
// for (var j=25; j <= width-25; j=j+25) {
//     lineGraph.append("svg:line")
//         .attr("x1", 25)
//         .attr("y1", j)
//         .attr("x2", width-25)
//         .attr("y2", j)
//         .style("stroke", "rgb(6,120,155)")
//         .style("stroke-width", 2);            
// };
 
// // Using for loop to draw multiple vertical lines
// for (var j=25; j <= height-25; j=j+25) {
//     lineGraph.append("svg:line")
//         .attr("x1", j)
//         .attr("y1", 25)
//         .attr("x2", j)
//         .attr("y2", height-25)
//         .style("stroke", "rgb(6,120,155)")
//         .style("stroke-width", 2);            
// };
// 

var radius = 15;
var x = 20;
var y = 20;

// var circle = d3.select("#D3lines")
// 	.append("svg:svg")
// 	.append("circle")
// 	.attr("r", radius)
// 	.attr("cx", x)
// 	.attr("cy", y)
// 	.style("fill","red");

// for (var j=1; j < 20; j=j+1) {
// 	circle.append("svg:circle")
// 		.attr("r", radius+j)
// 		.attr("cx", x+j)
// 		.attr("cy", y+j)
// 		.style("fill", "red");
// }

for (var j=1; j<=20; j=j+1) {
	d3.select("svg")
		//.append("svg:svg")
		.append("circle")
		.attr("r", radius)
		.attr("cx", 2*radius*j)
		.attr("cy", 2*radius*j)
		.style("opacity", j)
		.style("fill", "lightblue")
}

for (var j=0; j<=500; j=j+100) {
	d3.selectAll("circle").transition().delay(1500).duration(2000).attr("cy", j);	
}
// for (var j=0; j<=500; j=j+100) {
// 	d3.selectAll("circle").transition().duration(2000).attr("cy", j);	
// }
//d3.selectAll("circle").transition().duration(2000).attr("cy", 500);
// d3.select("svg")
//  .append("text")
//  .attr("id", "a")
//  .attr("x",20)
//  .attr("y",20)
//  .style("opacity", 0)
//  .text("HELLO WORLD");
// d3.select("svg")
//  .append("circle")
//  .attr("r", 100)
//  .attr("cx",400)
//  .attr("cy",400)
//  .style("fill","lightblue");
// d3.select("svg")
//  .append("text")
//  .attr("id", "b")
//  .attr("x",400)
//  .attr("y",400)
//  .style("opacity", 0)
//  .text("Uh, hi.");

// d3.select("#a").transition().delay(1000).style("opacity", 1);
// d3.select("#b").transition().delay(2000).style("opacity", .75);

// d3.selectAll("circle").transition().duration(2000).attr("cy", 200);
// d3.selectAll("circle").transition().delay(2100).duration(1000).attr("cy", 400);