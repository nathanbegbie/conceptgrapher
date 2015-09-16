
var groupList;

class Visualizer {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  run(constraint, rebuild) {
    // Force Setup
    var force = cola.d3adaptor() //.convergenceThreshold(0.01)
    .size([this.width, this.height])
    //.linkDistance(60)
    .avoidOverlaps(false)
    //.symmetricDiffLinkLengths(10)
    .flowLayout('y', 30)
    .jaccardLinkLengths(100)
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

    //create a placeholder for the shape of the arrowhead
    svg.append("defs").append("marker")
    .attr("id", "arrowhead")
    .attr("refX", 20)
    .attr("refY", 2)
    .attr("markerWidth", 6)
    .attr("markerHeight", 4)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M 0,0 V 4 L6,2 Z"); //this is actual shape for arrowhead

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

      // Setup nodes and edges correctly for D3
      var nodes = {};
      var links = {};

      // Filter nodes based on group constraint
      if (constraint !== null) {
        nodes = graph.nodes.filter( e => {

          for (var i of e["group"]) {
            if (constraint.indexOf(i) >= 0) {
              return true;
            }
          }

          return false;

        });
      }
      else {
        nodes = graph.nodes;
      }

      // Filter links based on constrained nodes
      links = graph.links.filter( e => {
        if (search(e["source"], nodes) >= 0 && search(e["target"], nodes) >= 0) {
          return true;
        }
      });

      // Update links to use numerical IDs for D3
      for (var i of links) {
        i["source"] = search(i["source"], nodes);
        i["target"] = search(i["target"], nodes);
      }

      // Adding links and nodes to visualization
      force
        .nodes(nodes)
        .links(links)
        .start();

      // Adding links to SVG
      link = link.data(links)
        .enter().append("line")
        .attr("class", d => {return "link " + d.typeof;})
        .attr("marker-end", d => {
          if (d.typeof === "directed") {
            return "url(#arrowhead)";
          }
          else {
            return " ";
          }
        });
      // size of symbols
      var scaleOfBigSymbols = 6;
      var scaleOfSmallSymbols = 4;

      // Adding nodes to SVG
      node = node.data(nodes)
        .enter().append("g")
        .attr("class", f => {return (f.group.join(" ") + " " + f.typeof + " node");});

        d3.selectAll(".ConceptNode").append("path")
        .attr("d", d3.svg.symbol().type("square"))
        .attr("transform", "scale(" + scaleOfBigSymbols + ")");

        //Fact
        d3.selectAll(".FactNode").append("path")
        .attr("d", d3.svg.symbol().type("circle"))
        .attr("transform", "scale(" + scaleOfBigSymbols + ")");

        //Scase
        d3.selectAll(".ScaseNode").append("path")
        .attr("d", d3.svg.symbol().type("cross"))
        .attr("transform", "scale(" + scaleOfSmallSymbols + ")");

        d3.selectAll(".MisconNode").append("path")
        .attr("d", d3.svg.symbol().type("diamond"))
        .attr("transform", "scale(" + scaleOfSmallSymbols + ")");

        node.append("svg:text")
        .attr("class", "nodetext")
        .attr("dx", 0)
        .attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .attr("fill", "black")
        .text(d => {
          return d.name
        });

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

      //createButtons(uniqueGroup);
        if (rebuild === true) {
          buildList(uniqueGroup);
        }

      var routeEdges = function () {
        d3cola.prepareEdgeRouting(margin / 3);
        link.attr("d", function (d) { return lineFunction(d3cola.routeEdge(d)); });
        if (isIE()) link.each(function (d) { this.parentNode.insertBefore(this, this) });
      }

    });

    // D3 helper methods

    function tick() {
      link.attr("x1", f => {return f.source.x;})
        .attr("y1",  f => {return f.source.y;})
        .attr("x2",  f => {return f.target.x;})
        .attr("y2",  f => {return f.target.y;});

      //node.attr("cx",  f => {return f.x;})
        //.attr("cy",  f => {return f.y;});

        node.attr("transform", function (d) {
          return "translate(" + d.x + "," + d.y + ")";
        });
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

    function buildList(groups) {

      var options = {
        valueNames: ['name'],
        item: '<li><p class="name"></p></li>'
      };

      groupList = new List('groups', options);
      var result = [];

      for (var i of groups) {
        result.push({name: i});
      }
      groupList.add(result);
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
  }

  clear() {
    d3.select('svg').remove();
  }

}


// Instantiation of visualizer
let visuals = new Visualizer($(window).width() - 300, $(window).height() - 20);
visuals.run(null, true);


$(document).on("click", ".name", () => {

  // Move group from selectable to filter
  var current = $(event.target).text();
  groupList.remove("name", current);
  $("body").find("#filter").append(`<li><p class="filtered-by">${current}</p></li>`);

  // Build list of items to filter by
  var output = [];

  var currentGroups = $(".filtered-by").each( (i, o) => {
    output.push(o.textContent);
  });

  // Clear D3 SVG and run with new paramaters
  visuals.clear();
  visuals.run(output, false);

});
