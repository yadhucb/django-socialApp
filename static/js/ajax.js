$(document).ready(function () {

    // =========== add comment ====================

    $('.add_comment').click(function (e) {
        console.log('clickkkkks')
        e.preventDefault();

        var comment = $(this).closest('.comment').find('.comment_input').val();
        if (comment != '') {
            var token = $('input[name=csrfmiddlewaretoken]').val()
            var blog_id = $(this).closest('.comment').find('.blog_id').val();
            console.log(comment, token, 'iddddd', blog_id)

            $.ajax({
                method: 'POST',
                url: '/blog/add-comment/',
                data: {
                    'comment': comment,
                    'blog_id': blog_id,
                    csrfmiddlewaretoken: token

                },
                success: function (data) {
                    $('.comment_body' + blog_id).load(location.href + " .comment_body" + blog_id);
                    $('.comment_count' + blog_id).load(location.href + " .comment_count" + blog_id);
                    document.getElementById("commentForm" + blog_id).reset();

                }
            })
        }
    })

    $(document).on('click', '.like_btn', function (e) {
        console.log('likessssss')
        e.preventDefault();

        var is_liked = $(this).closest('.like_container').find('.is_liked').val();
        console.log('like_text', is_liked)
        if (is_liked === 'True') {
            var token = $('input[name=csrfmiddlewaretoken]').val()
            var blog_id = $(this).closest('.like_container').find('.blog_id').val();
            console.log('blog', blog_id)
            console.log('blog', token)
            $.ajax({
                method: 'POST',
                url: '/blog/unlike/',
                data: {
                    'is_liked': is_liked,
                    'blog_id': blog_id,
                    csrfmiddlewaretoken: token

                },
                success: function (data) {
                    $('.like_btn' + blog_id).load(location.href + " .like_btn" + blog_id);
                    $('.like_count' + blog_id).load(location.href + " .like_count" + blog_id);



                }
            })

        }

        else {
            var token = $('input[name=csrfmiddlewaretoken]').val()
            var blog_id = $(this).closest('.like_container').find('.blog_id').val();
            console.log('blog', blog_id)
            console.log('blog', token)
            $.ajax({
                method: 'POST',
                url: '/blog/like/',
                data: {
                    'is_liked': is_liked,
                    'blog_id': blog_id,
                    csrfmiddlewaretoken: token

                },
                success: function (data) {
                    $('.like_btn' + blog_id).load(location.href + " .like_btn" + blog_id);
                    $('.like_count' + blog_id).load(location.href + " .like_count" + blog_id);

                }
            })

        }
    })

    // =========== follow ============

    $(document).on('click', '.follow_btn', function (e) {
        console.log('foloowwww')
        e.preventDefault();

        var follow_user_id = $(this).closest('.follow_container').find('.follow_user_id').val();
        console.log('like_text', follow_user_id)
        var token = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            method: 'POST',
            url: '/user/follow/',
            data: {
                'follow_user_id': follow_user_id,
                csrfmiddlewaretoken: token

            },
            success: function (data) {
                $('.followed' + follow_user_id).html('Followed');
                $('.following_count').load(location.href + ' .following_count');
            }
        })
    })


});