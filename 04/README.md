# algo

Otus course Algorithms and data structures

## 4. Базовые структуры данных

1. Динамические массивы:
   1. SingleArray
   2. VectorArray
   3. FactorArray
   4. MatrixArray

### Результаты работы алгоритмов

#### Запуск тестов

      python main.py

---
---
|       Class        |       Count        |                    Operation                     |                    Time (ms)                     |               Time per item (mks)                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |                    end insert                    |                 0.22125244140625                 |                0.110626220703125                 |
|    SingleArray     |        2000        |                    end insert                    |                415.6508445739746                 |                207.8254222869873                 |
|    VectorArray     |        2000        |                    end insert                    |                 1.06048583984375                 |                0.530242919921875                 |
|    FactorArray     |        2000        |                    end insert                    |                1.565694808959961                 |                0.7828474044799805                |
|    MatrixArray     |        2000        |                    end insert                    |                1.6438961029052734                |                0.8219480514526367                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |               insert at index 1000               |                1.5189647674560547                |                0.7594823837280273                |
|    SingleArray     |        2000        |               insert at index 1000               |                2355.022192001343                 |                1177.5110960006714                |
|    VectorArray     |        2000        |               insert at index 1000               |                1168.6089038848877                |                584.3044519424438                 |
|    FactorArray     |        2000        |               insert at index 1000               |                1182.7387809753418                |                591.3693904876709                 |
|    MatrixArray     |        2000        |               insert at index 1000               |                4538.961410522461                 |                2269.4807052612305                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |                insert at index 0                 |                3.942251205444336                 |                1.971125602722168                 |
|    SingleArray     |        2000        |                insert at index 0                 |                5160.975933074951                 |                2580.4879665374756                |
|    VectorArray     |        2000        |                insert at index 0                 |                3052.5505542755127                |                1526.2752771377563                |
|    FactorArray     |        2000        |                insert at index 0                 |                3355.6222915649414                |                1677.8111457824707                |
|    MatrixArray     |        2000        |                insert at index 0                 |                12639.03522491455                 |                6319.517612457275                 |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |                    end delete                    |                0.2434253692626953                |               0.12171268463134766                |
|    SingleArray     |        2000        |                    end delete                    |                2316.9050216674805                |                1158.4525108337402                |
|    VectorArray     |        2000        |                    end delete                    |                0.8757114410400391                |               0.43785572052001953                |
|    FactorArray     |        2000        |                    end delete                    |                0.8845329284667969                |               0.44226646423339844                |
|    MatrixArray     |        2000        |                    end delete                    |                1.6977787017822266                |                0.8488893508911133                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |               delete at index 1000               |                0.9927749633789062                |                0.4963874816894531                |
|    SingleArray     |        2000        |               delete at index 1000               |                2828.071355819702                 |                1414.035677909851                 |
|    VectorArray     |        2000        |               delete at index 1000               |                1261.228322982788                 |                 630.614161491394                 |
|    FactorArray     |        2000        |               delete at index 1000               |                1363.0273342132568                |                681.5136671066284                 |
|    MatrixArray     |        2000        |               delete at index 1000               |                5087.315320968628                 |                2543.657660484314                 |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |        2000        |                delete at index 0                 |                1.2271404266357422                |                0.6135702133178711                |
|    SingleArray     |        2000        |                delete at index 0                 |                3471.193790435791                 |                1735.5968952178955                |
|    VectorArray     |        2000        |                delete at index 0                 |                2058.6602687835693                |                1029.3301343917847                |
|    FactorArray     |        2000        |                delete at index 0                 |                608.1869602203369                 |                304.09348011016846                |
|    MatrixArray     |        2000        |                delete at index 0                 |                 7635.70761680603                 |                3817.853808403015                 |
---

