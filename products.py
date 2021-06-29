import os #operating system
products = []
if os.path.isfile('products.csv'): #確認檔案是否存在
	print('檔案存在')
	with open('products.csv','r',encoding = 'utf-8') as f: #讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue #回去上一段繼續，通常寫在高位，一開始就略過
			name,price = line.strip().split(',')
			products.append([name, price])
		print(products)
else:
	print('找不到檔案')


#讓使用者輸入
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
#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是：',p[1])
#p[0]:all products, p[1]:all price
#寫入檔案
with open ('products.csv','w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n' )
#寫入csc檔，＋號連接字串，encoding = utf-8中文字，\n換行


