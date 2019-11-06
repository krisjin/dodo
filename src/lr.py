import numpy
from pandas import read_csv
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = read_csv(
    'file:///Users/shijingui/Desktop/Data.csv',encoding='GBK'
)

#画出散点图，求x和y的相关系数
plt.scatter(data.活动推广费,data.销售额)

data.corr()

#估计模型参数，建立回归模型
'''
(1) 首先导入简单线性回归的求解类LinearRegression
(2) 然后使用该类进行建模，得到lrModel的模型变量
'''

lrModel = LinearRegression()
#(3) 接着，我们把自变量和因变量选择出来
x = data[['活动推广费']]
y = data[['销售额']]

#模型训练
'''
调用模型的fit方法，对模型进行训练
这个训练过程就是参数求解的过程
并对模型进行拟合
'''
lrModel.fit(x,y)

#对回归模型进行检验
score=lrModel.score(x,y)

#利用回归模型进行预测
v =lrModel.predict([[60],[70]])

#查看截距
alpha = lrModel.intercept_[0]

#查看参数
beta = lrModel.coef_[0][0]

alpha + beta*numpy.array([60,70])