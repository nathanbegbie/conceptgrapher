class Visualizer {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  run() {
    // Force Setup
    var force = cola.d3adaptor()
    .size([this.width, this.height])
    //.linkDistance(60)
    .avoidOverlaps(false)
    .symmetricDiffLinkLengths(10)
    .flowLayout('y', 30)
    //.jaccardLinkLengths(150)
    .on("tick", tick);

    var drag = force.drag()
    .on("dragstart", dragStart);

    var svg = d3.select("body").append("svg")
    .attr("width", this.width)
    .attr("height", this.height)
    .append("g")
    //.attr('transform', 'translate(250, 250) scale(0.6)')
    //.call(d3.behavior.zoom()
    //  .scaleExtent([0.2, 3])
    //  .on("zoom", zoom)
    //);

    var link = svg.selectAll(".link");
    var node = svg.selectAll(".node");

    d3.json("data.json", (error, graph) => {

      if(error) {
        throw error;
      }

      // Adding links and nodes to visualization
      force
        .nodes(graph.nodes)
        .links(graph.links)
        .start();

      // Adding links to SVG
      link = link.data(graph.links)
        .enter().append("line")
        .attr("class", "link");

      // Adding nodes to SVG
      node = node.data(graph.nodes)
        .enter().append("circle")
        .attr("class", f => {return (f.group.join(" ") + " node");})
        .attr("r", 12)
        .call(drag);

      // Calculating unique group numbers
      var uniqueGroup = [];

      for (var i of graph.nodes) {
        var group = i.group;
        for (var j of group) {
          if(uniqueGroup.indexOf(j) === -1) {
            uniqueGroup.push(j);
          }
        }
      }

      createButtons(uniqueGroup);

      var routeEdges = function () {
        d3cola.prepareEdgeRouting(margin / 3);
        link.attr("d", function (d) { return lineFunction(d3cola.routeEdge(d)); });
        if (isIE()) link.each(function (d) { this.parentNode.insertBefore(this, this) });
      }

      setTimeout(() => {//force.stop();
      //removeNodes();
      }, 2000);



    });

    // D3 helper methods

    function tick() {
      link.attr("x1", f => {return f.source.x;})
        .attr("y1",  f => {return f.source.y;})
        .attr("x2",  f => {return f.target.x;})
        .attr("y2",  f => {return f.target.y;});

      node.attr("cx",  f => {return f.x;})
        .attr("cy",  f => {return f.y;});
    }

    function zoom() {
      svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")")
    }

    function doubleClick(f) {
      d3.select(this).classed("fixed", f.fixed = false);
    }

    function dragStart(f) {
      //setTimeout(() => {force.stop();}, 1000);
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

    function removeNodes() {
      node.splice(1, 1);
      link.shift();
      link.pop();
      start();
    }
  }
}

let visuals = new Visualizer($(window).width() - 300, $(window).height() - 20);
visuals.run();
