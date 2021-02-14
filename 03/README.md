# algo

Otus course Algorithms and data structures

## 3. Битовая арифметика

Написать алгоритмы генерации ходов для шахматных фигур.
Доска пустая.

1. king - прогулка Короля
2. knight - прогулка Коня
3. rook - прогулка Ладьи
4. bishop - прогулка Слона
5. queen - прогулка Ферзя
6. test - тесты

### Результаты работы алгоритмов

#### Запуск тестов

      python console_tester.py ../03/chessmen/king.py ../03/test/1_king

|   Num    |                           Shell                            |                    Time (sec)                    |  Result  |
| -------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
|    0     |python ../03/chessmen/king.py 0                             |               0.02373814582824707                |   Pass   |
|    1     |python ../03/chessmen/king.py 1                             |               0.024032115936279297               |   Pass   |
|    2     |python ../03/chessmen/king.py 7                             |               0.02438664436340332                |   Pass   |
|    3     |python ../03/chessmen/king.py 8                             |               0.024240732192993164               |   Pass   |
|    4     |python ../03/chessmen/king.py 10                            |               0.023816585540771484               |   Pass   |
|    5     |python ../03/chessmen/king.py 15                            |               0.023948192596435547               |   Pass   |
|    6     |python ../03/chessmen/king.py 54                            |               0.025751352310180664               |   Pass   |
|    7     |python ../03/chessmen/king.py 55                            |               0.028588294982910156               |   Pass   |
|    8     |python ../03/chessmen/king.py 56                            |               0.02500772476196289                |   Pass   |
|    9     |python ../03/chessmen/king.py 63                            |               0.024182796478271484               |   Pass   |

---
---
      python console_tester.py ../03/chessmen/knight.py ../03/test/2_knight

|   Num    |                           Shell                            |                    Time (sec)                    |  Result  |
| -------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
|    0     |python ../03/chessmen/knight.py 0                           |               0.023945331573486328               |   Pass   |
|    1     |python ../03/chessmen/knight.py 1                           |               0.035925865173339844               |   Pass   |
|    2     |python ../03/chessmen/knight.py 2                           |               0.02557516098022461                |   Pass   |
|    3     |python ../03/chessmen/knight.py 36                          |               0.023862361907958984               |   Pass   |
|    4     |python ../03/chessmen/knight.py 47                          |               0.024071216583251953               |   Pass   |
|    5     |python ../03/chessmen/knight.py 48                          |               0.03051590919494629                |   Pass   |
|    6     |python ../03/chessmen/knight.py 54                          |               0.027673959732055664               |   Pass   |
|    7     |python ../03/chessmen/knight.py 55                          |               0.02358102798461914                |   Pass   |
|    8     |python ../03/chessmen/knight.py 56                          |               0.024262428283691406               |   Pass   |
|    9     |python ../03/chessmen/knight.py 63                          |               0.02481865882873535                |   Pass   |

---
---
      python console_tester.py ../03/chessmen/rook.py ../03/test/3_rook
|   Num    |                           Shell                            |                    Time (sec)                    |  Result  |
| -------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
|    0     |python ../03/chessmen/rook.py 0                             |               0.026357650756835938               |   Pass   |
|    1     |python ../03/chessmen/rook.py 1                             |               0.024744272232055664               |   Pass   |
|    2     |python ../03/chessmen/rook.py 2                             |               0.02517247200012207                |   Pass   |
|    3     |python ../03/chessmen/rook.py 36                            |               0.024601221084594727               |   Pass   |
|    4     |python ../03/chessmen/rook.py 47                            |               0.023683786392211914               |   Pass   |
|    5     |python ../03/chessmen/rook.py 48                            |               0.023767948150634766               |   Pass   |
|    6     |python ../03/chessmen/rook.py 54                            |                0.0243682861328125                |   Pass   |
|    7     |python ../03/chessmen/rook.py 55                            |               0.023660898208618164               |   Pass   |
|    8     |python ../03/chessmen/rook.py 56                            |               0.023694992065429688               |   Pass   |
|    9     |python ../03/chessmen/rook.py 63                            |               0.02471160888671875                |   Pass   |

---
---
      python console_tester.py ../03/chessmen/bishop.py ../03/test/4_bishop

|   Num    |                           Shell                            |                    Time (sec)                    |  Result  |
| -------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
|    0     |python ../03/chessmen/bishop.py 0                           |               0.024034976959228516               |   Pass   |
|    1     |python ../03/chessmen/bishop.py 1                           |               0.023999452590942383               |   Pass   |
|    2     |python ../03/chessmen/bishop.py 2                           |               0.02483963966369629                |   Pass   |
|    3     |python ../03/chessmen/bishop.py 36                          |               0.024014711380004883               |   Pass   |
|    4     |python ../03/chessmen/bishop.py 47                          |               0.023730039596557617               |   Pass   |
|    5     |python ../03/chessmen/bishop.py 48                          |                0.0244138240814209                |   Pass   |
|    6     |python ../03/chessmen/bishop.py 54                          |               0.02387714385986328                |   Pass   |
|    7     |python ../03/chessmen/bishop.py 55                          |               0.023572921752929688               |   Pass   |
|    8     |python ../03/chessmen/bishop.py 56                          |               0.02483057975769043                |   Pass   |
|    9     |python ../03/chessmen/bishop.py 63                          |               0.024715185165405273               |   Pass   |

---
---

      python console_tester.py ../03/chessmen/queen.py ../03/test/5_queen

|   Num    |                           Shell                            |                    Time (sec)                    |  Result  |
| -------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
|    0     |python ../03/chessmen/queen.py 0                            |               0.027300357818603516               |   Pass   |
|    1     |python ../03/chessmen/queen.py 1                            |               0.025121450424194336               |   Pass   |
|    2     |python ../03/chessmen/queen.py 2                            |               0.02407217025756836                |   Pass   |
|    3     |python ../03/chessmen/queen.py 36                           |               0.024249553680419922               |   Pass   |
|    4     |python ../03/chessmen/queen.py 47                           |               0.024439096450805664               |   Pass   |
|    5     |python ../03/chessmen/queen.py 48                           |               0.024002552032470703               |   Pass   |
|    6     |python ../03/chessmen/queen.py 54                           |               0.025226116180419922               |   Pass   |
|    7     |python ../03/chessmen/queen.py 55                           |               0.023897409439086914               |   Pass   |
|    8     |python ../03/chessmen/queen.py 56                           |               0.024457216262817383               |   Pass   |
|    9     |python ../03/chessmen/queen.py 63                           |               0.024648427963256836               |   Pass   |
