#hello worldを出力
print ("hello world")

#関数greetを定義
def greeting():
    print("こんにちは")
greeting()

#nameを引数に取り、「私の名前は{name}です」と出力するprint_name関数を実装
def print_name(name):
    print("私の名前は"+ name +"です")
print_name("さとうたろう")

#「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、戻り値をprint関数で出力
def get_greet():
    return "おはようございます"
print (get_greet())

#a, bを引数に取り、その足し算の結果を戻り値として返すadd関数を実装
def add(a,b):
    return a + b
print (add(5,7))