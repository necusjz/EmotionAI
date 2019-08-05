# How to use
Prepare PyCharm and JDK 1.8
## Install Homebrew
Enter in the terminal:
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
## Install Python 3.x
```bash
$ brew install python3
```
## Install Numpy, SciPy and scikit-learn
```bash
$ sudo pip3 install numpy
```
```bash
$ sudo pip3 install scipy
```
```bash
$ sudo pip3 install scikit-learn
```
## Install jieba and xlrd
jieba：
```bash
$ git clone https://github.com/fxsjy/jieba.git
```
```bash
$ git checkout jieba3k
```
```bash
$ cd your-jieba-site
```
```bash
$ python3 setup.py install
```
xlrd：

[Download xlrd](https://pypi.python.org/pypi/xlrd)
```bash
$ cd your-xlrd-site
```
```bash
$ python3 setup.py install
```
## Run the program
Use Pycharm to run _natural_language.py_ and _tkTest.py_, you can see the results.
