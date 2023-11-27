```python
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleImageFetcher(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        response = super(WebsiteSaleImageFetcher, self).shop(page=page, category=category, search=search, ppg=ppg, **post)
        product_ids = response.qcontext['products'].ids
        product_obj = request.env['product.template']
        products = product_obj.browse(product_ids)
        product_images = {}
        for product in products:
            product_images[product.id] = product.get_images()
        response.qcontext['product_images'] = product_images
        return response
```