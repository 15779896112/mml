$(function () {

    $('.order button').click(function () {
        identifier = $(this).attr('identifier')
        datas={
            'identifier':identifier
        }
        $.get('/sendgoods/',datas,function (response) {
            if(response.status == '1'){
                alert('发货成功')
                window.location.reload()
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