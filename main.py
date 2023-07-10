# -*- coding:utf-8 -*-
import requests,re
url = input('请输入壁纸网页：')
name = input('请输入壁纸名字：')
url_html = requests.get(url=url).text
wallpaperUrl = re.findall('src="(.*?)" x5-video-player-type',url_html)[0]
wallpaper = requests.get(url=wallpaperUrl).content
open(f'wallpaper\{name}.mp4','wb').write(wallpaper)
print(f'{name}下载好了！')
