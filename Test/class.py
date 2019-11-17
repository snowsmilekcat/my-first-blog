class TestClass:
    def __init__(self,val1,val2):#初期化時必ず通る。
       self.val1 = val1
       self.val2 = val2

classes = []
classes.append(TestClass(1,'test1'))#インスタンスをリストに格納
classes.append(TestClass(2,'test2'))#インスタンスをリストに格納

for list in classes:
    print('=======Class======')
    print('code:' + str(list.val1))
    print('code:' + list.val2)
