from auto_player import Player
from auto_ocr_player import OCR_Player
import time
import random

#OCR文字识别  桌面模式（不能遮挡游戏窗口）
# myplayer = OCR_Player(accuracy=0.6, adb_mode=False)
# while True:
# 	myplayer.find_touch(['s挑战', '点击屏幕继续'])
# 	r = random.randint(10, 15)/10
# 	time.sleep(r)

#ADB模式（确保设备ADB连接成功）
# myplayer = OCR_Player(accuracy=0.6, adb_mode=True)
# while True:
# 	myplayer.find_touch(['s挑战', '点击屏幕继续'])
# 	r = random.randint(10, 15) / 10
# 	time.sleep(r)

#ADB模型 CV图像 960*540
# 960*
single = True
sum = 0
if single:
	myplayer = Player(accuracy=0.8, adb_num=0, adb_mode=True)
	while True:
		myplayer.find_touch(['960_yys_tiaozhan', '960_yys_jixu']) # 魂土
		# myplayer.find_touch(['960_huodong_tiaozhan', '960_yys_jixu']) # 活动
		# if sum > 5:
		if sum > 60*(10+random.randint(1, 5)):
			myplayer.moni()
			sum = 0
		r = random.randint(10, 15) / 10
		sum += r
		time.sleep(r)
else:
	myplayer0 = Player(accuracy=0.8, adb_num=0, adb_mode=True)  # 大号
	myplayer1 = Player(accuracy=0.8, adb_num=1, adb_mode=True)  # 小号
	while True:
		myplayer1.find_touch(['960_hun11_tiaozhan', '960_yys_jixu'])  # 魂土
		myplayer0.find_touch(['960_hun11_tiaozhan', '960_yys_jixu'])  # 魂土
		#myplayer1.find_touch(['960_huodong_tiaozhan', '960_yys_jixu'])  # 活动
		#myplayer0.find_touch(['960_huodong_tiaozhan', '960_yys_jixu'])  # 活动
		if sum > 60*(10+random.randint(1, 5)):
			# if sum > 60*(20+random.randint(1, 5)):
			myplayer1.moni()
			myplayer0.moni()
			sum = 0
		r = random.randint(10, 15) / 10
		sum += r
		time.sleep(r)


#CV图像匹配 MuMu限定 640*360分辨率
# myplayer = Player(accuracy=0.8, adb_mode=False)
# while True:
# 	# myplayer.find_touch(['hun11_tiaozhan', 'yys_jixu']) # 魂土
# 	# myplayer.find_touch(['yys_tiaozhan', 'yys_jixu']) # 御灵
# 	myplayer.find_touch(['huodong_tiaozhan', 'yys_jixu']) # 御灵
# 	r = random.randint(10, 15) / 10
# 	time.sleep(r)
