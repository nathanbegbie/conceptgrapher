



// Setup
var width = 1200;
var height = 700;

// Force Setup
var force = d3.layout.force()
.size([width, height])
.charge(-40)
.linkDistance(60)
.on("tick", tick);

var drag = force.drag()
.on("dragstart", dragStart);

var svg = d3.select("body").append("svg")
.attr("width", width)
.attr("height", height);

var link = svg.selectAll(".link");
var node = svg.selectAll(".node");

d3.json("data.json", function(error, graph) {

  if(error) throw error;

  force
  .nodes(graph.nodes)
  .links(graph.links)
  .friction(0.2)
  .start();

  /*
  for(var i = 0; i < 100; i++) {
    force.tick();
  }

  force.stop();
  */

  // Adding Links to Visualization
  link = link.data(graph.links)
  .enter().append("line")
  .attr("class", "link");

  // Adding Nodes to Visualization
  node = node.data(graph.nodes)
  .enter().append("circle")
  .attr("class", "node")
  .attr("r", 12)
  //.on("dblclick", doubleClick)
  .call(drag);

  node.append("svg:text")
  .attr("class", "text")
  .attr("x", 12)
  .attr("y", "20")
  .text(function(d) {
    return d.name });



});

function tick() {
  link.attr("x1", function(f){return f.source.x;})
  .attr("y1", function(f){return f.source.y;})
  .attr("x2", function(f){return f.target.x;})
  .attr("y2", function(f){return f.target.y;});

  node.attr("cx", function(f){return f.x})
  .attr("cy", function(f){return f.y});
}

function doubleClick(f)  {
  d3.select(this).classed("fixed", f.fixed = false);
}

function dragStart(f)  {
  //d3.select(this).classed("fixed", f.fixed = true);
}
