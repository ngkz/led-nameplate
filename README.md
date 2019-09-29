# led-nameplate

## 説明
LEDネームプレートをPythonで制御するスクリプトです。

## 必要要件
Raspberry Pi 3B+で動作検証していますが、以下を満たす環境なら各種マイコンやPCでも動作します。

- LEDネームプレート: メーカーやモデルによって通信方式が異なります。[春風商事のLEDネームプレート](https://hrkz.tokyo/led-nameplate-s1144/)を推奨します。
- Python3
- USBホスト機能
- USBハブの電源制御機能(Ganged power switchingもしくはPer-port power switching)

USBハブの電源制御機能がなくてもLEDネームプレートのメッセージを設定できます。
ただしUSBがつながっている状態だと充電中の表示となり、メッセージは表示されません。
USBケーブルを抜くか、LEDネームプレート本体のメッセージ切り替えボタンを押すと、メッセージが表示されます。

## 使い方
ラズパイとLEDネームプレートをUSB接続した状態で、下記コマンドで任意のメッセージを表示できます。
```
cd ./led-nameplate/
sh led-ctrl.sh '冷やし中華、はじめました'
```

## インストール
USB電源をオン/オフ制御するため`libusb`と`uhubctl`をインストールします。
```
sudo apt install libusb-1.0-0-dev
git clone https://github.com/mvp/uhubctl
cd ./uhubctl/
make
cd ../
```

PythonからUSB機器を制御するライブラリ`python3-usb`とPythonの画像処理ライブラリ`python3-pil`をインストールします。
```
sudo apt install python3-usb python3-pil
```

LEDネームプレートを制御するスクリプトを`led-nameplate`にまとめています。
```
git clone https://github.com/harukaze-co/led-nameplate
```

##  解説
### 制御フロー
`led-ctrl.sh`にて以下の流れで制御しています。
1. 任意のメッセージを高さ11pxのPNG画像に変換
2. PNG画像からビットマップデータに変換
3. ビットマップデータと各種オプションをLEDネームプレートに書き込む
4. USBの電源をオフにする

### led-name-badge-ls32
LEDネームプレートに設定を書き込むPythonスクリプトは[jnweiger/led-name-badge-ls32](https://github.com/jnweiger/led-name-badge-ls32)を利用しています。

オプションで表示エフェクトを設定できます。
```
sudo python3 ./led-nameplate-11x44-hrkz.py abd -s 8 -m 8 -b 1 -a 1
```

オプションの設定方法は以下の通りです。
```
led-nameplate-11x44-hrkz.py [-s SPEED] [-m MODE] [-b BLINK] [-a ANTS] MESSAGE
```

- -s SPEED, --speed SPEED
	- 	スクロール速度を設定します（1〜8)
- -m MODE, --mode MODE
	- 表示エフェクトを設定します
	- 0: 右から左
	- 1: 左から右
	- 2: 下から上
	- 3: 上から下
	- 4: 固定
	- 5: アニメーション
	- 6: 降雪（上から下にドットを積む）
	- 7: カーテン（中央から表示）
	- 8: レーザー
- -b BLINK, --blink BLINK
	- 1:点滅、0:通常
- -a ANTS, --ants ANTS
	- 1:枠を表示、0:非表示

LEDネームプレートの制御プロトコルの詳細は[LEDネームプレート 製品紹介](https://hrkz.tokyo/led-nameplate-s1144/)で解説しています。

### フォント
デフォルトでは[自家製フォント工房](http://jikasei.me/font/jf-dotfont/)で配布されている「JFドットM+H10」フォントを利用しています。
`txt2img.py`の下記箇所を変更すれば任意のTrueTypeフォントを使えます。
```
fontfile = "JF-Dot-MPlusH10.ttf" #フォントファイル名
```

### uhubctl
`hub-ctrl`をベースに、より直感的な設定方法に改善されています。お好きなほうをご利用ください。
[mvp/uhubctl: uhubctl](https://github.com/mvp/uhubctl)

`hub-ctrl`を使う方法は[BeagleBoneBlackBox_USB電源制御 - Tech Info](https://www.si-linux.co.jp/techinfo/index.php?BeagleBoneBlackBox_USB%E9%9B%BB%E6%BA%90%E5%88%B6%E5%BE%A1)が参考になります。
