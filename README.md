# led-nameplate

## 説明
LEDネームプレートをPythonで制御するスクリプトです。

![demo-led-np-ctrl](https://user-images.githubusercontent.com/55935162/65830035-cb23fe80-e2e6-11e9-991b-f52a023ce54f.gif)

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
より詳しい情報は[LEDネームプレートをラズパイから制御する方法](https://hrkz.tokyo/led-nameplate-ctrl-rpi/)をご覧ください。
