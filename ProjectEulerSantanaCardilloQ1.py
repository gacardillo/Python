result = 0
for i in range(0,1000):
 if (i % 3 == 0 or i % 5 == 0):
  print i
  result = result + i
  print result

import unittest


class Mytest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual((i % 3), 0)
        self.assertEqual((i % 5), 4)

if __name__ == '__main__':
    unittest.main()

###Contributors used Overflow Stack to conduct research for code provided above###
