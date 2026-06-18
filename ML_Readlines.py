from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
np.random.seed(42)
X = np.random.randn(500, 5)
y = np.random.randint(0,2,500)

#80/20 Train-test Split
x_train,x_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f'Training samples: {len(x_train)} |  Test samples: {len(x_test)}')

#5-Fold Cross-VAlidation - more reliable than single split
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, random_state=40) 
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f'CV SCores each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean():.4f} +- {cv_scores.std():.4f}')