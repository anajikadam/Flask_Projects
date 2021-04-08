import pickle
# save the model to disk
filename = 'pipeMinSc_StdSc.pkl'
filename1 = 'RFClr.pkl'
# load the model from disk
model = pickle.load(open(filename1, 'rb'))
pipe= pickle.load(open(filename, 'rb'))

# a = [6,148,72,35,53.94,33.6,0.627,50]

a = [1,89,66,23,94,28.1,0.167,21]

x_test2 = pipe.transform([a])
output = model.predict(x_test2)
print(output[0])