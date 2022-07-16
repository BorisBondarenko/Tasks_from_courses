class Goods():
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
print(Goods.price)

setattr(Goods, 'inflation', 100)
print(Goods.inflation)
print(hasattr(Goods, 'inflation'))
