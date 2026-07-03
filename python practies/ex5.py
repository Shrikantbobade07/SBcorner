def even_number(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield i
gen = even_number(10)
for num in gen:
    print(num)