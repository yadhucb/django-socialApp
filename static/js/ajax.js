$(document).ready(function () {

    // =========== add to cart ====================

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


                }
            })

        }
    })


    // =============== qty plus in cart =============

    $(document).on('click', '.plus_btn', function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var quantity = $(this).closest('.qty_cart').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken').val()
        if (quantity < 5) {
            quantity++;
            $(this).closest('.qty_cart').find('.qty_input').val(quantity)
        }

        $.ajax({
            method: 'POST',
            url: '/cart/change-qty/',
            data: {
                'product_id': product_id,
                'quantity': quantity,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
            }
        })
    })

    // =============== qty minus in cart =============

    $(document).on('click', '.minus_btn', function (e) {
        e.preventDefault;
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var quantity = $(this).closest('.qty_cart').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken').val()

        if (quantity > 1) {
            quantity--
            $(this).closest('.qty_cart').find('.qty_input').val(quantity)
        }

        $.ajax({
            method: 'POST',
            url: '/cart/change-qty/',
            data: {
                'product_id': product_id,
                'quantity': quantity,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
            }


        })
    })

    // =============== qty delete in cart =============

    $(document).on('click', '.dlt_btn', function (e) {
        e.preventDefault;
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var token = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            method: 'POST',
            url: '/cart/',
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
                $('.cart_num').load(location.href + " .cart_num");
            }

        })
    })

    // =========== address save =============

    $(document).on('click', '.address_save_btn', function (e) {
        e.preventDefault
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var name = $('input[name=name]').val()
        var address = $("textarea[name=address]").val()
        var state = $('select[name=state]').val()
        var pin = $('input[name=pin]').val()
        var mob = $('input[name=mob]').val()

        if (name === '' || address === '' || state === '' || pin === '' || mob === '') {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">All fields are required!</P>'
        }
        else if (mob.length != 10) {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">Invalid mobile! Mobile number must be 10 digits</P>'
        }
        else if (pin.length != 6) {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">Invalid pin code! PIN code must be 6 digits</P>'
        }
        else {
            document.getElementById('btn-close').click()

            $.ajax({
                method: 'POST',
                url: '/profiles/address/',
                data: {
                    csrfmiddlewaretoken: token,
                    'name': name,
                    'address': address,
                    'state': state,
                    'pin': pin,
                    'mob': mob
                },

                success: function (response) {
                    $('.load_address').load(location.href + ' .load_address')
                }
            })
        }
    })

    // =========== address delete =============

    $(document).on('click', '.address_delete_btn', function (e) {
        e.preventDefault;
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var address_id = $(this).closest('.address_closest_cls').find('.address_id').val()
        $.ajax({
            method: 'POST',
            url: '/profiles/address-delete/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },

            success: function (data) {
                $('.load_address').load(location.href + ' .load_address')
            }
        })
    })

    // =========== address edit =============

    $(document).on('click', '.address_edit_btn', function (e) {
        e.preventDefault;
        $(".address_form").removeClass('address_remove')
        $(".address_form").addClass('address_add')
        var token = $('input[name=csrfmiddlewaretoken]').val()
        address_id = $(this).closest('.address_closest_cls').find('.address_id').val()
        $.ajax({
            method: 'POST',
            url: '/profiles/address-edit/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },

            success: function (data) {
                $('input[name=name]').val(data.name)
                $("textarea[name=address]").val(data.address)
                $('select[name=state]').val(data.state)
                $('input[name=pin]').val(data.pin)
                $('input[name=mob]').val(data.mob)
            }
        })
    })

    // =========== address default =============

    $(document).on('click', '.address_default_btn', function (e) {
        e.preventDefault;
        token = $('input[name=csrfmiddlewaretoken]').val()
        address_id = $(this).closest('.address_closest_cls').find('.address_id').val()

        $.ajax({
            method: 'POST',
            url: '/profiles/address-default/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },
            success: function (data) {
                $('.address_load').load(location.href + ' .address_load')
                $(".address_load1").load(location.href + ' .address_load1')
            }
        })
    })


});