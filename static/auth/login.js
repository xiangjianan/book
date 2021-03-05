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
                // 认证成功，进入home
                if (data.usr) {
                    location.href = '/app_home/home/';
                } 
                // 认证失败，提示错误信息
                else {
                    $('#login_auth').html(data.msg)
                }
            }
        })
    })
})