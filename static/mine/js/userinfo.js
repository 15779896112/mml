$(function () {
    $.get('/getuserinfo/',function (response) {
        $('#user_name').val(response.name)
        $('#sex').val(response.sex)
        $('#old').val(response.old)



    })






})