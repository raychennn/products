#不知道輸入幾次用while，反之用for
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name) #分類價格和商品
	p.append(price)
	products.append(p)#二維清單
print(products)

for p in products:
	print(p[0],'的價格是：',p[1])
#p[0]:all products, p[1]:all price
with open ('products.csv','w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n' )
#寫入csc檔，＋號連接字串，encoding = utf-8中文字，\n換行