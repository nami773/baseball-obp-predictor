# baseball-obp-predictor
A machine learning project for predicting OBP of baseball players

Data used: https://billpetti.github.io/baseballr/

The objective of this project was to predict the 'On Base Percentage' (OBP) value of baseball players based on their game performances, such as the number of hits or strikeouts. OBP is calculated as the ratio of "times on base" to "plate appearances" throughout the season. To achieve this prediction, a Decision Tree Regression model with a maximum height of 4 was selected.

Through a thorough evaluation process using cross-validation with 10 folds, it was determined that the selected Decision Tree Regression model performed exceptionally well in predicting OBP, demonstrating a low root mean squared error of 0.0050. This common error value indicates that the model's predictions closely align with the actual OBP values, providing a high level of accuracy.

The Decision Tree:
![plottree](https://github.com/nami773/baseball-obp-predictor/assets/128548019/982e0df0-8ea7-410b-80b9-51f5e57182ca)
