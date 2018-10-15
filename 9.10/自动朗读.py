#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:L
# Date:2018/9/19 13:41
import uuid
import re
import os
import argparse
from pydub import AudioSegment
from aip import AipSpeech
from playsound import playsound
from goose3 import Goose
from goose3.text import StopWordsChinese

""" 你的 百度 APPID AK SK """
APP_ID = '14234285'
API_KEY = '8Vjov2dljwViGIu5dPPRtGvW'
SECRET_KEY = 'vpa7YAcMZHWPIdyW35Sy671UCHvcfBGL'

# 命令行输入参数处理
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--url', type=str, help="input the target url")

# 获取参数
# args = parser.parse_args()
# URL = args.url

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def text_to_voice(text):
    file_name = str(uuid.uuid1()) + '.mp3'
    result = client.synthesis(text, 'zh', 3, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回 dict 参照下面错误码
    if not isinstance(result, dict):
        with open(file_name, 'wb+') as f:
            f.write(result)
    return file_name


def get_text():
    g = Goose()
    url = "https://item.btime.com/36a0f17i0489keqltn35q96p4lr?from=haozcxw"
    article = g.extract(url=url)
    print(article.title)
    print(article.cleaned_text)
    return article.cleaned_text


# 合并音频文件
def merge_voice(file_list):
    voice_dict = {}
    song = None
    for i, f in enumerate(file_list):
        if i == 0:
            song = AudioSegment.from_file(f, "mp3")
        else:
            # 拼接音频文件
            song += AudioSegment.from_file(f, "mp3")
        # 删除临时音频
        os.unlink(f)

    # 导出合并后的音频文件，格式为MP3格式
    file_name = str(uuid.uuid1()) + ".mp3"
    song.export(file_name, format="mp3")
    return file_name


if __name__ == "__main__":
    # text = get_text()
    # test = "Those days when we were together appear in my mind time after time,because they were so joyful, happy, blest, disappointing, sad and painful. I miss you ,and miss you so mach.Within you I lose myself, without you I find myself wanting to be lost again."

    # 将文本按 500 的长度分割成多个文本
    # text_list = [text[i:i + 500] for i in range(0, len(text), 500)]
    # text_list = "我买几个橘子去你就在此地不要走动"
    text_list =["我买几个橘子去", "你就在此地不要走动"]

    file_list = []
    for t in text_list:
        file_list.append(text_to_voice(t))
    print(file_list)
    final_voice = merge_voice(file_list)
    print(final_voice)
    # 播放音频
    playsound(final_voice)