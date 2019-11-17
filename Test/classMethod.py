import datetime
class TestClass:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod #クラスメソッドの定義
    def testClassMethod(cls,date_diff=0):#引数なしの場合、diff=0
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return cls(d.year,d.month,d.day)

#クラスメソッドはインスタンス化なしに呼び出せる。
testClass1 = TestClass.testClassMethod()
print(testClass1.year,testClass1.month,testClass1.day)

#クラスメソッドはインスタンス化なしに呼び出せる。
testClass2 = TestClass.testClassMethod(-5)
print(testClass2.year,testClass2.month,testClass2.day)

#通常のインスタンス
testClass3 = TestClass(2019,11,20)
print(testClass3.year,testClass3.month,testClass3.day)
