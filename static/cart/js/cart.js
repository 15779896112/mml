$(function () {


    $('input:first').click(function () {
        if($('input:first').is(':checked')) {
            $('input').each(function () {

                $(this).prop("checked", 'true')
            })
        }else {
            $('input').each(function () {

                $(this).removeAttr("checked")
            })
        }

    })


    $('input').click(function () {
        var check
        $(this).is(':checked')?check='yes':check='no'
        datas = {
            'cartid':$(this).attr('cartid'),
            'check':check
        }
        $.get('/isselect',datas,function (response) {
            if(response.status == '1'){
               $('.commodityPrice h2 .total').html(response.sum)
            }

        })
    })

    $('.dell').click(function () {
        datas = {
            'cartid':$(this).attr('cartid')
        }
        var $that = $(this)
         $.get('/dell/',datas,function (response) {
            if(response.status == '1'){
                $that.parent().parent().remove()
               $('.commodityPrice h2 .total').html(response.sum)
            }

        })
    })
    



})