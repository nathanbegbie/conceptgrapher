
  $(document).ready(function(){
    $("#group1").click(function(){
      $("body").find(".1").css("fill", "#"+num()+num()+num());
    });
  });

  function num() {
    return Math.floor(Math.random()*256).toString(16);
  }
