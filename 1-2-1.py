# coding: UTF-8

print('Hello, world!')
print(10 ** 3)

msg = 'test'
print(msg)
print(msg[1])

num = 1 

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data_list1 = []
data_list1 = [i * 2 for i in data_list]
print(data_list1)

data_list2 = [i * 2 for i in data_list if i % 2 ==0]
print(data_list2)

for one, two in zip([1, 2, 3] ,[11, 12, 13]):
  print(one, "と", two)

while num <= 10:
  print(num)
  num = num + 1

print('最後の値は{0}です'.format(num))

def calc_multi(a, b):
  return a * b

print(calc_multi(3, 10))

# 再帰関数の例（フィボナッチ数）
def calc_fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return calc_fib(n - 1) + calc_fib(n - 2)

print('フィボナッチ数:', calc_fib(10))

print((lambda a, b: a * b)(10, 4))

def calc_double(x) :
  return x * 2

print(list(map(calc_double, [1, 2, 3, 4])))
print(list(map(lambda x : x * 2, [1, 2, 3, 4])))

# PrintClassの作成とprint_meメソッドの作成
class PrintClass:
  def print_me(self):
    print(self.x, self.y)

#インスタンスの作成、生成
p1 = PrintClass()

#属性の値を代入
p1.x = 10
p1.y = 100
p1.z = 1000

#メソッドの呼び出し
p1.print_me()
print(p1.z)

class MyCalcClass:
  #コンストラクタ:オブジェクト生成時に呼び出される特殊な関数、初期化など
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def calc_add1(self, a, b):
    return a + b
  
  def calc_add2(self):
    return self.x + self.y

  def calc_multi(self, a, b):
    return a * b

  def calc_print(self, a):
    print('data:{0}:yの値{1}'.format(a, self.y))

instance_1 = MyCalcClass(1, 2)
instance_2 = MyCalcClass(5, 10)

print('2つの数の足し算(新たに数字を引数としてセット):', instance_1.calc_add1(5, 3))
print('2つの数の足し算(インスタンス化のときの値):', instance_1.calc_add2())
instance_1.calc_print(5)

print('2つの数の足し算(新たに数字を引数としてセット):', instance_2.calc_add1(10, 3)) #13
print('2つの数の足し算(インスタンス化のときの値):', instance_2.calc_add2()) #15
print('2つの数の掛け算:', instance_2.calc_multi(4, 3)) #12
instance_2.calc_print(20) #data:20 y 10

##　総合問題
# 1-1 素数判定　
# 1.10までの素数を表示するプログラムを書く。

def calc_prime_num(x):
  n_list = range(2, x + 1)

  for i in range(2 , int(x ** 0.5) + 1):
    n_list = [x for x in n_list if (x == i or x % i != 0)]

  for j in n_list:
    print(j)

print(range(2, int(10 ** 0.5) + 1))
calc_prime_num(10)