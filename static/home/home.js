$(function () {
    // 修改作者信息
    $('.change_auth').click(function () {
        // 找到input标签的value值
        let val = $(this).parent().parent().prev().children().children().val();
        // 找到input标签的name值
        let name = $(this).parent().parent().prev().children().children().attr('name');
        // 获取auth_id
        auth_id = parseInt(name);
        console.log(val);
        console.log(name);
        console.log(auth_id);
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
        pub_id = parseInt(name);
        console.log(val);
        console.log(name);
        console.log(pub_id);
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
        book_id = parseInt(name);
        // 找到作者标签checked的value值
        let auth_val_list=[];
        $.each($(`#modal${book_id} input:checkbox:checked`),function(){
            auth_val_list.push($(this).val())
        });
        console.log(auth_val_list)
        // 找到出版社标签的value值
        let pub_val = $(this).parent().parent().prev().children().next().next().children().val();
        console.log(val);
        console.log(pub_val);
        console.log(auth_val_list);

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