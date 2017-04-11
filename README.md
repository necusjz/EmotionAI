# CSA
关于电影评论的中文情感分析。
## 操作流程
准备好PyCharm和JDK 1.8
### 安装Homebrew
在终端输入：
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### 安装python 3.x
```
brew install python3
```
### 安装numpy、scipy、scikit-learn库
```
sudo pip3 install numpy
```
```
sudo pip3 install scipy
```
```
sudo pip3 install scikit-learn
```
### 安装jieba、xlrd库
jieba：
```
git clone https://github.com/fxsjy/jieba.git
```
```
git checkout jieba3k
```
```
cd your-jieba-site
```
```
python3 setup.py install
```
xlrd：
[下载xlrd](https://pypi.python.org/pypi/xlrd)
```
cd your-xlrd-site
```
```
python3 setup.py install
```
### 运行程序
用PyCharm导入natural_language.py、tkTest.py并运行后者即可看见结果。
