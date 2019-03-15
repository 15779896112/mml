$(function(){
	var code = mrdm();
	var un=0,pw=0,cd=0,fx=0;
	$('input').focus(function(){
		$(this).parent().find('.msg').css('display','block').stop().animate({
			'top':'-29'
		},500)
	})
	$('input').blur(function(){
		$(this).parent().find('.msg').stop().animate({
			'top':'-35'
		},500).css('display','none');
		
	})
//	用户名
	$('#user_name').blur(function(){
		unDecide();
	})
	$('#user_pw').blur(function(){
		pwDecide();
	})
	$('#captcha').blur(function(){
		cdDecide();
	})
	$('#nowReg').click(function(){
		unDecide();
		pwDecide();
		cdDecide();
		fxDecide();
		if(un&&pw&&cd&&fx){
			var str = "";
			if($.cookie('user')){
				str = $.cookie('user');
				str += "?"+$('#user_name').val()+","+$('#user_pw').val();
			}else{
				str = $('#user_name').val()+","+$('#user_pw').val();
			}
			$.cookie('user',str,{expires:7, path:"/"});
			console.log('存储成功');
			$('#main').css({
				'height':"300px",
				'text-align':'center',
				'color':'#02AFFF',
				'line-height':"300px",
				"font-size": "40px"
			}).html('注册成功');
			setTimeout(function(){
				window.location.href='login.html';
			},1500)

		}
	})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	function unDecide(){
//		用户名		
		un=0;
		
		if($('#user_name').val()==""){
			$('.un .msg_red').css('display','block').html('用户名不能为空');
			$('.un i').css('display','block').css('background','url(../img/error.png)')
		}
		else if($('#user_name').val()==""){
			$('.un .msg_red').css('display','block').html('用户名不能为空');
			$('.un i').css('display','block').css('background','url(../img/error.png)')
		}else{
			$('.un .msg_red').css('display','none');
			if($.cookie('user')){
				var ur = $.cookie('user');
				var str = ur.split('?')

			}
			$('.un .msg_red').css('display','none');
			$('.un i').css('display','block').css('background','url(../img/correct.png)')
			un=true;
		}	
	}
	function pwDecide(){
//		密码
		pw=0;
		if($('#user_pw').val()==''){
			$('.pw .msg_red').css('display','block').html('密码不能为空');
			$('.pw i').css('display','block').css('background','url(../img/error.png)')
		}else{
			$('.pw .msg_red').css('display','none');  
			$('.pw i').css('display','block').css('background','url(../img/correct.png)')
			pw=true;
		}
	}
	
	function cdDecide(){
		cd=0;
		var reg = new RegExp(code, "i");
		if($('#captcha').val()=="" || $('#captcha').val().length>4){
			$('.cd .msg_red').css('display','block').html('验证码不正确');
			$('.cd i').css('display','block').css('background','url(../img/error.png)')
		}else if(!reg.test($('#captcha').val())){
			$('.cd .msg_red').css('display','block').html('验证码不正确');
			$('.cd i').css('display','block').css('background','url(../img/error.png)')
		}else{
			$('.cd .msg_red').css('display','none');  
			$('.cd i').css('display','block').css('background','url(../img/correct.png)')
			cd=true;
		}
	}
	
	function fxDecide(){
		fx=0;
		if(!$('#serviceContract').is(':checked')){
			$('#nowReg').parent().find('.msg_red').css('display','block');
		}
		else{
			$('#nowReg').parent().find('.msg_red').css('display','none');
			fx=true;
		}
	}
//	code

	$('.code').html(code);
	$('.code,.code1').on('click',function(){
		code = mrdm();
		$('.code').html(code);
		return false;
	})



	function mrdm(){
		var code = "";
		for (var i=0;i<4;i++) {
			if(parseInt(Math.random()*2)){
				code += parseInt(Math.random()*10);
			}else{
				code += String.fromCharCode(parseInt(Math.random()*26)+65);
			}
		}
		return code;
	}
	
	
	
})
