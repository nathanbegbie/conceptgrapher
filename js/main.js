
var groupList;

class Visualizer {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  run(constraint, rebuild) {
    // Force Setup
    var force = cola.d3adaptor()
    .size([this.width, this.height])
    //.linkDistance(60)
    //.avoidOverlaps(true)
    //.symmetricDiffLinkLengths(100)
    .flowLayout('y', 30)
    .jaccardLinkLengths(100)
    .on("tick", tick);


    var drag = force.drag()
    .origin( d => { return d; })
    .on("dragstart", dragStarting)
    .on("drag", dragging)
    .on("dragend", dragEnding);

    var svg = d3.select("#svg-wrapper").append("svg")
    .attr("width", this.width)
    .attr("height", this.height)
    .call(d3.behavior.zoom().on("zoom", zoom)).on("dblclick.zoom", null);

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

    // now accept a param that chooses what to filter by
    $.getJSON('data.json').done( graph => {

      // Setup nodes and edges correctly for D3
      var nodes = {};
      var links = {};

      // Filter nodes based on group constraint
      if (constraint !== null && constraint.length > 0) {
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
        .attr("class", f => {return (f.group.join(" ") + " " + f.typeof + " node");})
        .attr("content", f => {return f.content;})
        .call(drag);

        d3.selectAll(".ConceptNode").append("path")
        .attr("d", d3.svg.symbol().type("circle"))
        .attr("transform", "scale(" + scaleOfBigSymbols + ")")
        .on("dblclick", doubleClick)
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);

        //Fact
        d3.selectAll(".FactNode").append("path")
        .attr("d", d3.svg.symbol().type("square"))
        .attr("transform", "scale(" + scaleOfBigSymbols + ")")
        .on("dblclick", doubleClick)
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);

        //Scase
        d3.selectAll(".ScaseNode").append("path")
        .attr("d", d3.svg.symbol().type("cross"))
        .attr("transform", "scale(" + scaleOfSmallSymbols + ")")
        .on("dblclick", doubleClick)
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);

        d3.selectAll(".MisconNode").append("path")
        .attr("d", d3.svg.symbol().type("diamond"))
        .attr("transform", "scale(" + scaleOfSmallSymbols + ")")
        .on("dblclick", doubleClick)
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);

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

      if (rebuild === true) {
        buildList(uniqueGroup);
      }

    });

    // D3 helper methods

    function tick() {
      link.attr("x1", f => {return f.source.x;})
        .attr("y1",  f => {return f.source.y;})
        .attr("x2",  f => {return f.target.x;})
        .attr("y2",  f => {return f.target.y;});

        node.attr("transform", d => {
          return "translate(" + d.x + "," + d.y + ")";
        });
    }

    function mouseover(d) {
      var content = d.content;

      if(content.length > 100) {
        content = content.substring(0,105) + "....";
      }

      $("#description").append(`<p class="valign">${d.name}: ${content}</p>`);
    }

    function mouseout(d) {
      $("#description").find("p").remove();
    }

    function zoom() {
      visuals.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")")
    }

    function dragStarting(f) {
      d3.event.sourceEvent.stopPropagation();
      d3.select(this).classed("fixed", f.fixed = true);
      d3.select(this).classed("dragging", true);
    }

    function doubleClick(f) {
      d3.select(this).classed("fixed", f.fixed = false);
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
        item: '<a class="collection-item"><p class="name"></p></a>'
      };

      groupList = new List('groups', options);
      var result = [];

      for (var i of groups) {
        result.push({name: i});
      }
      groupList.add(result);
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
let visuals = new Visualizer($("#svg-wrapper").width(), $(window).height() - 60);
visuals.run(null, true);


$(document).on("click", ".name", () => {

  // Move group from selectable to filter
  var current = $(event.target).text();
  groupList.remove("name", current);
  $("body").find("#filter").append(`<div class="chip"><span class="filtered-by">${current}</span><i class="material-icons close-filter">close</i></div>`);

  // Build list of items to filter by
  var output = [];

  var currentGroups = $(".filtered-by").each( (i, o) => {
    output.push(o.textContent);
  });

  // Clear D3 SVG and run with new paramaters
  visuals.clear();
  visuals.run(output, false);

});

$(document).on("click", ".close-filter", () => {
  // Get removed group
  var current = $(event.target).parent().find('span').text();

  // Add back to list
  groupList.add([{name: current}]);

  // Build list of items to filter by
  var output = [];

  var currentGroups = $(".filtered-by").each( (i, o) => {
    output.push(o.textContent);
  });

  output.splice(output.indexOf(current), 1);

  // Clear D3 SVG and run with new paramaters
  visuals.clear();
  visuals.run(output, false);
});

$(document).on("mouseover", ".chip",  () => {
  var current = $(event.target).find('span').html();
  if (current !== undefined) {
    $("body").find(".node").css("fill", "#F5F5F5");
    $("body").find(`.${current}`).css("fill", "#64DD17");
  }
});

$(document).on("mouseleave", ".chip",  () => {
    $("body").find(".ConceptNode").css("fill", "#4783c1");
    $("body").find(".FactNode").css("fill", "#FFC107");
    $("body").find(".MisconNode").css("fill", "#e76351");
    $("body").find(".ScaseNode").css("fill", "#55cd7c");
});
