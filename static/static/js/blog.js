/**

 @Name：layui.blog 闲言轻博客模块
 @Author：徐志文
 @License：MIT
 @Site：http://www.layui.com/template/xianyan/
    
 */
layui.define(['element', 'form','laypage','jquery','laytpl'],function(exports){
  var element = layui.element
  ,form = layui.form
  ,laypage = layui.laypage
  ,$ = layui.jquery
  ,laytpl = layui.laytpl;
  

  //statr 分页
  
  laypage.render({
    elem: 'test1' //注意，这里的 test1 是 ID，不用加 # 号
    ,count: 50 //数据总数，从服务端得到
    ,theme: '#1e9fff'
  });
  
  // end 分頁
 


  // start 导航显示隐藏
  
  $("#mobile-nav").on('click', function(){
    $("#pop-nav").toggle();
  });

  // end 导航显示隐藏




  //start 评论的特效
  
  (function ($) {
    $.extend({
        tipsBox: function (options) {
          options = $.extend({
            obj: null,  //jq对象，要在那个html标签上显示
            str: "+1",  //字符串，要显示的内容;也可以传一段html，如: "<b style='font-family:Microsoft YaHei;'>+1</b>"
            startSize: "12px",  //动画开始的文字大小
            endSize: "30px",    //动画结束的文字大小
            interval: 600,  //动画时间间隔
            color: "red",    //文字颜色
            callback: function () { }    //回调函数
          }, options);

          $("body").append("<span class='num'>" + options.str + "</span>");

          var box = $(".num");
          var left = options.obj.offset().left + options.obj.width() / 2;
          var top = options.obj.offset().top - 10;
          box.css({
            "position": "absolute",
            "left": left + "px",
            "top": top + "px",
            "z-index": 9999,
            "font-size": options.startSize,
            "line-height": options.endSize,
            "color": options.color
          });
          box.animate({
            "font-size": options.endSize,
            "opacity": "0",
            "top": top - parseInt(options.endSize) + "px"
          }, options.interval, function () {
            box.remove();
            options.callback();
          });
        }
      });
  })($); 

  function niceIn(prop){
    prop.find('i').addClass('niceIn');
    setTimeout(function(){
      prop.find('i').removeClass('niceIn'); 
    },1000);    
  }

  $(function () {
    $(".like").on('click',function () {
      var aid =$(this).attr("aid");
      $.ajax({
                url:"/zan/"
                ,data:{"id":aid}
                ,type:"post"
                ,dataType:"json"
                ,success:function (data) {
                    if(data.code==0){
                      console.log("ssss")
                    }else {
                        layer.msg(data.msg)
                    }
                }
            })
      if(!($(this).hasClass("layblog-this"))){
        this.text = '已赞';
        $(this).addClass('layblog-this');
        $.tipsBox({
          obj: $(this),
          str: "+1",
          callback: function () {
          }
        });
        niceIn($(this));
        layer.msg('点赞成功', {
          icon: 6
          ,time: 1000
        })
      }
    });
  });

  //end 评论的特效


  // start点赞图标变身
  $('#LAY-msg-box').on('click', '.info-img', function(){
    $(this).addClass('layblog-this');
  })


  // end点赞图标变身

      //end 提交
  $('#item-btn').on('click', function(){
    var elemCont = $('#LAY-msg-content')
    ,content = elemCont.val();
    if(content.replace(/\s/g, '') == ""){
      layer.msg('请先输入留言');
      return elemCont.focus();
    }

    var view = $('#LAY-msg-tpl').html()

    //模拟数据
    ,data = {
      username: '闲心'
      ,avatar: '../static/static/images/info-img.png'
      ,praise: 0
      ,content: content
    };
    var html = '\t\t<div class="info-box">\n' +
    '\t\t\t<div class="info-item">\n' +
    '\t\t\t\t<img class="info-img" src="'+data.avatar+'" alt="">\n' +
    '\t\t\t  <div class="info-text">\n' +
    '\t\t\t\t\t<p class="title">\n' +
    '\t\t\t\t\t  <span class="name">'+data.username+'</span>\n' +
    '\t\t\t\t\t  <span class="info-img">\n' +
    '\t\t\t\t\t  \t<i class="layui-icon layui-icon-praise"></i>\n' +
    '\t\t\t\t\t  \t'+data.praise+'\n' +
    '\t\t\t\t\t \t</span>\n' +
    '\t\t\t\t\t</p>\n' +
    '\t\t\t\t\t<p class="info-intr">\n' +
    '\t\t\t\t\t\t'+content+'\n' +
    '\t\t\t\t\t</p>\n' +
    '\t\t\t  </div>\n' +
    '\t\t\t</div>\n' +
    '\t\t</div>'
    //模板渲染
      $.ajax({
          url:"/message/",
          type:"post",
          data:{"message":content},
          dataType: "json",
          success:function (data) {
              console.log(data)
              if(data.code == 0){
                $('#LAY-msg-box').prepend(html);
                layer.msg('留言成功', {
                  icon: 1
                });
              }
          }
      })


  })

  // start  图片遮罩
  var layerphotos = document.getElementsByClassName('layer-photos-demo');
  for(var i = 1;i <= layerphotos.length;i++){
    layer.photos({
      photos: ".layer-photos-demo"+i+""
      ,anim: 0
    }); 
  }
  // end 图片遮罩


  //输出test接口
  exports('blog', {});

  //login -----------------
  //监听提交--login
  //自定义验证规则
  form.verify({
    title: function(value){
      if(value.length < 1){
        return '用户名不能为空';
      }
    }
    ,pass: [/(.+){6,8}$/, '密码必须6到12位']
    ,content: function(value){
      layedit.sync(editIndex);
    }
  });

  form.on('submit(loginbtn)', function(data){
    $.ajax({
      url:"/login/",
      type:"post",
      data:data.field,
      dataType: "json",
      success:function (data) {
          if(data.code == 1){
              layer.msg(data.msg)
          }else if (data.code == 0){
            window.location.href ="/manage/";
          }
      }
    });
    return false;
  });

});  
