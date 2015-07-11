;$(function(){
  $('.t-optional').hide();
  
  $('#identi div').mouseover(function(){
    if(!$(this).hasClass('active'))
      $(this).addClass('mouseover');
  })
  $('#identi div').mouseleave(function(){
    $(this).removeClass('mouseover');
  })
  $('#identi div').eq(0).click(function(){
    $(this).addClass('active').siblings().removeClass("active");
    $('.t-optional').hide();
    $('.s-optional').show();
    $('form div:eq(1) span:first').text('学号');
  });
  $("#identi div").eq(1).click(function(){
    $(this).addClass('active').siblings().removeClass('active');
    $('.t-optional').show();
    $('.s-optional').hide();
    $('form div:eq(1) span:first').text('学工号');
  })
  
});