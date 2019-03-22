$(function () {
    $('button').click(function () {

        datas = {
            'goodsid':$(this).attr('goodsid')

        }
        console.log($(this).attr('goodsid'))
        $.get('/goodsdown/',datas,function (response) {
            if(response.states == '1'){
                alert('操作成功')
                window.location.reload()
            }
        })

    })
})