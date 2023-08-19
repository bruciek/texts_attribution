## Документация

### Загрузка библиотеки.

1. Поместите `Text.py` в рабочую директорию.
2. Подключите библиотеку в вашей программе следующим образом:

```python
from Text import Text
```

### Описание

Библиотека `Text.py` содержит в себе реализованный класс `Text`, который содержит следующие поля:

* `text: str` - текст представляющий собой питоновский `str`.
* `size: int` - количество слов в `text`.
* `change_points: list[int]` - последовательность моментов разладок в тексте.

### Инициализация класса.

1. **Через конструктор класса (для явной передачи текста)**.

```python
Text(text: tp.Optional[str] = None,
     preprocessing: bool = True,
     change_points: tp.Optional[list[int]] = None)
```

<details><summary><a>Параметры</a></summary> 

* `text: str` - текст который передаем в класс
* `preprocessing: bool` - параметр предобработки текста.
* `change_points: list[int]` - передаваемые моменты разладки, если текст уже является склееным.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text(text = "Это какой-то текст", preprocessing = True, change_points = None)
```

</details>

2. **Через классовый метод (для чтения из файла)**

```python
Text.read_txt(path: str,
              preprocessing: tp.Optional[bool] = True,
              change_points: tp.Optional[list[int]] = None)
```

<details><summary><a>Параметры</a></summary> 

* `path: str` - путь к файлу расширения `txt`.
* `preprocessing: bool` - параметр предобработки текста.
* `change_points: list[int]` - передаваемые моменты разладки, если текст уже является склееным.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/chapter_1.txt')
```

</details>

### Базовые операции над текстом

Поддерживаются базовые операции аналогичные для строк.

* **Унарные:**
    * `len()` - возвращает количество слов в тексте.
    * `str()` - возвращает `Text.text`.
    * `print()` - печатает `Text.text`.

* **Бинарные:**
    * `+` - возвращает текст, полученный конкатенацией двух текстов (автоматически увеличивает размер и добавляет
      момент разладки).

P.S. **Это не методы класса, а перегруженные операции питона!**

### Методы класса

0. **Технические методы**

`most_used_words` - находит самые популярные слова в тексте.

<details><summary><a>Параметры.</a></summary> 

* `n: int` - количество слов.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает словарь из `n` самых используемых слов в тексте, где ключи - слова, а значения - частота слова в тексте.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.most_used_words(n = 10)
```

</details>


`words_count` - считает количество заданных слов в тексте.

<details><summary><a>Параметры.</a></summary> 

* `words: list[str]` - слова используемые для подсчета.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает число слов из списка `words` встреченных в тексте.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.words_count(words = ['и', 'но', 'а'])
```

</details>


`empiric_bridge` - возвращает значения эмпирического моста, построенного по заданному инварианту.

<details><summary><a>Параметры.</a></summary> 

* `invariant: list[str]` - опциональный параметр, отвечающий за авторский инвариант.
    * `Text.special_words` - все служебные слова (по умолчанию).

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает пару состояющую из двух массивов (`x: np.ndarray` ,`y: np.ndarray`), которые задают координаты эмпирического
моста по соотвествующим осям.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.empiric_bridge(invariant = ['а', 'и', 'но'])
```

</details>


`empiric_bridge_plot` - строит график эмприрического моста, построенного по заданному инварианту.

<details><summary><a>Параметры.</a></summary> 

* `texts: list['Text']` - тексты, для которых строятся графики эмпирического моста.
* `titles: list[str]` - опциональный параметр, отвечает за легенды для графиков эмпирического моста.
* `invariant: list[str]` - опциональный параметр, отвечающий за авторский инвариант.
    * `Text.special_words` - все служебные слова (по умолчанию).
* `change_points: bool` - опциональный параметр, отвечающий за отрисовку моментов разладки. По умолчанию равен `True`. Работает, только если подаётся список из одного текста.
* `mode: Callable` - опциональный параметр, отвечающий за то, какую функцию применить к значениям эмпирического моста.  
* `show: bool` - опциональный параметр, отвечающий за то, показывать ли построенный график. По умолчанию равен `False`.

</details>

<details><summary><a>Возвращаемое значение</a></summary>
Возвращает график эмпирических мостов для заданного списка текстов.
</details>

<details><summary><a>Пример.</a></summary> 

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
fig = Text.empiric_bridge_plot(texts=[T1, T2], titles=['Глава 1', 'Глава 2'],
                         invariant = ['а', 'и', 'но'], mode = abs)
fig.show()
```

</details>


`empiric_bridge_maximum_norm` - sup-статистика для эмпирического моста.

<details><summary><a>Параметры.</a></summary> 

