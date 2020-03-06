class Datamining:

    def __init__(self, train_set):
        self.__train(train_set)

    def __train(self, train_set):
        # unpack training set
        x = [tup[0] for tup in train_set]
        y = [tup[1] for tup in train_set]
        self.gradient, self.intercept = self.__find_gradient_and_intercept(x, y)

    def __find_gradient_and_intercept(self, x, y):
        x_mean = sum(x)/len(x)
        y_mean = sum(y)/len(y)

        # Ordinary Least Squares (OLS) Method
        # equation taken from: https://towardsdatascience.com/linear-regression-simplified-ordinary-least-square-vs-gradient-descent-48145de2cf76
        x_minus_x_mean = [a - x_mean for a in x]
        y_minus_y_mean = [a - y_mean for a in y]

        numerator = sum([a*b for a,b in zip(x_minus_x_mean, y_minus_y_mean)])
        denominator = sum([a**2 for a in x_minus_x_mean])

        m = numerator / denominator
        b = y_mean - m*x_mean
        return m, b

    def predict(self, x):
        return self.gradient*x + self.intercept
