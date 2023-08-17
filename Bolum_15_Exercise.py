def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        #a = b        # bu ifadede a değişkeninin değeri güncellendiğinden dolayı fibonacciye uymaz
        #b = a+b
        a,b = b,a+b  
        yield b 
        if(b >100):
                break

iterator = iter(fibonacci())
print(iterator) #fonksiyon objesinin yerini bastırıyor
for number in iterator:
    print(next(iterator))