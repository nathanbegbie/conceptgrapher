"use strict";

$(document).on("click", ".name", function () {
  /*
  Handles addition of filter.
  Will add new filter to the DOM, remove it from the main list, and will
  reset D3 to show the change.
  */

  // Remove filtering how-to
  $("body").find("#filter-text").remove();

  // Move group from selectable to filter
  var current = $(event.target).text();
  groupList.remove("name", current);
  $("body").find("#filter").append("<div class=\"chip\"><span class=\"filtered-by\">" + current + "</span><i class=\"material-icons close-filter\">close</i></div>");

  // Build list of items to filter by
  var output = [];
  var currentGroups = $(".filtered-by").each(function (i, o) {
    output.push(o.textContent);
  });

  // Clear D3 SVG and run with new paramaters
  visuals.clear();
  visuals.run(output, false);

  // Reset show cycles button
  var current = $("body").find(".cycles-button");
  current.removeClass("remove-cycles");
  current.addClass("show-cycles");
  $("#cycle-button").text("Show Cycles");
});

$(document).on("click", ".close-filter", function () {
  /*
  Handles removal of filter.
  Will remove filter from DOM, add it back to the main list, and will
  reset D3.
  */
  var current = $(event.target).parent().find('span').text();
  groupList.add([{ name: current }]);

  // Build list of items to filter by
  var output = [];
  var currentGroups = $(".filtered-by").each(function (i, o) {
    output.push(o.textContent);
  });

  output.splice(output.indexOf(current), 1);

  // Clear D3 SVG and run with new paramaters
  visuals.clear();
  visuals.run(output, false);

  // Reset show cycles button
  var current = $("body").find(".cycles-button");
  current.removeClass("remove-cycles");
  current.addClass("show-cycles");
  $("#cycle-button").text("Show Cycles");

  // Remove any descriptive text
  $("#description").find("p").remove();
});

$(document).on("click", ".show-cycles", function () {
  /*
  Handle click of show cycles button.
  Will highlight cycles within the graph, then change the icon.
  */
  var current = $("body").find(".cycles-button");
  current.removeClass("show-cycles");
  current.addClass("remove-cycles");

  $("body").find(".ConceptNode").css("fill", "#EFEFEF").css("opacity", "0.6");
  $("body").find(".FactNode").css("fill", "#EFEFEF").css("opacity", "0.6");
  $("body").find(".MisconNode").css("fill", "#EFEFEF").css("opacity", "0.6");
  $("body").find(".ScaseNode").css("fill", "#EFEFEF").css("opacity", "0.6");

  $("body").find(".cycle").css("fill", "#F44336").css("opacity", "1");
  $("#cycle-button").text("Remove Cycles");
});

$(document).on("click", ".remove-cycles", function () {
  /*
  Handle click of remove cycles button.
  Will remove highlighted cycles within the graph.
  */
  var current = $("body").find(".cycles-button");
  current.removeClass("remove-cycles");
  current.addClass("show-cycles");
  $("#cycle-button").text("Show Cycles");

  $("body").find(".ConceptNode").css("fill", "#4783c1").css("opacity", "1");
  $("body").find(".FactNode").css("fill", "#FFC107").css("opacity", "1");
  $("body").find(".MisconNode").css("fill", "#e76351").css("opacity", "1");
  $("body").find(".ScaseNode").css("fill", "#55cd7c").css("opacity", "1");
});

$(document).on("mouseenter", ".chip", function () {
  /*
  Handle mouseover event of filters.
  Will fade unselected groups by reducing opacity.
  */
  var current = $(event.target).find('span').html();
  if (current !== undefined) {
    $("body").find(".node").css("fill", "#F5F5F5").css("opacity", "0.6");
    $("body").find(".ConceptNode." + current).css("fill", "#4783c1").css("opacity", "1");
    $("body").find(".FactNode." + current).css("fill", "#FFC107").css("opacity", "1");
    $("body").find(".MisconNode." + current).css("fill", "#e76351").css("opacity", "1");
    $("body").find(".ScaseNode." + current).css("fill", "#55cd7c").css("opacity", "1");
  }
  var content;

  if (current !== undefined || null) {
    var _iteratorNormalCompletion = true;
    var _didIteratorError = false;
    var _iteratorError = undefined;

    try {
      for (var _iterator = groupAttr[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
        var i = _step.value;

        if (i.name === current) {
          content = i.content;
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

    if (content === undefined) {
      content = "";
    }

    $("#description").append("<p class=\"valign\"><span class=\"highlight\"><b>" + current + "</b></span> " + content + "</p>");
  }

  // Reset show cycles button
  var current = $("body").find(".cycles-button");
  current.removeClass("remove-cycles");
  current.addClass("show-cycles");
  $("#cycle-button").text("Show Cycles");
});

$(document).on("mouseleave", ".chip", function () {
  /*
  Handle mouseleave event of filters.
  Will return faded groups to normal opacity.
  */
  $("#description").find("p").remove();

  $("body").find(".ConceptNode").css("fill", "#4783c1").css("opacity", "1");
  $("body").find(".FactNode").css("fill", "#FFC107").css("opacity", "1");
  $("body").find(".MisconNode").css("fill", "#e76351").css("opacity", "1");
  $("body").find(".ScaseNode").css("fill", "#55cd7c").css("opacity", "1");
});

$(document).ready(function () {
  $('.modal-trigger').leanModal();
});
