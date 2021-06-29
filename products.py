#不知道輸入幾次用while，反之用for
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

