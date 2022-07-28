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

    // =========== edit comment ====================

    // =========== get edit comment ====================

    $(document).on('click', '.edit_comment', function (e) {
        console.log('clickkkkks')
        e.preventDefault();

        var comment_id = $(this).closest('.edit_comment_container').find('.comment_id').val();

        $.ajax({
            method: 'GET',
            url: '/blog/edit-comment/',
            data: {

                'comment_id': comment_id

            },
            success: function (data) {
                $('.comment_input').val(data.comment);
                $(".add_comment").addClass("d-none");
                $(".edit_comment_btn").removeClass("d-none");
            }
        })

    })

    // =========== post edit comment ===========
    $(document).on('click', '.edit_comment_btn', function (e) {
        e.preventDefault();
        var blog_id = $(this).closest('.comment').find('.blog_id').val();
        var comment = $(this).closest('.comment').find('.comment_input').val();
        console.log('bloggg111', blog_id)
        if (comment != '') {
            var token = $('input[name=csrfmiddlewaretoken]').val()

            $.ajax({
                method: 'POST',
                url: '/blog/edit-comment/',
                data: {
                    'comment': comment,
                    csrfmiddlewaretoken: token

                },
                success: function (data) {
                    $('.comment_body' + blog_id).load(location.href + " .comment_body" + blog_id);
                    $(".add_comment").removeClass("d-none");
                    $(".edit_comment_btn").addClass("d-none");
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

    // ======== remove follower ==========

    $(document).on('click', '.remove_follower_btn', function (e) {
        console.log('foloowwww')
        e.preventDefault();

        var follower_user_id = $(this).closest('.follower_container').find('.follower_user_id').val();
        console.log('like_text', follower_user_id)
        var token = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            method: 'POST',
            url: '/user/remove-follower/',
            data: {
                'follower_user_id': follower_user_id,
                csrfmiddlewaretoken: token

            },
            success: function (data) {
                $('.follower' + follower_user_id).html('Removed');
                $('.followers_count').load(location.href + ' .followers_count');
            }
        })
    })

    // ======== unfollow ==========

    $(document).on('click', '.unfollow_btn', function (e) {
        console.log('foloowwww')
        e.preventDefault();

        var following_user_id = $(this).closest('.following_container').find('.following_user_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            method: 'POST',
            url: '/user/unfollow/',
            data: {
                'following_user_id': following_user_id,
                csrfmiddlewaretoken: token

            },
            success: function (data) {
                $('.following' + following_user_id).html('Removed');
                $('.following_count').load(location.href + ' .following_count');
            }
        })
    })
});