$(function(){
	var code = mrdm();
	var aa=0,pw=0,cd=0,fx=0,call=0;
//	用户名
	$('#tell').blur(function(){
		tel();
	})
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
		tel();

		if($('.tt .msg_red').hasClass('true')){
			call =true
		}

		if(aa&&pw&&cd&&fx&&call){
			 $('form').submit()

		}
	})
	
	
	
	
	
	
	
	
	
	
	
	
	
	function tel(){
//		手机号
		call=0;
		sMobile = $('#tell').val()
		if(!(/^1[3|4|5|8][0-9]\d{8,8}$/.test(sMobile))){
			$('.tt .msg_red').css('display','block').html('手机号格式不对');
		}else{

			data= {
				'tel':$('#tell').val()
			}
			$.get('/checkename/',data,function (response) {
				if(response.status == '0'){
					$('.tt .msg_red').css('display','block').html(response.msg)
					$('.tt .msg_red').css('color','red')
					$('.un .msg_red').removeClass('true').addClass('false')
				}else if(response.status == '1'){
					$('.tt .msg_red').css('display','block').html(response.msg)
					$('.tt .msg_red').css('color','blue')
					$('.tt .msg_red').removeClass('false').addClass('true')


				}
			})





		}
	}
	
	
	
	
	
	function unDecide(){
//		用户名		
		aa=0;

		
		if($('#user_name').val()==""){
			$('.un .msg_red').css('display','block').html('用户名不能为空');
		} else{

			$('.un .msg_red').css('display','none');
			aa=true;

		}




	}
	function pwDecide(){
//		密码
		pw=0;
		if($('#user_pw').val()==''){
			$('.pw .msg_red').css('display','block').html('密码不能为空');
		}else{
			$('.pw .msg_red').css('display','none');
			pw=true;
		}
	}
	
	function cdDecide(){
		cd=0;
		var reg = new RegExp(code, "i");
		if($('#captcha').val()=="" || $('#captcha').val().length>4){
			$('.cd .msg_red').css('display','block').html('验证码不正确');
		}else if(!reg.test($('#captcha').val())){
			$('.cd .msg_red').css('display','block').html('验证码不正确');
		}else{
			$('.cd .msg_red').css('display','none');
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
