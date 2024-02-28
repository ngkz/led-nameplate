#! /usr/bin/python3
# -*- encoding: utf-8 -*-
# (C) 2019 hrkz.tokyo
# License: http://www.gnu.org/licenses/gpl.html GPL version 2
import sys
import os.path
from PIL import Image, ImageDraw, ImageFont
#設定
fontfile = "JF-Dot-MPlusH10.ttf" #フォントファイル名

#例外処理
args = sys.argv
if len(args) != 2:
    print("エラー: 引数の数が一致しません。\n使い方：", args[0], "'任意のメッセージ'")
    sys.exit(1)

dirpath = os.path.dirname(os.path.abspath(__file__)) + "/" #実行ファイルの絶対パス
text = args[1] #メッセージを設定

im_fnt = ImageFont.truetype(dirpath + fontfile, 10) #ImageFontインスタンスを作る
w = im_fnt.getlength(text) #文字列の縦横を取得
im = Image.new("1",(int(w),11),"black") #Imageインスタンスを作る。高さは11px固定
draw = ImageDraw.Draw(im) #im上のImageDrawインスタンスを作る
draw.text((0,0),text, fill="white", font=im_fnt) #1px分、下にシフトして書き込む
im.save(dirpath + "message.png") #画像を保存
