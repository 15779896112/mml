$(function () {
    $('.ping').click(function () {
        goodsid = $(this).attr('goods')
        identifier = $(this).children('span').attr('identifier')
        $('.goodsname').val(goodsid)
        $('.this_identifier').val(identifier)
        // console.log($('.this_identifier').val(identifier))
        $(this).parent().siblings().css('display','block')
        console.log(1111)


    })
    $('.order button').click(function () {
        identifier = $(this).attr('identifier')
        datas={
            'identifier':identifier
        }
        $.get('/getgoods/',datas,function (response) {
            if(response.status == '1'){
                alert('成功确认收货')
            }
        })
    })


    // $('#start_pay').click(function () {
    //     identifier = $(this).attr('identifier')
    //     datas={
    //         'identifier':identifier
    //     }
    //     $.get('/start_pay/',datas,function (response) {
    //
    //     })
    // })
})