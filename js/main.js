class Visualizer {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  run(constraint) {
    // Force Setup
    var force = cola.d3adaptor() //.convergenceThreshold(0.01)
    .size([this.width, this.height])
    //.linkDistance(60)
    .avoidOverlaps(false)
    //.symmetricDiffLinkLengths(10)
    .flowLayout('y', 30)
    .jaccardLinkLengths(50)
    .on("tick", tick);

    var drag = d3.behavior.drag() //force.drag();
    //.origin(d =>  {return d;})
    //.on("dragstart", dragStarting)
    //.on("drag", dragging)
    //.on("dragend", dragEnding);

    var svg = d3.select("body").append("svg")
    .attr("width", this.width)
    .attr("height", this.height)
    .call(d3.behavior.zoom().on("zoom", zoom));

    svg.append("rect")
    .attr("class", "background")
    .attr("width", "100%")
    .attr("height", "100%")
    .style("fill", "none")
    .style("pointer-events", "all");

    var visuals = svg.append("g")
    .attr('transform', 'translate(250, 250) scale(0.3)');


    var link = visuals.selectAll(".link");
    var node = visuals.selectAll(".node");

    //d3.json("data.json", (error, graph) => {


    // now accept a param that chooses what to filter by
    $.getJSON('data.json').done( graph => {

      // for every node check if group in constraint USE JS ARRAY FILTER
      // if true
      //    push to node array
      //    use node index to find all edges
      //    push edges to edge array
      // else next

      // Setup nodes and edges correctly for D3
      var nodes = {};
      var links = {};

      // Filter nodes based on constraint
      if (constraint !== null) {
        nodes = graph.nodes.filter( e => {
          if (constraint.indexOf(e["name"]) >= 0) {
            return true;
          }
        });
      }
      else {
        nodes = graph.nodes;
      }

      // Filter links based on constrained nodes
      links = graph.links.filter( e => {
        if (constraint.indexOf(e["source"]) >= 0 && constraint.indexOf(e["target"]) >= 0) {
          return true;
        }
      });

      // Update links to use numerical IDs for D3
      for (var i of links) {
        i["source"] = search(i["source"], nodes);
        i["target"] = search(i["target"], nodes);
      }

      console.log(nodes);
      console.log(links);

      //if(error) {
      //  throw error;
    //  }

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
      //addNodes();
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
      visuals.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")")
    }

    function doubleClick(f) {
      d3.select(this).classed("fixed", f.fixed = false);
    }

    function dragStarting(f) {
      d3.event.sourceEvent.stopPropagation();
      d3.select(this).classed("dragging", true);
      force.start();
    }

    function dragging(f) {
      d3.select(this).attr("cx", f.x = d3.event.x).attr("cy", f.y = d3.event.y);
    }

    function dragEnding(f) {
      d3.select(this).classed("dragging", false);
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

    function search(name, arr) {
      for (var i = 0; i < arr.length; i++) {
        if (arr[i]["name"] === name) {
          return i;
        }
      }
      return -1;
    }

    function removeNodes() {
      console.log('Before');
      console.log(node);
      node.splice(10, 10);
      //link.shift();
      //link.pop();
      console.log('After');
      console.log(node);

      var x = visuals.selectAll(".node").data(node);

      x.exit().remove();
      force.nodes(node);

    }

    function addNodes() {
      var a = {"name": "TESTING", "group": ["TESTGROUP"]};
      node.push(a);
      console.log('TEST');
      force.start();
    }
  }
}

let visuals = new Visualizer($(window).width() - 300, $(window).height() - 20);
visuals.run(["MFIN238", "MFIN132", "MFIN135"]);

$(document).ready(() => {
  $(".test").on("click", () => {
    console.log("Clearing...");
    d3.select('svg').remove();
    $("#groups").find("button").remove();
    visuals.run();
  });
});
