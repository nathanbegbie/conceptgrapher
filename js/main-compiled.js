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
    value: function run() {
      // Force Setup
      var force = d3.layout.force().size([this.width, this.height]).charge(-40).linkDistance(60).on("tick", tick);

      var drag = force.drag().on("dragstart", dragStart);

      var svg = d3.select("body").append("svg").attr("width", this.width).attr("height", this.height);

      var link = svg.selectAll(".link");
      var node = svg.selectAll(".node");

      d3.json("data.json", function (error, graph) {

        if (error) throw error;

        force.nodes(graph.nodes).links(graph.links).friction(0.2).start();

        /*
        for(var i = 0; i < 100; i++) {
          force.tick();
        }
         force.stop();
        */

        // Adding Links to Visualization
        link = link.data(graph.links).enter().append("line").attr("class", "link");

        // Adding Nodes to Visualization
        node = node.data(graph.nodes).enter().append("circle").attr("class", "node").attr("r", 12)
        //.on("dblclick", doubleClick)
        .call(drag);

        node.append("svg:text").attr("class", "text").attr("x", 12).attr("y", "20").text(function (d) {
          return d.name;
        });
      });

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

      function doubleClick(f) {
        d3.select(this).classed("fixed", f.fixed = false);
      }

      function dragStart(f) {
        //d3.select(this).classed("fixed", f.fixed = true);
      }
    }
  }]);

  return Visualizer;
})();

var visuals = new Visualizer(1200, 700);
visuals.run();
