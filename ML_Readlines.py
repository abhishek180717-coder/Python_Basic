from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
np.random.seed(42)
X = np.random.randn(500, 5)
y = np.random.randint(0,2,500)

#80/20 Train-test Split:-
x_train,x_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f'Training samples: {len(x_train)} |  Test samples: {len(x_test)}')

#5-Fold Cross-Validation - more reliable than single split:-
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, random_state=40) 
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV SCores each fold: {cv_scores.round(3)}")
print(f'Mean: {cv_scores.mean():.4f} +- {cv_scores.std():.4f}')






#A B Testing Analysis:-
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt

#Data:-
n_A, conv_A = 1000, 52
n_B, conv_B = 1000, 68
rate_A = conv_A / n_A
rate_B = conv_B / n_B

print(f'Version A conersion rate: {rate_A*100:.1f}%')
print(f'Version B conersion rate: {rate_B*100:.1f}%')
print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')


#chi-Square test for Statistical Significance:-
table = [[conv_A, n_A-conv_A], [conv_B, n_B-conv_B]]
chi2, p_value, dof, expected = stats.chi2_contingency(table)

print(f'Chi-square: {chi2:.4f}')
print(f'P_value: {p_value:.4f}')
print('Resul:', 'SIGNIFICANT - B is better!' if p_value<0.05 else 'NOT significant - could be random') 








#Linear Regression in ML:-

#Study hours vs Exam Marks:-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

study = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2.5, 4.5, 6.5, 8.5]
marks = [25, 38, 52, 65, 71, 78, 85, 89, 93, 96, 43, 68, 82, 91]

X = np.array(study).reshape(-1,1)
y = np.array(marks)

X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f'Slope:      {model.coef_[0]:.2f}    (marks increase per study hour)')
print(f'INtercept:  {model.intercept_:.2f}  (marks at 0 study hours)')

y_pred = model.predict(X_test)
print(f'R^2 Score:  {r2_score(y_test,y_pred):.4f}  (1.0 = perfect)')
print(f'RMSE:       {mean_squared_error(y_test,y_pred)**0.5:.2f} marks average error')

#Predict new Student:-
new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks:  {new_pred:.1f}')

#Plot:-
plt.figure(figsize=(9,5))
plt.scatter(X,y,color='steelblue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
plt.xlabel('Study Hours/Day'); plt.ylabel('Exam Marks')
plt.title('Linear Regression -- Study Hours vs Marks')
plt.legend(); plt.grid(True,alpha=0.3); plt.show()