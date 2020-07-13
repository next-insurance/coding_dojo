# pull: git pull
# push: git commit -am 'done'
#       git push

import unittest


class OCR:

    def foo(self):
        return 4


class Test(unittest.TestCase):


    def test_sanity(self):
        uut = OCR()
        self.assertEqual(uut.foo(), 4)


if __name__ == '__main__':
    unittest.main()