$(function(){
//	创建并修改搜索栏下边的文字样式
	$.get("json/recommend.json",function(res){
//		console.log(res);
		$.each(res, function() {
//			console.log(this);
//			找到推荐的内容并添加
			if(this.title=="recommend"){
//				console.log(this.details.url)
				var oLi = $("<li/>");
				$("<a href="+this.details.url+">"+this.details.title+"</a>").appendTo(oLi);
//						<li><a href="">iPhone 7</a></li>
				
				oLi.appendTo($('#recommend'));
			}
			
//		需要查找页面中异步构建的元素，所以要添加完成再调用
			r_choose();
		})
	});
	

	//轮播图片
	$.get("json/carousel.json",function(res){
		var i = true;
		$.each(res,function(){
			var oLi = $('<li/>');
			oLi.css('background',this.bg);
			//图片
			oLi.html("<a href="+this.aURL+">"+"<img src="+this.img+"></a>");
			oLi.appendTo($('.carouselArea .carousel'));
			//标题  必须重新创建一个标签
			var liTitle = $('<li/>');
//			第一个li添加css
			if(i){
				liTitle.addClass('cur');
				i=false;
			}
			liTitle.html("<a href="+this.aURL+">" + this.title + "</a>");
			liTitle.appendTo($('.carouselArea .small_Slider'));
		});
//		加载完 
		mian_animate();
	});
	$.get('json/commodity.json',function(res){
//		控制楼层
		var rwTop3cX = 0;
		var tcfX = 0;
		var lcfX = 0;
		var wsX = 0;
		var rwbX = 0;
		$.each(res, function() {
//			轮播图下边推荐
			if(this.title=='snapUp'){
				for(var i=0;i<this.data.length;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.snapUp').find('ul'));
				}
			}
//			轮播图下边推荐2
			if(this.title=='rightList'){
				for(var i=0;i<3;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.right_list').find('ul').eq(0));
				}
				for(var i=3;i<this.data.length;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.right_list').find('ul').eq(1));
				}
			}
//			楼中上下轮播
			if(this.title=="tcf"){
				for(var i=0;i<this.data.length;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.tcf').eq(tcfX).find('ul'));
				}
				tcfX++;
			}
//			楼中左右轮播
			if(this.title=='lcf'){
				for(var i=0;i<this.data.length;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.lcf').eq(lcfX).find('ul'));
				}
				lcfX++;
			}
//			楼中左右轮播下边两个
			if(this.title=='rwTop3c'){
//				console.log("控制楼层rw_top_3c下标： "+(rwTop3cX+1))
				for(var i=0;i<this.data.length;i++){
					var oLi = $('<li/>');
					oLi.html('<a href=page/shop.html?'+this.data[i].item+'>'+"<img src="+this.data[i].img+"></a>").appendTo($('.rw_top_3c').find('ul')[rwTop3cX]);
				}
				rwTop3cX++;
			}
//			百叶窗
			if(this.title=="windowShade"){
				for(var i=0;i<this.data.length;i++){
					var oLi = $('<li/>');
					var oSpan = $('<span/>');	
					var oDl = $('<dl/>')
					var oDd1 = $('<dd/>');	
					var oDd2 = $('<dd/>');
					var oA = $("<a href="+"page/shop.html?"+this.data[i].item+"/>");
					var oP1 = $('<p/>');	
					var oP2 = $('<p/>');	
					
					$("<h2><span class="+ (i==0?'one':'')+(i==1?'two':'')+(i==2?'thr':'') +">"+(i+1)+"</span>"+this.data[i].title+"</h2>").appendTo(oLi);
					oDd1.html($("<img src="+this.data[i].img+">"));
					oA.html($("<p>"+this.data[i].title+"</p><p>"+this.data[i].price+"</p>"));
					
					oDd1.addClass('window_shade_img');
					oDd2.addClass('window_shade_title');
					
					oDd1.appendTo(oDl);
					oA.appendTo(oDd2);
					oDd2.appendTo(oDl);
					oDl.appendTo(oLi);
					oLi.appendTo($('.window_shade').find('ul')[wsX]);
				
				}
				wsX++;
			}
//			下边5个	
			if(this.title=="rwBottom"){
				$.each(this.data, function() {
					var oUl = $('<ul/>');
					$('<li><a href='+'page/shop.html?'+this.item+'><img src='+this.img+'></a></li>').appendTo(oUl);
					$('<li><a href='+'page/shop.html?'+this.item+'>'+this.title+'</a></li>').appendTo(oUl);
					$('<li><em>'+this.price+'</em><del>'+this.LRP+'</del></li>').appendTo(oUl);
//									<ul>
//										<li><a href="#"><img src="img/138_05097149322678475_240.jpg"/></a></li>
//										<li><a href="#">联想Lenovo C5030  I35005U4G1TGRW-10(W)(E)</a></li>
//										<li><em>￥4229.00</em><del>￥4800.00</del></li>
//									</ul>
					oUl.appendTo($('.rw_bottom')[rwbX]);
				});
				rwbX++;
			}
			
			
			
		
		});
		
			//楼层中的轮播
			flCarousel();
			//	百叶窗
			shutter();

	})
	
	
	
	
	
	
	
	
	

//	导航切换 没有动态获取了0.0
	headNav();

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
})

