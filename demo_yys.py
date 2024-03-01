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
single = False
sum = 0  #多少秒模拟
stop_times = 500 #次数
if single:
	myplayer = Player(accuracy=0.8, adb_num=0, adb_mode=True, stop_times=stop_times)
	while True:
		# myplayer.find_touch(['960_huodong_tiaozhan', 'yys_jixu']) # 魂土
		# myplayer.find_touch(['960_yys_tiaozhan', 'yys_jixu'])
		myplayer.find_touch(['yys_tiaozhan', 'yys_jixu']) # 活动
		# if sum > 2:
		if sum > 60*(10+random.randint(1, 5)):
			re = myplayer.moni()
			sum = 0
			if re == 'shibai':
				sum = 60 * 5
		r = random.randint(10, 15) / 10
		sum += r
		time.sleep(r)
else:
	myplayer1 = Player(accuracy=0.8, adb_num=1, adb_mode=True, stop_times=stop_times)  # 小号房主在前（魂王）
	myplayer0 = Player(accuracy=0.8, adb_num=0, adb_mode=True, stop_times=stop_times)  # 大号房主在前（魂土）
	confirm = False
	while True:
		confirm = myplayer1.find_touch(['duoren_tiaozhan', 'yys_jixu'], confirm=confirm)  # 魂土
		confirm = myplayer0.find_touch(['duoren_tiaozhan', 'yys_jixu'], confirm=confirm)  # 魂土
		# myplayer1.find_touch(['960_yys_tiaozhan', 'yys_jixu'])  # 活动
		# myplayer0.find_touch(['960_yys_tiaozhan', 'yys_jixu'])  # 活动
		if sum > 60*(10+random.randint(1, 5)):
		# if sum > 10*(1):
			re1 = myplayer1.moni()
			re2 = myplayer0.moni()
			sum = 0
			if re1 == 'shibai' or re2 == 'shibai':
				sum = 60 * 5
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
