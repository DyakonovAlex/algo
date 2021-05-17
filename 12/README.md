# algo

Otus course Algorithms and data structures

## 12. Алгоритм Бойера Мура

Реализовано:

- Обычным перебором
- Оптимизация по последнему символу - алгоритм Бойера-Мура-Хорспула
- Оптимизация по совпавшему суффиксу - алгоритм Бойера Мура

Пример работы алгоритма Бойера Мура:

- первая строчка текст
- вторая строчка шаблон
- знак "|" показывает где находимся

```bash
.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
bc.abc.bc.c.abc
              |
shift >> 15 (o <> c; sybmol: o - not in pattern)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
               bc.abc.bc.c.abc
                             |

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
               bc.abc.bc.c.abc
                            |
shift >> 4 (. <> b;symbol: c)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                   bc.abc.bc.c.abc
                                 |

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                   bc.abc.bc.c.abc
                               |
shift >> 6 (t <> a; suffix: bc)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                         bc.abc.bc.c.abc
                                       |

shift >> 2 (a <> c; symbol: a)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                           bc.abc.bc.c.abc
                                         |

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                           bc.abc.bc.c.abc
                                    |


shift >> 9 (v <> .; suffix: c.abc)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                                    bc.abc.bc.c.abc
                                                  |

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                                    bc.abc.bc.c.abc
                                    |
shift >> 9 (v <> b; suffix: c.abc)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                                             bc.abc.bc.c.abc
                                                           |

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                                             bc.abc.bc.c.abc
                                                         |
shift >> 6 (. <> a; suffix: bc)

.kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc
                                                   bc.abc.bc.c.abc
                                                                 |
```
