"use strict";

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var groupList;
var groupAttr;
var nodes;

var Visualizer = (function () {
  /*
  The Visualizer class provides functionality for creating a D3 forced layout
  in the DOM, as well as dynamic filtering of data.
  */

  function Visualizer(width, height) {
    _classCallCheck(this, Visualizer);

    this.width = width;
    this.height = height;
  }

  _createClass(Visualizer, [{
    key: "run",
    value: function run(constraint, rebuild) {
      /*
      The priamry function for the Visualizer class. Does most of the work for setting up
      D3 / D3Cola, and setting up the DOM. Accepts an optional list of groups to
      filter the data by. Also accepts a boolean argument to determine if this is
      a first-time run.
      */

      // Force Setup
      var force = cola.d3adaptor().size([this.width, this.height]).flowLayout('y', 30).jaccardLinkLengths(100).on("tick", tick);

      var drag = force.drag().origin(function (d) {
        return d;
      }).on("dragstart", dragStarting).on("drag", dragging).on("dragend", dragEnding);

      var svg = d3.select("#svg-wrapper").append("svg").attr("width", this.width).attr("height", this.height).call(d3.behavior.zoom().on("zoom", zoom)).on("dblclick.zoom", null);

      svg.append("defs").append("marker").attr("id", "arrowhead").attr("refX", 20).attr("refY", 2).attr("markerWidth", 6).attr("markerHeight", 4).attr("orient", "auto").append("path").attr("d", "M 0,0 V 4 L6,2 Z");

      svg.append("rect").attr("class", "background").attr("width", "100%").attr("height", "100%").style("fill", "none").style("pointer-events", "all");

      var visuals = svg.append("g").attr('transform', 'translate(250, 250) scale(0.3)');

      var link = visuals.selectAll(".link");
      var node = visuals.selectAll(".node");

      try {
        // Start asynchronous callback for JSON data
        $.getJSON('data.json').done(function (graph) {

          // Setup nodes and edges correctly for D3
          nodes = {};
          var links = {};
          groupAttr = graph.groups;

          // Filter nodes based on group constraint
          if (constraint !== null && constraint.length > 0) {
            nodes = graph.nodes.filter(function (e) {
              var _iteratorNormalCompletion = true;
              var _didIteratorError = false;
              var _iteratorError = undefined;

              try {

                for (var _iterator = e["group"][Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
                  var i = _step.value;

                  if (constraint.indexOf(i) >= 0) {
                    return true;
                  }
                }
              } catch (err) {
                _didIteratorError = true;
                _iteratorError = err;
              } finally {
                try {
                  if (!_iteratorNormalCompletion && _iterator["return"]) {
                    _iterator["return"]();
                  }
                } finally {
                  if (_didIteratorError) {
                    throw _iteratorError;
                  }
                }
              }

              return false;
            });

            // Filter links based on constrained nodes
            links = graph.links.filter(function (e) {
              if (search(e["source"], nodes) >= 0 && search(e["target"], nodes) >= 0) {
                return true;
              }
            });

            // Update links to use numerical IDs for D3
            var _iteratorNormalCompletion2 = true;
            var _didIteratorError2 = false;
            var _iteratorError2 = undefined;

            try {
              for (var _iterator2 = links[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
                var i = _step2.value;

                i["source"] = search(i["source"], nodes);
                i["target"] = search(i["target"], nodes);
              }

              // Adding links and nodes to visualization
            } catch (err) {
              _didIteratorError2 = true;
              _iteratorError2 = err;
            } finally {
              try {
                if (!_iteratorNormalCompletion2 && _iterator2["return"]) {
                  _iterator2["return"]();
                }
              } finally {
                if (_didIteratorError2) {
                  throw _iteratorError2;
                }
              }
            }

            force.nodes(nodes).links(links).start();

            // Adding links to SVG
            link = link.data(links).enter().append("line").attr("class", function (d) {
              return "link " + d["typeof"];
            }).attr("marker-end", function (d) {
              if (d["typeof"] === "directed") {
                return "url(#arrowhead)";
              } else {
                return " ";
              }
            });

            // Size of symbols
            var scaleOfBigSymbols = 6;
            var scaleOfSmallSymbols = 4;

            // Adding nodes to SVG
            node = node.data(nodes).enter().append("g").attr("class", function (f) {
              return f.group.join(" ") + " " + f["typeof"] + " " + f.isCycle + " node";
            }).attr("content", function (f) {
              return f.content;
            }).call(drag);

            // Concept
            d3.selectAll(".ConceptNode").append("path").attr("d", d3.svg.symbol().type("circle")).attr("transform", "scale(" + scaleOfBigSymbols + ")").on("dblclick", doubleClick).on("mouseover", mouseover).on("mouseout", mouseout);

            // Fact
            d3.selectAll(".FactNode").append("path").attr("d", d3.svg.symbol().type("square")).attr("transform", "scale(" + scaleOfBigSymbols + ")").on("dblclick", doubleClick).on("mouseover", mouseover).on("mouseout", mouseout);

            // Scase
            d3.selectAll(".ScaseNode").append("path").attr("d", d3.svg.symbol().type("cross")).attr("transform", "scale(" + scaleOfSmallSymbols + ")").on("dblclick", doubleClick).on("mouseover", mouseover).on("mouseout", mouseout);

            // Misconcept
            d3.selectAll(".MisconNode").append("path").attr("d", d3.svg.symbol().type("diamond")).attr("transform", "scale(" + scaleOfSmallSymbols + ")").on("dblclick", doubleClick).on("mouseover", mouseover).on("mouseout", mouseout);

            // Text
            node.append("svg:text").attr("class", "nodetext").attr("dx", 0).attr("dy", ".35em").attr("text-anchor", "middle").attr("fill", "black").text(function (d) {
              return d.name;
            });
          } else {
            $("#svg-wrapper").append("<div id='filter-text'><h5>To get started, use the filters on the right to select data.</h5></div>");
          }

          // Create filtering list
          var uniqueGroup = [];

          var _iteratorNormalCompletion3 = true;
          var _didIteratorError3 = false;
          var _iteratorError3 = undefined;

          try {
            for (var _iterator3 = graph.nodes[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
              var i = _step3.value;

              var group = i.group;
              var _iteratorNormalCompletion4 = true;
              var _didIteratorError4 = false;
              var _iteratorError4 = undefined;

              try {
                for (var _iterator4 = group[Symbol.iterator](), _step4; !(_iteratorNormalCompletion4 = (_step4 = _iterator4.next()).done); _iteratorNormalCompletion4 = true) {
                  var j = _step4.value;

                  if (uniqueGroup.indexOf(j) === -1) {
                    uniqueGroup.push(j);
                  }
                }
              } catch (err) {
                _didIteratorError4 = true;
                _iteratorError4 = err;
              } finally {
                try {
                  if (!_iteratorNormalCompletion4 && _iterator4["return"]) {
                    _iterator4["return"]();
                  }
                } finally {
                  if (_didIteratorError4) {
                    throw _iteratorError4;
                  }
                }
              }
            }
          } catch (err) {
            _didIteratorError3 = true;
            _iteratorError3 = err;
          } finally {
            try {
              if (!_iteratorNormalCompletion3 && _iterator3["return"]) {
                _iterator3["return"]();
              }
            } finally {
              if (_didIteratorError3) {
                throw _iteratorError3;
              }
            }
          }

          if (rebuild === true) {
            buildList(uniqueGroup);
          }
        });
      } catch (e) {
        console.log(e.name);
      }

      /* ------ D3 Helper Methods ------*/

      function tick() {
        /*
        D3 method to reposition nodes through transformation.
        */
        link.attr("x1", function (f) {
          return f.source.x;
        }).attr("y1", function (f) {
          return f.source.y;
        }).attr("x2", function (f) {
          return f.target.x;
        }).attr("y2", function (f) {
          return f.target.y;
        });

        node.attr("transform", function (d) {
          return "translate(" + d.x + "," + d.y + ")";
        });
      }

      function mouseover(d) {
        /*
        Handles mouseover of a node.
        Will cause node information to be displayed in a text area at the bottom
        of the screen.
        */
        var content = d.content;
        var currentGroups;

        var _iteratorNormalCompletion5 = true;
        var _didIteratorError5 = false;
        var _iteratorError5 = undefined;

        try {
          for (var _iterator5 = nodes[Symbol.iterator](), _step5; !(_iteratorNormalCompletion5 = (_step5 = _iterator5.next()).done); _iteratorNormalCompletion5 = true) {
            var i = _step5.value;

            if (i.name === d.name) {
              currentGroups = i.group.join(" ");
            }
          }
        } catch (err) {
          _didIteratorError5 = true;
          _iteratorError5 = err;
        } finally {
          try {
            if (!_iteratorNormalCompletion5 && _iterator5["return"]) {
              _iterator5["return"]();
            }
          } finally {
            if (_didIteratorError5) {
              throw _iteratorError5;
            }
          }
        }

        if (content.length > 100) {
          content = content.substring(0, 105) + "....";
        }

        if (currentGroups.length > 100) {
          currentGroups = currentGroups.substring(0, 105) + "....";
        }

        $("#description").append("<div class=\"valign\"><p><span class=\"highlight\"><b>" + d.name + "</b></span> " + content + "</p><p><span class=\"highlight\"><b>Groups</b></span> " + currentGroups + "</p>");
      }

      function mouseout(d) {
        /*
        Handles mouseover of a node.
        Will remove added descriptive data.
        */
        $("#description").find("p").remove();
      }

      function zoom() {
        /*
        D3 method to handle zooming of the SVG panel.
        */
        visuals.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
      }

      function dragStarting(f) {
        /*
        Handles the start of the drag event.
        Stops zooming from interfering with dragging, and also sets nodes to fixed
        to create the "sticky nodes" effect.
        */
        d3.event.sourceEvent.stopPropagation();
        d3.select(this).classed("fixed", f.fixed = true);
        d3.select(this).classed("dragging", true);
      }

      function doubleClick(f) {
        /*
        Returns nodes to original state on double click, removing fixed status.
        */
        d3.select(this).classed("fixed", f.fixed = false);
      }

      function dragging(f) {
        /*
        Handles repositioning of the node during the drag event.
        */
        d3.select(this).attr("cx", f.x = d3.event.x).attr("cy", f.y = d3.event.y);
      }

      function dragEnding(f) {
        /*
        Handles the ending of the drag event.
        */
        d3.select(this).classed("dragging", false);
      }

      function buildList(groups) {
        /*
        Builds the filtering list from a set of unique groups.
        This list is then used by List.js to provide real-time filtering in the DOM.
        */

        var options = {
          valueNames: ['name'],
          item: '<a class="collection-item"><p class="name"></p></a>'
        };

        groupList = new List('groups', options);
        var result = [];

        var _iteratorNormalCompletion6 = true;
        var _didIteratorError6 = false;
        var _iteratorError6 = undefined;

        try {
          for (var _iterator6 = groups[Symbol.iterator](), _step6; !(_iteratorNormalCompletion6 = (_step6 = _iterator6.next()).done); _iteratorNormalCompletion6 = true) {
            var i = _step6.value;

            result.push({ name: i });
          }
        } catch (err) {
          _didIteratorError6 = true;
          _iteratorError6 = err;
        } finally {
          try {
            if (!_iteratorNormalCompletion6 && _iterator6["return"]) {
              _iterator6["return"]();
            }
          } finally {
            if (_didIteratorError6) {
              throw _iteratorError6;
            }
          }
        }

        groupList.add(result);
      }

      function search(name, arr) {
        /*
        Provides a custom search for name based on the structure of the JSON objects.
        */
        for (var i = 0; i < arr.length; i++) {
          if (arr[i]["name"] === name) {
            return i;
          }
        }
        return -1;
      }
    }
  }, {
    key: "clear",
    value: function clear() {
      /*
      A class function to reset the DOM.
      */
      d3.select('svg').remove();
    }
  }]);

  return Visualizer;
})();
