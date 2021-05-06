
import datasets
import regression
import  importlib
importlib.reload(regression)
x,y = datasets.load_linear_example1()
model = regression.LinearRegression()
model.fit(x,y)
print(model.theta)