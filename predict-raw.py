import pickle

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
# customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('input', customer)
print('Churn probability of this customer is:', round(y_pred, 2))