|       Class        |       Count        |                    Operation                     |                    Time (ms)                     |               Time per item (mks)                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |                    end insert                    |                2.134561538696289                 |                0.2134561538696289                |
|    VectorArray     |       10000        |                    end insert                    |                22.350072860717773                |                2.2350072860717773                |
|    FactorArray     |       10000        |                    end insert                    |                 7.61103630065918                 |                0.761103630065918                 |
|    MatrixArray     |       10000        |                    end insert                    |                8.469820022583008                 |                0.8469820022583008                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |               insert at index 5000               |                34.273386001586914                |                3.4273386001586914                |
|    VectorArray     |       10000        |               insert at index 5000               |                31588.993787765503                |                3158.8993787765503                |
|    FactorArray     |       10000        |               insert at index 5000               |                34844.92611885071                 |                3484.492611885071                 |
|    MatrixArray     |       10000        |               insert at index 5000               |                127623.18396568298                |                12762.318396568298                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |                insert at index 0                 |                116.31298065185547                |                11.631298065185547                |
|    VectorArray     |       10000        |                insert at index 0                 |                86155.30157089233                 |                8615.530157089233                 |
|    FactorArray     |       10000        |                insert at index 0                 |                86965.86155891418                 |                8696.586155891418                 |
|    MatrixArray     |       10000        |                insert at index 0                 |                324640.3534412384                 |                32464.03534412384                 |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |                    end delete                    |                1.3201236724853516                |               0.13201236724853516                |
|    VectorArray     |       10000        |                    end delete                    |                3.778219223022461                 |                0.3778219223022461                |
|    FactorArray     |       10000        |                    end delete                    |                3.778696060180664                 |                0.3778696060180664                |
|    MatrixArray     |       10000        |                    end delete                    |                7.280826568603516                 |                0.7280826568603516                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |               delete at index 5000               |                19.632339477539062                |                1.9632339477539062                |
|    VectorArray     |       10000        |               delete at index 5000               |                32524.603605270386                |                3252.4603605270386                |
|    FactorArray     |       10000        |               delete at index 5000               |                32748.066425323486                |                3274.8066425323486                |
|    MatrixArray     |       10000        |               delete at index 5000               |                132202.84175872803                |                13220.284175872803                |
| ------------------ | ------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
|     RealArray      |       10000        |                delete at index 0                 |                33.08558464050293                 |                3.308558464050293                 |
|    VectorArray     |       10000        |                delete at index 0                 |                50295.69697380066                 |                5029.569697380066                 |
|    FactorArray     |       10000        |                delete at index 0                 |                16781.282424926758                |                1678.1282424926758                |
|    MatrixArray     |       10000        |                delete at index 0                 |                198195.81151008606                |                19819.581151008606                |
---

#### Комментарии

1. Операция **"Вставка к конец"**. SingleArray ожидаемо работает хуже всех: мы каждый раз перестраиваем массив. Быстрее всего, при вставке 2000, получилось у VectorArray: его первоначальный размер 1000 и он только один раз перестроился. Но при вставке 10 000, видно, что это не самое оптимальное решение. FactorArray, c небольшим отрывом, на первом месте, MatrixArray на втором.
2. Операция **"Вставка в середину"**. SingleArray ожидаемо работает хуже всех: мы каждый раз перестраиваем массив и двигаем все элементы. VectorArray и FactorArray работают практически с одинаковой скоростью, и для 2 000, и для 10 000. MatrixArray работает в 4 раза медленней из-за более сложный рассчетов.
3. Операция **"Вставка в начало"**. Ситуация аналогична встаке в середину. Только времени тратится больше из-за большего объема копируемых данных.
4. Операция **"Удаление последнего"**. SingleArray работает медленнее всех из-за постоянного перестроения. VectorArray и FactorArray работают примерно одинаково по времени из-за одинакового количества операций. MatrixArray работает в 2 раза дольше из-за более сложных вычислений при доступе к элементу.
5. Операция **"Удаление из середины"**. Ситуация аналогична операции **"Вставка в середину"**
6. Операция **"Удаление сначала"**. FactorArray быстрее всех из-за более оптимального размера массива. MatrixArray хуже всех из-за более сложных вычислений при доступе к элементу.

#### Выводы

1. SingleArray - оптимально по памяти, но любая операция ведет к перевыделению памяти и поэтому работает долго.
2. VectorArray - совсем не оптимально по памяти, выделяем сразу с большим запасом. Эффективен при вставке / удалении в конец массива.
3. FactorArray - более эффективен по памяти, чем предыдущий, выделяем память пропорционально уже выделенной.
4. MatrixArray - из-за более сложной организации хранения, требуется больше времени для доступа к элементу. Только вставка в конец дает хорошие результаты. В остальном, результаты хуже чем в остальных структурах.
