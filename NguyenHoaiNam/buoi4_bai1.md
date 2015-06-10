```
def do_twice(f, val):
     f(val)
     f(val)
def print_twice(printVal):
    print printVal
    print ‘tran_manh_huy'
def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)
1. text = 'spam'
2. do_four(print_twice, text)
```
Đầu tiên chương trình chạy và nó sẽ lưu các hàm do chúng ta định nghĩa
Chạy dòng code 1 lưu biến text là chuỗi spam.
Thực hiện dòng code 2 nó đến hàm do_four và gán f = print_twice và val = text
khi hàm do_four thực hiện nó gọi đến hàm do_twice lần 1 và thực thi do_twice với f = print_twice với giá trị truyền vào cho đối số printVal là biến val 
và val = 'spam'. => in ra 2 dòng là
```
spam
tran_manh_huy
```
Sau đó thực hiện gọi đến hàm do_twice lần 2 và kết quả tương tự
```
spam
tran_manh_huy
```
=> Kết thu được sau khi thực hiện chương trình trên là 
```
spam
tran_manh_huy
spam
tran_manh_huy
```