* `invariant: list[str]` - опциональный параметр, отвечающий за авторский инвариант.
    * `Text.special_words` - все служебные слова (по умолчанию).

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает максимальное отклонение от `0` эмпирического моста.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.empiric_bridge_maximum_norm(invariant = ['а', 'и', 'но'])
```

</details>


`words_relative_frequency` - считает частоту каждого из заданных слов по тексту. Отличие от метода `words_count` состоит в том, что частота возвращается для каждого слова из заданных в отдельности.

<details><summary><a>Параметры.</a></summary> 

* `words: list[str]` - слова используемые для подсчета.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

В виде словаря для каждого слова из списка `words` возвращает частоту, с которой оно встретилось в тексте.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.words_relative_frequency(words = ['и', 'но', 'а'])
```

</details>


`MSE_words_relative_frequency` - для каждого из заданных слов вычисляет среднеквадратичное отклонение для выборки из частот его появления в заданном списке текстов.

<details><summary><a>Параметры</a></summary> 

* `words: list[str]` - слова, для которых вычисляется среднеквадратичное отклонение
* `texts: list['Text']` - тексты, по которым для каждого слова строится выборка из частот.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

В виде словаря для каждого слова из списка `words` возвращает среднеквадратичное отклонение.

</details>

<details><summary><a>Пример.</a></summary>

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
T3 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_3.txt')
Text.mse_words_relative_frequency(words=["а", "и"], texts=[T1, T2, T3])
```

</details>


`transition_frequencies` - по заданному алфавиту оценивает двумерный массив частот перехода от символа к символу в тексте.

<details><summary><a>Параметры.</a></summary>

* `alphabet: list[str]` - алфавит, переходы между символами которого учитываются.

</details>

<details><summary><a>Возвращаемое значение.</a></summary>

Возвращает в виде двумерного массива матрицу частот переход от символа к символу.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.transition_frequencies(alphabet = ["а", "б", "в", "г"])
```

</details>


`transition_probabilities` - по заданному алфавиту оценивает двумерную матрицу переходных вероятностей от символа к символу в тексте.

<details><summary><a>Параметры</a></summary> 

* `alphabet: list[str]` - алфавит, переходы между символами которого учитываются.

* `transition_frequencies: np.ndarray` - опциональный параметр, матрица частот перехода.
    * `None` - значение по умолчанию. В этом случае частоты оцениваются по тексту с помощью метода `transition_frequencies`.

</details>

<details><summary><a>Возвращаемое значение.</a></summary>

Возвращает в виде двумерного массива матрицу переходных вероятностей от символа к символу.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.transition_probabilities(alphabet = ["а", "б", "в", "г"])
```

</details>


`unique_word_process` - процесс количеств слов в тексте, встретившихся хотя бы один раз.

<details><summary><a>Параметры</a></summary> 

* `mode` - опциональный параметр, отвечающий за обход текста.
    * `forward ` - прямой обход (по умолчанию).
    * `reverse` - обратный обход.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает массив значений, где на `i`-ом месте стоит количество слов, встретившихся хотя бы один раз, в первых `i` словах текста.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.unique_word_process(mode = 'reverse')
```

</details>


`unique_word_process_plot` - строит график процесса количеств слов в тексте, встретившихся хотя бы один раз.

<details><summary><a>Параметры</a></summary> 

* `mode` - опциональный параметр, отвечающий за обход текста.
    * `forward ` - прямой обход.
    * `reverse` - обратный обход.
    * `both`(по умолчанию) - оба обхода на одном графике.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.unique_word_process_plot(mode = 'reverse')
```

</details>


`once_word_process` - процесс количеств слов в тексте, встретившихся ровно один раз.

<details><summary><a>Параметры</a></summary> 

* `mode` - опциональный параметр, отвечающий за обход текста.
    * `forward` (по умолчанию) - прямой обход.
    * `reverse` - обратный обход. 

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает массив значений, где на `i`-ом месте стоит количество слов, встретившихся ровно один раз в первых `i` словах
текста.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.once_word_process(mode = 'reverse')
```

</details>


`once_word_process_plot` - строит график процесса количеств слов в тексте, встретившихся ровно один раз.

<details><summary><a>Параметры</a></summary> 

* `mode` - опциональный параметр, отвечающий за обход текста.
    * `forward ` - прямой обход.
    * `reverse` - обратный обход.
    * `both`(по умолчанию) - оба обхода на одном графике.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.once_word_process_plot(mode = 'reverse')
