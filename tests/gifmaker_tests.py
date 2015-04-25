import unittest

import gifmaker

class GifmakerTests(unittest.TestCase):
    def test_raw_time_to_min(self):
        raw = '01:00'
        self.assertEqual(1, gifmaker.raw_time_to_min(raw))



if __name__ == '__main__':
    unittest.main()
