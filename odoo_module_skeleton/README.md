# Odoo 17 CE E-commerce Image Fetcher Module

This module dynamically fetches and displays product images and extra product media from external URLs on the e-commerce website, without storing these images in the Odoo database.

## Installation

1. Copy the `odoo_module_skeleton` directory into your Odoo addons directory.
2. Update the addons list in your Odoo instance.
3. Install the module from the apps menu.

## Configuration

1. Navigate to the product template form in the Odoo backend.
2. You will find new fields for `main_image_url` and `extra_media_urls`.
3. Input the URLs for the main image and extra media in these fields.

## Usage

The images from the URLs you input will be fetched and displayed on the product pages of your e-commerce website.

## Testing

Test cases are provided in the `tests/test_product_template.py` file. Run these tests to validate the functionality, performance, and security of the module.

## Known Issues

No known issues at this time.

## Deployment

1. Transfer the `odoo_module_skeleton` directory from your development environment to your production environment.
2. Backup your Odoo instance before installing the module.
3. Monitor and maintain the module post-deployment.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes you wish to make.

## License

This module is licensed under the MIT License.