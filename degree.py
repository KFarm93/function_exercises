import matplotlib.pyplot as plot

def temp(c):
    return c * 1.8 + 32

temp(20)
xs = range(-50, 50)
ys = range(-50, 50)


plot.plot(xs, ys)
plot.show()
