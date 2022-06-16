# Классификация эмоций в речи с помощью методов машинного обучения
## Данные
Использовалась [Берлинская база данных эмоций](http://emodb.bilderbar.info/docu/), включающая около 550 аудиофайлов. Распределение аудиофайлов по классам эмоций представлено
на диаграмме ниже.
![Распределение аудиофайлов по классам](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/distribution.png)
## Метод k ближайших соседей
Результаты обучения модели в паре с PCA представлены на рисунке ниже. Лучшее качество предсказаний - 52%.
![KNN](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/knn.png)
## Логистическая регрессия
Результаты обучения модели в паре с PCA представлены на рисунке ниже. Лучшее качество предсказаний - 58%.
![Logistic regression](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/lr.png)
## Многослойный персептрон
Результаты обучения модели представлены на рисунке ниже. Лучшее качество предсказаний - 82%.
![MLP](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/mlp.png)
## Использованное программное обеспечение
Разработка велась при помощи IDE _DataSpell 2022.1.1_ и следующих технологий:
- Python - 3.10
- Scikit-learn - 1.1.0
- Numpy - 1.22.3
- Pandas - 1.4.2
- Matplotlib - 3.5.2
- Seaborn - 0.11.2
