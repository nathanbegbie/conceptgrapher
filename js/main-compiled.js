"use strict";

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Visualizer = (function () {
  function Visualizer(width, height) {
    _classCallCheck(this, Visualizer);

    this.width = width;
    this.height = height;
  }

  _createClass(Visualizer, [{
    key: "run",
    value: function run(constraint) {
      // Force Setup
      var force = cola.d3adaptor() //.convergenceThreshold(0.01)
      .size([this.width, this.height])
      //.linkDistance(60)
      .avoidOverlaps(false)
      //.symmetricDiffLinkLengths(10)
      .flowLayout('y', 30).jaccardLinkLengths(50).on("tick", tick);

      var drag = d3.behavior.drag(); //force.drag();
      //.origin(d =>  {return d;})
      //.on("dragstart", dragStarting)
      //.on("drag", dragging)
      //.on("dragend", dragEnding);

      var svg = d3.select("body").append("svg").attr("width", this.width).attr("height", this.height).call(d3.behavior.zoom().on("zoom", zoom));

      svg.append("rect").attr("class", "background").attr("width", "100%").attr("height", "100%").style("fill", "none").style("pointer-events", "all");

      var visuals = svg.append("g").attr('transform', 'translate(250, 250) scale(0.3)');

      var link = visuals.selectAll(".link");
      var node = visuals.selectAll(".node");

      //d3.json("data.json", (error, graph) => {

      // now accept a param that chooses what to filter by
      $.getJSON('data.json').done(function (graph) {

        // Setup nodes and edges correctly for D3
        var nodes = {};
        var links = {};

        // Filter nodes based on group constraint
        if (constraint !== null) {
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
        } else {
          nodes = graph.nodes;
        }

        // Filter links based on constrained nodes
        links = graph.links.filter(function (e) {
          if (search(e["source"], nodes) >= 0 && search(e["target"], nodes) >= 0) {
            return true;
          }
        });
        console.log(links);

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

        console.log(nodes);
        console.log(links);

        // Adding links and nodes to visualization
        force.nodes(nodes).links(links).start();

        // Adding links to SVG
        link = link.data(links).enter().append("line").attr("class", "link");

        // Adding nodes to SVG
        node = node.data(nodes).enter().append("circle").attr("class", function (f) {
          return f.group.join(" ") + " node";
        }).attr("r", 12).call(drag);

        // Calculating unique group numbers
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

        createButtons(uniqueGroup);

        var routeEdges = function routeEdges() {
          d3cola.prepareEdgeRouting(margin / 3);
          link.attr("d", function (d) {
            return lineFunction(d3cola.routeEdge(d));
          });
          if (isIE()) link.each(function (d) {
            this.parentNode.insertBefore(this, this);
          });
        };
      });

      // D3 helper methods

      function tick() {
        link.attr("x1", function (f) {
          return f.source.x;
        }).attr("y1", function (f) {
          return f.source.y;
        }).attr("x2", function (f) {
          return f.target.x;
        }).attr("y2", function (f) {
          return f.target.y;
        });

        node.attr("cx", function (f) {
          return f.x;
        }).attr("cy", function (f) {
          return f.y;
        });
      }

      function zoom() {
        visuals.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
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
        var _iteratorNormalCompletion5 = true;
        var _didIteratorError5 = false;
        var _iteratorError5 = undefined;

        try {
          for (var _iterator5 = groups[Symbol.iterator](), _step5; !(_iteratorNormalCompletion5 = (_step5 = _iterator5.next()).done); _iteratorNormalCompletion5 = true) {
            var i = _step5.value;

            var add = $("<button class=\"group\" value=" + i + ">Group " + i + "</button>");
            $("#groups").append(add);
            $("#groups").delegate(".group", "click", function () {
              var value = $(this).attr("value");
              $("body").find(".node").css("fill", "#EEEEEE");
              $("body").find("." + value).css("fill", "#" + num() + num() + num());
            });
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
      }

      function num() {
        return Math.floor(Math.random() * 256).toString(16);
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
  }]);

  return Visualizer;
})();

var visuals = new Visualizer($(window).width() - 300, $(window).height() - 20);
visuals.run(["MFIN014"]);

$(document).ready(function () {
  $(".test").on("click", function () {
    console.log("Clearing...");
    d3.select('svg').remove();
    $("#groups").find("button").remove();
    visuals.run();
  });
});
