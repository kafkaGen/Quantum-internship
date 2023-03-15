import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


if __name__ == '__main__':
    ### Load data
    df = pd.read_csv('Quantum internship/Regression_problem_on_tabular_data/internship_train.csv')
    test = pd.read_csv('Quantum internship/Regression_problem_on_tabular_data/internship_hidden_test.csv')
    X = df.drop('target', axis=1)
    y = df['target'].copy()

    ### Poly features
    poly = PolynomialFeatures(degree=2, include_bias=True)
    X_new = poly.fit_transform(X[['6', '7']])
    test_new = poly.transform(test[['6', '7']])
    
    ### Fitting model
    model = LinearRegression()
    model.fit(X_new, y)

    ### Prediction
    pred = model.predict(test_new)
    answ = pd.DataFrame(pred, columns=['target'])
    answ.to_csv('Quantum internship/Regression_problem_on_tabular_data/prediction.csv', index=False)