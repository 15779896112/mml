$(function () {
    // var goodsid = null
    $('a').click(function () {
        goodsid = $(this).attr('goods')
        $('.goodsname').val(goodsid)
        $(this).parent().siblings().css('display','block')


    })
    // $('button').click(function () {
    //
    //      $('form').submit()
    //
    //
    //     alert('发表成功')
    //
    // })

})