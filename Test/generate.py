def func_sample():
    yield('A')
    yield('B')
    yield('C')#yieldが使われるとその関数はジェネレータ関数となる。

for i in func_sample():
    print(i)
