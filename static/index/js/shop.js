$(function () {


//	购买数量
    $('.count_sum').find('a').eq(0).on('click', function () {
        var sum = $('#count').val();
        sum++;
        $('#count').val(sum);
        return false;
    })
    $('.count_sum').find('a').eq(1).on('click', function () {
        var sum = $('#count').val();
        sum--;
        if (sum <= 0) {
            $('#count').val(1);
            return false;
        }
        $('#count').val(sum);
        return false;
    })


//	立即购买
    $('#nowBuy').on('click', function () {
        adminCart();
        setTimeout(function () {
            window.location.href = 'cart.html';
        }, 1500)
        return false;
    })

//	添加到购物车

    $('#addCart').on('click', function () {
        var num = $('#count').val()
        var goodsid = $(this).attr('class')
        var datas = {
            'num': num,
            'goodsid':goodsid

        }
        $.get('/addcart/', datas, function (response) {

            if(response.status == '1'){
                $('.shoppingCart span .num').html(response.num)
                $('.shoppingCart span .alwaysNum').html(response.sum)

                $('.shoppingCart').show()
            }else{
                 // $.cookie('back', 'shop', {expires: 3, path: '/'})

                window.open('/login/', '_self')
            }
        })





    })

//	关闭购物信息
    $('.close').on('click', function () {
        $('.shoppingCart').hide()

    })


})



