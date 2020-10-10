$(function () {
    $('#submit').click(function () {
        $.ajax({
            url: '/login_auth/',
            type: 'post',
            data: {
                'usr': $('#id_usr').val(),
                'pwd': $('#id_pwd').val(),
            },
            success: function (data) {
                data = JSON.parse(data)
                if (data.usr) {
                    location.href = '/home/';
                } else {
                    $('#login_auth').html(data.msg)
                }
            }
        })
    })
})