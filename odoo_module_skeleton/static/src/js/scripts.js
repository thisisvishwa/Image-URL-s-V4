odoo.define('odoo_module_skeleton.product_template', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $(document).ready(function () {
        $('.product_template').each(function () {
            var $product = $(this);
            var mainImageUrl = $product.data('main-image-url');
            var extraMediaUrls = $product.data('extra-media-urls');

            if (mainImageUrl) {
                ajax.jsonRpc('/odoo_module_skeleton/fetch_image', 'call', {
                    'url': mainImageUrl
                }).then(function (data) {
                    if (data.result) {
                        $product.find('.main-image').attr('src', data.result);
                    }
                });
            }

            if (extraMediaUrls) {
                extraMediaUrls.forEach(function (url) {
                    ajax.jsonRpc('/odoo_module_skeleton/fetch_image', 'call', {
                        'url': url
                    }).then(function (data) {
                        if (data.result) {
                            var $img = $('<img>').attr('src', data.result);
                            $product.find('.extra-media').append($img);
                        }
                    });
                });
            }
        });
    });
});