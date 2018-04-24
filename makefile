gauss.png : gauss.txt plot_gauss.py
	python plot_gauss.py

gauss.txt : gauss
	./gauss > gauss.txt

advec_nolineal.x : ejercicio22.cpp
	c++ ejercicio22.cpp -o gauss
