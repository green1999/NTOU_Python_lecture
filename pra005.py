# 販賣機
# 做一個販賣機，只可以投15，50，100元，或是按q離開
# 販賣機的東西有，柳橙汁10元，礦泉水15元，牛奶30元
# 利用function進行，是否可以購買的運算，並顯示餘額

def cal(price, p2):
	return price - p2

price = input('請投入現金，只接受15,50,100元，按q可退出投幣:')
if price == '15' or price == '50' or price == '100':
	# price = int(price)
	print(f'投入數字:{price}')

	print('飲料售價:柳橙汁10元，礦泉水15元，牛奶30元')
	drink_number = input('請輸入數字選擇想購買的飲料(柳橙汁:1，礦泉水:2，牛奶:3，退出:q):')
	print(f'輸入數字:{drink_number}')
	item = ['柳橙汁', '礦泉水', '牛奶']
	p2 = [10, 15, 30]

	if drink_number == '1':
		price = int(price)
		p2 = int(10)
		if cal(price, p2) < 0:
			print (f'餘額不足哦!\n還需要{abs(cal(price, p2))}元\n謝謝光臨!')
		else:
			print(f'購買了{item[0]}，花費{p2}元，餘額{cal(price,p2)}元\n謝謝光臨!')
	elif drink_number == '2':
		price = int(price)
		p2 = int(15)
		if cal(price, p2) < 0:
			print (f'餘額不足哦!\n還需要{abs(cal(price, p2))}元\n謝謝光臨!')
		else:
			print(f'購買了{item[1]}，花費{p2}元，餘額{cal(price, p2)}元\n謝謝光臨!')
	elif drink_number == '3':
		price = int(price)
		p2 = int(30)
		if cal(price, p2) < 0:
			print (f'餘額不足哦!\n還需要{abs(cal(price, p2))}元\n謝謝光臨!')
		else:
			print(f'購買了{item[2]}，花費{p2}元, 餘額{cal(price, p2)}元\n謝謝光臨!')

elif price == 'q':
	print('退出投幣')
	# exit()
else:
	print('只接受15,50,100元，按q可退出投幣')