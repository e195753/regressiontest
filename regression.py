import numpy as np
class LinearRegression:
    x = None
    theta = None
    y = None

    def fit(self,input,output):
        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(input.T,input)),input.T),output)

    def predict(self,x):
        pass

    def score(self,x,y):
        pass