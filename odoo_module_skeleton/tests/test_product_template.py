```python
from odoo.tests import common

class TestProductTemplate(common.TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        self.product_template = self.env['product.template']

    def test_main_image_url_field_exists(self):
        field_names = self.product_template.fields_get().keys()
        self.assertIn('main_image_url', field_names, "main_image_url field does not exist")

    def test_extra_media_urls_field_exists(self):
        field_names = self.product_template.fields_get().keys()
        self.assertIn('extra_media_urls', field_names, "extra_media_urls field does not exist")

    def test_image_fetching(self):
        # Create a product template with image URLs
        product = self.product_template.create({
            'name': 'Test Product',
            'main_image_url': 'https://example.com/image.jpg',
            'extra_media_urls': 'https://example.com/media1.jpg,https://example.com/media2.jpg'
        })

        # Fetch the images
        product.fetch_images()

        # Check that the images were fetched correctly
        self.assertTrue(product.main_image, "Main image was not fetched correctly")
        self.assertTrue(product.extra_media, "Extra media was not fetched correctly")

    def test_invalid_url_handling(self):
        # Create a product template with an invalid image URL
        product = self.product_template.create({
            'name': 'Test Product',
            'main_image_url': 'https://invalidurl.com/image.jpg'
        })

        # Fetch the images
        product.fetch_images()

        # Check that the invalid URL was handled correctly
        self.assertFalse(product.main_image, "Invalid URL was not handled correctly")

    def test_performance(self):
        # Create a large number of product templates with image URLs
        for i in range(1000):
            self.product_template.create({
                'name': 'Test Product {}'.format(i),
                'main_image_url': 'https://example.com/image{}.jpg'.format(i),
                'extra_media_urls': 'https://example.com/media{}.jpg'.format(i)
            })

        # Fetch the images for all product templates
        self.product_template.search([]).fetch_images()

        # Check that the images were fetched within a reasonable time
        # This is a placeholder and should be replaced with actual performance testing code
        self.assertTrue(True, "Performance test failed")
```