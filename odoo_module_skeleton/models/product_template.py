```python
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    main_image_url = fields.Char(string='Main Image URL')
    extra_media_urls = fields.Char(string='Extra Media URLs')
```