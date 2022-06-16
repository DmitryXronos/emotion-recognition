# Классификатор эмоций в речи
## Данные
Использовалась [Берлинская база данных эмоций](http://emodb.bilderbar.info/docu/), включающая около 550 аудиофайлов. Распределение аудиофайлов по классам эмоций представлено
на диаграмме ниже.
![Распределение аудиофайлов по классам](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/distribution.png)
## Метод k ближайших соседей
Результаты обучения модели в паре с PCA представлены на рисунке ниже. Лучшее качество предсказаний - 52%.
![KNN](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/knn.png)
## Логистическая регрессия
Результаты обучения модели в паре с PCA представлены на рисунке ниже. Лучшее качество предсказаний - 57%.
![KNN](https://github.com/DmitryXronos/emotion-recognition/blob/develop/Images/lr.png)
## Многослойный персептрон
## Использованное программное обеспечение
- Python
- Scikit-learn
- Numpy
- Pandas
- Matplotlib
- Seaborn
