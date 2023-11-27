{
    'name': 'Dynamic Image Fetcher for Odoo 17 CE E-commerce',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Fetches and displays product images from external URLs',
    'sequence': 1,
    'author': 'Your Name',
    'website': 'Your Website',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_form_view.xml',
        'data/data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
    This module fetches and displays product images and extra product media from external URLs on the e-commerce website, without storing these images in the Odoo database.
    """,
}