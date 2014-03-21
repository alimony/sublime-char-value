#!/usr/bin/env python3
# encoding: utf-8

'''Run some basic tests on ascii, unicode, and emoji chars.'''

if __name__ == '__main__':
    import unittest
    from char_value import char_value

    class TestCharValue(unittest.TestCase):

        def test_empty_string(self):
            test_string = ''
            char_value_string = ''
            self.assertEqual(char_value_string, char_value(test_string))

        def test_one_ascii_char(self):
            test_string = 'a'
            char_value_string = '97'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_two_ascii_chars(self):
            test_string = 'ab'
            char_value_string = '97 98'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_three_ascii_chars(self):
            test_string = 'abc'
            char_value_string = '97 98 99'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_one_unicode_char(self):
            test_string = '★'
            char_value_string = '9733'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_two_unicode_chars(self):
            test_string = '★★'
            char_value_string = '9733 9733'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_three_unicode_chars(self):
            test_string = '★★★'
            char_value_string = '9733 9733 9733'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_one_emoji_char(self):
            test_string = '😄'
            char_value_string = '128516'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_two_emoji_chars(self):
            test_string = '😄😄'
            char_value_string = '128516 128516'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_three_emoji_chars(self):
            test_string = '😄😄😄'
            char_value_string = '128516 128516 128516'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_one_ascii_one_unicode_char(self):
            test_string = 'a★'
            char_value_string = '97 9733'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_two_ascii_two_unicode_chars(self):
            test_string = 'aa★★'
            char_value_string = '97 97 9733 9733'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_one_ascii_one_unicode_one_emoji_char(self):
            test_string = 'a★😄'
            char_value_string = '97 9733 128516'
            self.assertEqual(char_value_string, char_value(test_string))

        def test_two_ascii_two_unicode_two_emoji_chars(self):
            test_string = 'aa★★😄😄'
            char_value_string = '97 97 9733 9733 128516 128516'
            self.assertEqual(char_value_string, char_value(test_string))

    unittest.main(argv=['TestCharValue'])
