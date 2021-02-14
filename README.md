# algo

Otus course Algorithms and data structures

## ДЗ 3. Битовая арифметика

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

## ДЗ 2. Алгебраические алгоритмы

1. power - задача возведения в степень:
   1. Итеративный (n умножений)
   2. Возведение в степень через степень двойки с домножением
   3. Возведение в степень через двоичное разложение показателя степени
2. fibonacci - задача поиска чисел Фибоначчи:
   1. Через рекурсию
   2. Через итерацию
   3. По формуле золотого сечения
   4. Через умножение матриц
3. primenumbers - задача поиска кол-ва простых чисел до N:
   1. Перебор делителей, с использованием массива
   2. Решето Эратосфена со сложностью O(n log log n)
   3. Решето Эратосфена со сложностью O(n)
4. test - тесты

### Результаты работы алгоритмов

#### Запуск тестов

      python console_tester.py ../02/power/power.py ../02/test/3_power
      python console_tester.py ../02/fibonacci/fibonacci.py ../02/test/4_fibo/
      python console_tester.py ../02/primenumbers/primenum.py ../02/test/5_primes
---
---

#### Возведение в степень

|   Num    |                           Shell                   |     Итеративный       |     Степень двойки    | Двоичное разложение   |
| -------- | -----------------------------------------------   |---------------------- |---------------------- |---------------------- |
|    0     | python ../02/power/power.py 2 10                  | 0.023826122283935547  | 0.024005413055419922  |  0.0243380069732666   |
|    1     | python ../02/power/power.py 123456789 0           | 0.024706602096557617  | 0.023856401443481445  | 0.02385115623474121   |
|    2     | python ../02/power/power.py 1.001 1000            | 0.024847030639648438  | 0.023171186447143555  | 0.02498340606689453   |
|    3     | python ../02/power/power.py 1.0001 10000          | 0.02620077133178711   | 0.024151325225830078  | 0.02334427833557129   |
|    4     | python ../02/power/power.py 1.00001 100000        | 0.04545760154724121   | 0.03107309341430664   | 0.023335933685302734  |
|    5     | python ../02/power/power.py 1.000001 1000000      | 0.23850750923156738   | 0.12777042388916016   | 0.023429155349731445  |
|    6     | python ../02/power/power.py 1.0000001 10000000    | 2.1909568309783936    |  0.3821840286254883   | 0.02324199676513672   |
|    7     | python ../02/power/power.py 1.00000001 100000000  | 23.255650997161865    |  7.1498682498931885   | 0.024010658264160156  |
|    8     | python ../02/power/power.py 1.000000001 1000000000| xxxxxxxxxxxxxxxxxx    | xxxxxxxxxxxxxxxxxxx   | 0.023508310317993164  |

---
---

#### Числа Фибоначчи

|   Num    |                           Shell                   |     Итеративный       |   Золотое сечения     |   Умножение матриц    |
| -------- | -----------------------------------------------   |---------------------- |---------------------- |---------------------- |
|    0     |python ../02/fibonacci/fibonacci.py 0              | 0.04300856590270996   | 0.024712800979614258  | 0.026434659957885742  |
|    1     |python ../02/fibonacci/fibonacci.py 1              | 0.024378538131713867  | 0.024186372756958008  | 0.02524399757385254   |
|    2     |python ../02/fibonacci/fibonacci.py 2              | 0.02409839630126953   | 0.023664474487304688  | 0.02493453025817871   |
|    3     |python ../02/fibonacci/fibonacci.py 3              | 0.02448272705078125   | 0.023470163345336914  | 0.023805856704711914  |
|    4     |python ../02/fibonacci/fibonacci.py 4              | 0.02409839630126953   | 0.024456501007080078  | 0.02318572998046875   |
|    5     |python ../02/fibonacci/fibonacci.py 5              | 0.02448272705078125   | 0.023222684860229492  | 0.024948835372924805  |
|    6     |python ../02/fibonacci/fibonacci.py 10             | 0.024273157119750977  | 0.023289203643798828  | 0.02527332305908203   |
|    7     |python ../02/fibonacci/fibonacci.py 100            | 0.023380041122436523  | 0.024473905563354492  | 0.024983644485473633  |
|    8     |python ../02/fibonacci/fibonacci.py 1000           | 0.024165868759155273  | 0.024882078170776367  | 0.0233309268951416    |
|    9     |python ../02/fibonacci/fibonacci.py 10000          | 0.023785114288330078  | 0.07281136512756348   | 0.024018526077270508  |
|    10    |python ../02/fibonacci/fibonacci.py 100000         | 0.10939550399780273   | 0.8029928207397461    | 0.03952980041503906   |
|    11    |python ../02/fibonacci/fibonacci.py 1000000        | 8.23327088356018      | 11.448654413223267    | 0.8634970188140869    |

---
---

#### Поиск простых чисел

|   Num    |                           Shell                   |  Перебор делителей    | Эратосфен O(nloglogn) |    Эратосфен O(n)     |
| -------- | -----------------------------------------------   |---------------------- |---------------------- |---------------------- |
|    0     |python ../02/primenumbers/primenum.py 10           | 0.024752140045166016  | 0.02689361572265625   | 0.025563716888427734  |
|    1     |python ../02/primenumbers/primenum.py 1            | 0.024990558624267578  | 0.025903940200805664  | 0.0252683162689209    |
|    2     |python ../02/primenumbers/primenum.py 2            | 0.02878737449645996   | 0.02382183074951172   | 0.029026031494140625  |
|    3     |python ../02/primenumbers/primenum.py 3            | 0.029674291610717773  | 0.025368213653564453  | 0.028712749481201172  |
|    4     |python ../02/primenumbers/primenum.py 4            | 0.028914690017700195  | 0.024040699005126953  | 0.02916121482849121   |
|    5     |python ../02/primenumbers/primenum.py 5            | 0.029738187789916992  | 0.025082826614379883  | 0.03203582763671875   |
|    6     |python ../02/primenumbers/primenum.py 100          | 0.031174182891845703  | 0.02543926239013672   | 0.03127408027648926   |
|    7     |python ../02/primenumbers/primenum.py 1000         | 0.02927398681640625   | 0.02559041976928711   | 0.029406070709228516  |
|    8     |python ../02/primenumbers/primenum.py 10000        | 0.03594470024108887   | 0.026258230209350586  | 0.03755068778991699   |
|    9     |python ../02/primenumbers/primenum.py 100000       | 0.12144017219543457   | 0.042658090591430664  | 0.07487273216247559   |
|    10    |python ../02/primenumbers/primenum.py 1000000      | 1.4036412239074707    | 0.20000386238098145   | 0.3630061149597168    |
|    11    |python ../02/primenumbers/primenum.py 10000000     | 32.25389909744263     | 2.3835761547088623    | 3.5481419563293457    |
|    12    |python ../02/primenumbers/primenum.py 100000000    | xxxxxxxxxxxxxxxxxxx   | 23.466675519943237    | 39.15320873260498     |

## ДЗ 1. Циклы и рекурсия

1. Cоздана система тестирования и проверена на задаче "Length String"

        python console_tester.py --help
        usage: console_tester.py [-h] prog_exec test_dir

        Console Tester

        positional arguments:
        prog_exec   Full path for program execute
        test_dir    Full path to the test directory

        optional arguments:
        -h, --help  show this help message and exit

        python console_tester.py ../01/strlen/strlen.py ../01/test/0_strlen

2. Решена задача Lucky Tickets

        python console_tester.py ../01/tickets/ticket.py ../01/test/1_tickets
