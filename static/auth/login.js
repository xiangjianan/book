$(function () {
    $('#submit').click(function () {
        $.ajax({
            url: '/app_auth/login/',
            type: 'post',
            data: {
                'usr': $('#id_usr').val(),
                'pwd': $('#id_pwd').val(),
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