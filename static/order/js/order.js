$(function () {
    var sum = 0
    var num = 0
    $('.total').each(function () {
        sum += parseInt($(this).attr('price'))
        console.log($(this).html)
    })
    $('.num').each(function () {
        num += parseInt($(this).attr('n'))
    })
    $('.all').html('￥'+sum)
    $('#num').html(num)

})