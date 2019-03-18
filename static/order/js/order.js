$(function () {
    var sum = 0
    var num = 0
    $('.total').each(function () {
        sum += parseInt($(this).attr('price'))
    })
    $('.num').each(function () {
        num += parseInt($(this).attr('n'))
    })
    $('.all').html('￥'+sum)
    $('#num').html(num)
    
    $('.nextStep a').click(function () {
        datas = {
            'orderid':$(this).attr('orderid')
        }
        $.get('/pay/',datas,function (response) {
            if (response.status == 1){
                console.log(response.alipayurl)
                window.open(response.alipayurl, target='_self')

            }
        })
    })

})