import numpy as np

marks=np.array([10,1,20,30,4,5,31])

print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.argmax(marks))
print(np.argmin(marks))
print(np.sqrt(marks))


bourdain=np.array([[1,2,0],[6,7,7], [0,5,5]])
print(np.sum(bourdain))
print(np.sum(bourdain, axis=0))
print(np.sum(bourdain, axis=1))