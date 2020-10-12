$(function (){
    $('.change-btn').click(function (){
        $.ajax({
            url: '/app_home/change_auth/',
            type: 'post',
            data: {
                'auth_name': $('#id_usr').val(),
            },
            success: function (data) {
                data = JSON.parse(data)
                console.log(data)
                if (data.usr) {
                    location.href = '/app_home/home/';
                } else {
                    $('#login_auth').html(data.msg)
                }
            }
        })
    })
})