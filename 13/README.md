# algo

Otus course Algorithms and data structures

## 13. Алгоритм RLE

Реализовано:

- программа для сжатия файлов
- программа для распаковки файлов

Программа принимает 3 аргумента:

- action:      zip or unzip.  
- src_name:    source file name
- dst_name:    destination file name

Примеры:

```bash
$ python rle.py -h                   
usage: rle.py [-h] action src_name dst_name

Zip / Unzip file

positional arguments:
  action      zip or unzip
  src_name    source file name
  dst_name    destination file name

optional arguments:
  -h, --help  show this help message and exit

$ python rle.py zip test.txt test.zip
$ python rle.py unzip test.zip test_2.txt
```

Неплохо работает для текстовой последовательности, типа "AAAAABBBCDGCBLL".  
Плохо работает для [обычного текста](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt)
