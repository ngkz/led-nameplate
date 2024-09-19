upload: data-matrix.png data-insignia.png
	python led-nameplate-11x44-hrkz.py -m 5,5,4 -s 7,7,7 -B 50 data-matrix.png data-insignia.png data-head.png

data-matrix.png:
	python matrix.py

data-insignia.png:
	python insignia.py

clean:
	$(RM) data-matrix.png matrix.gif data-insignia.png insignia-rotating-converted.gif