```

</details>


1. **Методы атрибуции и проверки на однородность с помощью авторского инварианта**.

`invariant_naive_test` - определяет к какому тексту ближе оригинал на основе частот. Не является статистическим тестом.

<details><summary><a>Параметры</a></summary> 

* `text: 'Text'` - оригинальный текст.
* `text1: 'Text'` - первый текст для сравнения.
* `text2: 'Text'` - второй текст для сравнения.
* `invariant: list[str]` - опциональный параметр, отвечающий за авторский инвариант. 
    * `text.most_used_words(10)` - топ-10 по популярности слов в оригинальном тексте (по умолчанию).

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает три числа - частоты появления представителей инварианта в каждом из текстов.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_3.txt')
Text.invariant_naive_test(T, T1, T2, invariant = ['а', 'но'])
```

</details>


`invariant_attribution_test` - проверка двух заданных тестов на совместную однородность.

<details><summary><a>Параметры</a></summary> 

* `text1: 'Text'` - первый текст.
* `text2: 'Text'` - второй текст.
* `invariant: list[str]` - опциональный параметр, отвечающий за авторский инвариант. 
    * `Text.special_words` - служебные слова (по умолчанию).

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает пару состоящую из статистики и p-value `(stat, p-value)`.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
Text.invariant_attribution_test(T1, T2, invariant=['а', 'но'])
```

</details>


`empiric_bridge_test` - тест на однородность, основанный на эмпирическом мосте, построенном по заданному инварианту.

<details><summary><a>Параметры</a></summary> 

* `invariant: list[str]` - авторский инвариант. Если не указан, то по умолчанию берутся все служебные слова.

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает пару состоящую из статистики и p-value `(stat, p-value)`.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.empiric_bridge_test(invariant = ['а', 'и', 'но'])
```

</details>


`best_invariant` - подбирает инвариант, минимизирующий максимум-норму эмпирического моста с помощью жадного алгоритма.

<details><summary><a>Параметры</a></summary> 

* `words: list[str]` - слова среди которых ищем инвариант.
    * `Text.special_words` (по умолчанию) - все служебные слова.
* `max_iter: int` - максимальное число слов в инварианте (5 по умолчанию).
* `mode: bool` - параметр, отвечающий за вывод промежуточных результатов (`False` по умолчанию).

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает инвариант, минимизирующий отклонение эмпирического моста.

</details>

<details><summary><a>Пример.</a></summary>

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.best_invariant(words=T.most_used_words(100), max_iter=5, mode=True)
```

</details>


2. **Метод атрибуции с помощью дельты Бёрроуза**

`burrows_delta` - дельта Бёрроуза между двумя текстами.

<details><summary><a>Параметры</a></summary>

* `text1: 'Text'` - первый текст.
* `text2: 'Text'` - второй текст.
* `words: list[str]` - опциональный параметр, отвечающий за список слов, по которым вычисляется дельта Бёрроуза.
    * `Text.special_words` - все служебные слова (по умолчанию).
* `texts: list['Text']` - опциональный параметр, отвечающий за совокупность текстов, по которым вычисляется среднеквадратическое отклонение.
    * `[text1, text2]` - список из первого и второго текста (по умолчанию).

</details>

<details><summary><a>Возвращаемое значение</a></summary>

Возвращает значение дельты Бёрроуза между текстами `text1` и `text2`.

</details>

<details><summary><a>Пример.</a></summary>

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
T3 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_3.txt')
Text.burrows_delta(T1, T2, words = Text.special_words, texts = [T1, T2, T3])
```

</details>


3. **Метод атрибуции с помощью статистики Хмелёва**

`one_sided_khmelev_statistics` - вычисляет приведённую статистику Хмелёва для первого текста относительно второго.

<details><summary><a>Параметры.</a></summary> 

* `text1: 'Text'`
* `text2: 'Text'`

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает приведённую (делённую на количество символов) статистику Хмелёва для `text1` относительно `text2`.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
Text.one_sided_khmelev_statistics(T1, T2)
```

</details>


`khmelev_statistics` - вычисляет приведённую статистику Хмелёва для первого текста относительно второго и наоборот.

<details><summary><a>Параметры.</a></summary> 

* `text1: 'Text'`
* `text2: 'Text'`

</details>

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает кортеж из приведённых (делённых на количество символов) статистик Хмелёва для `text1` относительно `text2` и для `text2` относительно `text1`.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T1 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T2 = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_2.txt')
Text.khmelev_statistics(T1, T2)
```

</details>


4. **Методы атрибуции и проверки на однородность, основанные на бесконечной урновой схеме**

`unique_word_process_test` - тест на однородность, основанный на процессе количеств слов, встретившихся в тексте хотя бы один раз.

<details><summary><a>Возвращаемое значение.</a></summary> 

Возвращает пару, состоящую из статистики и p-value `(stat, p-value)`.

</details>

<details><summary><a>Пример.</a></summary> 

```python
T = Text.read_txt('Eugene Onegin/Texts/preprocessed/chapter_1.txt')
T.unique_word_process_test()
```

</details>
