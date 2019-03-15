$(function () {

    $('#goodstype').click(function () {
        if($(this).attr('status')=='false'){
            $('#main .menu').css('display', 'block')
            $(this).attr('status','true')

        }else {
            $(this).attr('status','false')
            $('#main .menu').css('display', 'none')

        }
    })

    $('.menu ul li').on('click',function () {
        // $('#main .menu ul .sub_menu')

        $('#main .menu ul li .sub_menu').css('display', 'block')
        $('.sub_menu .sm_tle .fenlei').children().remove()
        $li = $(this)
        $(this).siblings().removeClass('showtype')
        $(this).attr('class','showtype')
        datas = {
            'typeid':$li.attr('typeid')
        }

        $.get('/subclass/',datas,function (response) {
            // console.log(response.childtype_list)
            var lis = response.childtype_list
            for (var i=0;i<lis.length;i++) {
                var name = lis[i]['name']
                var  id = lis[i]['id']

                var str = '<div class="aa" id='+ id +'><a href="'+'/index/'+id+'">'+name+'</a></div>'

                $('.sub_menu .sm_tle .fenlei').append(str)




            }
            // $('.sub_menu .sm_tle .fenlei .aa').on('click',function () {
            //     var fatherid = $(this).attr('id')
            //     window.open()
            //
            //
            //
            //
            // })
            $('#main .menu ul .sub_menu').css('display', 'block')





        })




    })


     //








})


