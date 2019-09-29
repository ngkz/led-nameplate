#!/bin/sh
if [ $# -ne 1 ]; then
  echo "エラー: 引数の数が一致しません。"
  exit 1
fi

sudo ../uhubctl/uhubctl -a on -l 1-1 -p 2
sleep 1
sudo python3 ./txt2img.py "$@"
sudo python3 ./led-nameplate-11x44-hrkz.py message.png
sleep 1
sudo ../uhubctl/uhubctl -a off -l 1-1 -p 2
