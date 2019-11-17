def calc(val1,val2):
   print('＝＝＝＝＝＝処理開始＝＝＝＝＝＝')
   result = 0

   try:
    result = val1 + val2
   except:
    print('処理失敗')
   finally:
    print('計算終了')
   return result

print(calc(100,200))
print(calc(100,'200'))#型変換エラーの発生
