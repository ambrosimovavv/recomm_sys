from sklearn.datasets import _samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier

# генерация данных
X, y = _samples_generator.make_classification(n_samples=150, n_features=25,
                                              n_classes=3, random_state=7,
                                              n_informative=6, n_redundant=0)

# выбор k наиболее важных признаков
k_best_selector = SelectKBest(f_regression, k=9)

# инициализируем классификатор случайного дерева
classifier = ExtraTreesClassifier(n_estimators=60, max_depth=4)

# Создание конвеера
proc_pipeline = Pipeline([('selector', k_best_selector),
                          ('erf', classifier)])

# можно установить свои параметры для селектора и классификаторы, отличные от тех, что указывались  конструкторе
proc_pipeline.set_params(selector__k=7, erf__n_estimators=30)

# обучим конвеер

proc_pipeline.fit(X, y)
output = proc_pipeline.predict(X)
print("\nпрогнозирование результатов для входных данных\n", output)

print("\Оценка Ошибки \n", proc_pipeline.score(X, y))

#proc_pipeline.name_steps['selector'].get_support