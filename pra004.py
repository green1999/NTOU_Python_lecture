# #留言讀取程式
# data = []
# with open('reviews.txt', 'r') as f:
# 	for line in f: #一行一行讀取
# 		data.append(line) #如果用變數x = line，只能存取一行資料
# 		#print(len(data))
# print(len(data)) #長度 #1000000筆留言
# print(data[0])

# #留言讀取程式01 一筆一筆讀取資料
# data = []
# count = 0
# with open('reviews.txt', 'r') as f:
# 	for line in f: #一行一行讀取
# 		data.append(line)
# 		count += 1 #count = count + 1
# 		if count % 1000 == 0: #如果count/1000餘數為0(每一千筆)
# 			print(len(data))
# print("檔案讀取完了，總共有",len(data),"筆資料")

# #算留言平均數
# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# 	print(sum_len)
# print('留言的平均長度',sum_len/len(data))

# #篩選範例1
# new = []
# for d in data #d是字串 data是list
# 	if len(d) < 100:
# 		new.append(d) #如果符合字串長度小於100，就裝進new的list中
# print('一共有'，len(new)
# print(new[0])

#篩選練習1
#篩選reviews.txt中有提到good的留言，並計算數量，最後顯示第一則留言
good = [d for d in data if 'good' in d] #d1要裝的東西
#output = 運算 for 變數 in 清單 if 篩選條件

#range
#python 內建功能，清單產生器
range(5) #[0,1,2,3,4] #range(結尾值)

for i in range(5): #43跟45行結果一樣
	print(i)

range(2, 5) #range(開始值，結尾值) #[2,3,4]

range(2, 10)
for i in range(2, 10):
	print(i)

range(2, 10, 3) #[2, 5, 8] 3=step #range(開始值，結尾值，遞減值)

