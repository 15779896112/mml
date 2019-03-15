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
})


