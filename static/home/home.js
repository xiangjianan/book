$(function () {
    // 修改作者信息
    $('.change_auth').click(function () {
        // 找到input标签的value值
        let val = $(this).parent().parent().prev().children().children().val();
        // 找到input标签的name值
        let name = $(this).parent().parent().prev().children().children().attr('name');
        // 获取auth_id
        let auth_id = parseInt(name);
        $.ajax({
            url: `/app_home/${auth_id}/change_auth/`,
            type: 'post',
            data: {
                auth_name: val,
            },
            success: function (data) {
                if (data) {
                    location.href = '/app_home/author/';
                }
            }
        })
    })

    // 修改出版社信息
    $('.change_pub').click(function () {
        // 找到input标签的value值
        let val = $(this).parent().parent().prev().children().children().val();
        // 找到input标签的name值
        let name = $(this).parent().parent().prev().children().children().attr('name');
        // 获取auth_id
        let pub_id = parseInt(name);
        $.ajax({
            url: `/app_home/${pub_id}/change_pub/`,
            type: 'post',
            data: {
                pub_name: val,
            },
            success: function (data) {
                if (data) {
                    location.href = '/app_home/publish/';
                }
            }
        })
    })

    // 修改书籍信息
    $('.change_book').click(function () {
        // 找到input标签的value值
        let val = $(this).parent().parent().prev().children().children().val();
        // 找到input标签的name值
        let name = $(this).parent().parent().prev().children().children().attr('name');
        // 获取auth_id
        let book_id = parseInt(name);
        // 找到作者标签checked的value值，并打包成数组
        let auth_val_list=[];
        $.each($(`#modal${book_id} input:checkbox:checked`),function(){
            auth_val_list.push($(this).val())
        });
        // 找到出版社标签的value值
        let pub_val = $(this).parent().parent().prev().children().next().next().children().val();

        $.ajax({
            url: `/app_home/${book_id}/change_book/`,
            type: 'post',
            data: {
                book_name: val,
                pub_id: pub_val,
                auth_id_list: JSON.stringify(auth_val_list),
            },
            success: function (data) {
                if (data) {
                    location.href = data;
                }
            }
        })
    })
})