import testMod

test_class1 = testMod.TestClass()
test_class1.test_method('1')

from testMod import TestClass
#クラス名の指定だけで使用できるようにするための記述

test_class2 = TestClass()
test_class2.test_method('2')
