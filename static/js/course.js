;$(function(){
  
  $('#source').hide();

  $("#nav-list li").eq(0).click(function(){
    $(this).addClass('nav-list-active').siblings().removeClass('nav-list-active');
    $("#tip").show();
    $('#source').hide();
  });
  $("#nav-list li").eq(1).click(function(){
    $(this).addClass('nav-list-active').siblings().removeClass('nav-list-active');
    $("#tip").hide();
    $('#source').show();
  });
});