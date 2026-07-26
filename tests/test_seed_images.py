import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import seed


class SeedImageMappingTests(unittest.TestCase):
    def test_mapping_for_known_products(self):
        self.assertEqual(seed.get_product_image_filename('Top Bliss'), 'top_bliss.PNG')
        self.assertEqual(seed.get_product_image_filename('Chaqueta Biker Cuerina (Efecto Piel)'), 'biker.jfif')
        self.assertEqual(seed.get_product_image_filename('Vestido Sparkle Glitz'), 'Vestido_Sparkle_Glitz.jfif')

    def test_mapping_falls_back_to_default(self):
        self.assertEqual(seed.get_product_image_filename('Producto sin imagen conocida'), None)


if __name__ == '__main__':
    unittest.main()
