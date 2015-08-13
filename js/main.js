
class Visualizer {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  run() {
    // Force Setup
    var force = d3.layout.force()
    .size([this.width, this.height])
    .charge(-500)
    .linkDistance(60)
    .on("tick", tick);

    var drag = force.drag()
    .on("dragstart", dragStart);

    var svg = d3.select("body").append("svg")
    .attr("width", this.width)
    .attr("height", this.height);

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
      .attr("class", function(d) {return (d.group + " node");})
      .attr("r", 12)
      //.on("dblclick", doubleClick)
      .call(drag);

      node.append("svg:text")
      .attr("class", "text")
      .attr("x", 12)
      .attr("y", "20")
      .text(function(d) {
        return d.name;});

      //var send = (graph.nodes).filter(unique);
      /*var send = $.grep(graph.nodes, function(curr, i) {
        return $.inArray(curr, graph.nodes) == i;
      }) */

      // Calculating unique group numbers
      var uniqueGroup = [];

      for (var i of graph.nodes) {
        if(uniqueGroup.indexOf(i.group) === -1) {
          uniqueGroup.push(i.group);
        }
      }

      createButtons(uniqueGroup);

      setTimeout(function(){force.stop()}, 2000);

      });

      function tick() {
        link.attr("x1", function(f){return f.source.x;})
        .attr("y1", function(f){return f.source.y;})
        .attr("x2", function(f){return f.target.x;})
        .attr("y2", function(f){return f.target.y;});

        node.attr("cx", function(f){return f.x})
        .attr("cy", function(f){return f.y});
      }

      function doubleClick(f) {
        d3.select(this).classed("fixed", f.fixed = false);
      }

      function dragStart(f) {
        //d3.select(this).classed("fixed", f.fixed = true);
        setTimeout(function(){force.stop()}, 1000);
      }

      function createButtons(groups) {
        for (var i of groups) {
          var add = $(`<button class="group" value=${i}>Group ${i}</button>`);
          $("#groups").append(add);
          $("#groups").delegate(".group","click",function() {
            var value = $(this).attr("value");
            $("body").find(".node").css("fill", "#EEEEEE");
            $("body").find("." + value).css("fill", "#"+num()+num()+num());
          });
        }
      }

      function num() {
        return Math.floor(Math.random()*256).toString(16);
      }
  }

}

let visuals = new Visualizer($(window).width() - 300, $(window).height() - 20);
visuals.run();
