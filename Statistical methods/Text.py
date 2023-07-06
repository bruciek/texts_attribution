import scipy.stats as st

import numpy as np
import pandas as pd
import typing as tp
import plotly.express as px
import plotly.graph_objs as go
from bokeh.palettes import magma

from collections import Counter
from itertools import product


class Text:
    
    special_words = 'в на с за к по из у от для во без до о через со при про' \
                    ' об ко над из-за из-под под и что но а да хотя когда чтобы ' \
                    'если тоже или зато будто не как же ж даже бы ли только вот то' \
                    'ни лишь ведь вон нибудь уже либо'.split()

    def __init__(
            self,
            text: tp.Optional[str] = None,
            preprocessing: bool = True,
            change_points: tp.Optional[tp.List[int]] = None,

    ) -> None:
        if preprocessing:
            self.text = Text.preprocessing(text)
        else:
            self.text = text

        self.size = len(self.text.split())

        if change_points is None:
            self.change_points = []
        else:
            self.change_points = change_points

    def __add__(self, text2: 'Text') -> 'Text':
        """
       :param text2:
       :return: Return concatenation of Text1 and Text2
       """

        if self.size > 0:
            result = Text(text=self.text + ' ' + text2.text, preprocessing=False, 
                          change_points=self.change_points + [self.size] + text2.change_points)
        else:
            result = Text(text=self.text + text2.text, preprocessing=False, 
                          change_points=self.change_points + text2.change_points)
        
        return result

    def __len__(self) -> int:

        """
        :return: size of text
        """
        return self.size

    def __str__(self) -> str:

        """
        :return: text
        """
        return self.text

    @classmethod
    def read_txt(cls, path: str,
                 preprocessing: tp.Optional[bool] = True,
                 change_points: tp.Optional[tp.List[int]] = None) -> 'Text':
        try:
            return Text(open(path).read(), preprocessing=preprocessing, change_points=change_points)
        except FileNotFoundError:
            raise FileNotFoundError

    @classmethod
    def preprocessing(cls, text: str) -> str:

        """
        Naive preprocessing - remove special symbols.
        :param text: sting for preprocessing.
        :return: parsed string.
        """

        text = ' '.join(text.lower().split())
        
        symbols = ['»', '«', ')', '(', '[', ']', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…', '–',
                   '—', 'X', 'V', 'I', 'L', '*', '/', '"', '-', ',', '.', '?', '!', '{', '}', 'a', 'b', 'c', 'd', 'e', 
                   'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z', "'"]

        for s in symbols:
            text = text.replace(s, '')
            
        return ' '.join(text.lower().split())
    
    def to_txt(self, path: str) -> None:
        try:
            file = open(path, "w")
            file.write(str(self))
            file.close()
        
        except FileNotFoundError:
            raise FileNotFoundError

    def most_used_words(self, n: int) -> tp.Dict[str, int]:

        """
        :param n: 
        :return dict of n the most used words in the text
        """

        return dict(Counter(self.text.split(' ')).most_common(n))

    def words_count(self, words: tp.List[str]) -> int:

        """
        :param words:
        :return number of words from invariant encountered in the text
        """

        count = 0
        for word in self.text.split():
            if word in words:
                count += 1
        return count

    def empiric_bridge(self, invariant: tp.Optional[tp.List[str]] = None) -> tp.Tuple[np.ndarray, np.ndarray]:

        """
        :param invariant:
        :return: tp.Tuple of coordinates of x-axis and coordinates of y-axis
        """
        if invariant is None:
            invariant = self.special_words

        n = self.size
        sample_indicators = np.array([int(i) for i in [item in invariant for item in self.text.split()]])

        var = sample_indicators.var()
        s_n = sample_indicators.sum()
        x = np.array([i / n for i in range(n+1)])
        y = np.array([(n * sample_indicators[:k].sum() - k * s_n) / (np.sqrt(var) * n * np.sqrt(n))
                      for k in range(n+1)])

        return x, y

    @classmethod
    def empiric_bridge_plot(cls, texts: tp.List['Text'], titles: tp.Optional[tp.List[str]] = None,
                            invariant: tp.Optional[tp.List[str]] = None,
                            change_points: tp.Optional[bool] = False, mode: tp.Optional[tp.Callable] = None,
                            show: tp.Optional[bool] = False) -> go.Figure:
        """
        :param texts:
        :param titles:
        :param invariant:
        :param change_points:
        :param mode:
        :param show:
        :return:
        """
        if invariant is None:
            invariant = Text.special_words

        if titles is None:
            titles = [f'Текст {i+1}' for i in range(len(texts))]

        if mode is None:
            def mode(arg):
                return arg

        # Итоговый рисунок
        fig = go.Figure(
            layout=go.Layout(
                width=800,
                height=600,
                title="Эмпирический мост",
                template="none",
                font={'color': 'black', 'family': 'Times New Roman', 'size': 14},
                xaxis={'title': '$t$'},
                yaxis={'title': '$Z_{n}(t)$'}
            )
        )
        colors = magma(len(texts)*3)

        for i in range(len(texts)):
            text = texts[i]
            title = titles[i]
            x, y = text.empiric_bridge(invariant=invariant)
            y = mode(y)
            fig = fig.add_trace(go.Scatter(
                name=title,
                x=x,
                y=y,
                mode='lines',
                marker=dict(color=colors[3*i]),
                line=dict(width=1),
                legendgroup=f"{i}",
                showlegend=True)
            )
            fig.add_trace(go.Scatter(
                name=title,
                x=x,
                y=[y[np.where(np.abs(y) == np.max(np.abs(y)))[0][0]]] * len(x),
                line=dict(
                    color=colors[3*i],
                    width=1,
                    dash="dashdot"
                ),
                mode="lines",
                legendgroup=f"{i}",
                showlegend=False
            )
            )

        if len(texts) == 1 and change_points:
            for i in texts[0].change_points:
                fig.add_vline(x=i / texts[0].size, line_width=1, line_dash="dash", line_color="red")

        if show:
            fig.show()

        return fig

    def empiric_bridge_maximum_norm(self, invariant: tp.Optional[tp.List[str]] = None) -> float:
        if invariant is None:
            invariant = self.special_words

        """
        :param invariant:
        :return: 'sup'-statistic (J_infinity) using empiric bridge.
        """
        return max(abs(i) for i in self.empiric_bridge(invariant)[1])

    def words_relative_frequency(self, words: tp.List[str]) -> tp.Dict[str, float]:
        """
        :param words:
        :return frequency for any word in words
        """
        dicttext = Counter([word for word in self.text.split() if word in words])
        result = {}
        for word in words:
            if word not in dicttext:
                dicttext[word] = 0
            else:
                result.update({word: dicttext[word] / len(self.text.split())})
        return result
    
    @classmethod
    def mse_words_relative_frequency(cls, words: tp.List[str], texts: tp.List['Text']) -> tp.Dict[str, float]:
        """
        :param words:
        :param texts:
        :return MSE for any word in words where mean frequency corresponds to general population
        """
        
        # по списку текстов получаем
        d = [txt.words_relative_frequency(words) for txt in texts]
        
        # считаем среднюю частоту слова по всем тестам
        average = {}
        for word in words:
            mu = 0 
            for text in d:
                mu += text[word]
            mu = mu / len(d)
            average[word] = mu
    
        # получаем нужный словарь
        mse_dict = {}
        for word in words:
            sigma = 0
            for text in d:
                sigma += (text[word]-average[word])**2
            sigma = np.sqrt(sigma/len(d))
            mse_dict[word] = sigma
    
        return mse_dict
    
    def transition_frequencies(self, alphabet: tp.List[str]) -> np.ndarray:
        """
        :param alphabet:
        :return transition frequencies in text for each pair of alphabet symbols 
        """
        
        alphabet.sort()
        
        transition_dictionary_keys = list(product(alphabet, alphabet))
        transition_dictionary = dict.fromkeys(transition_dictionary_keys, 0.0)
        
        text_arr = list(str(self))
        if text_arr[-1] != " ":
            text_arr += [" "]
            
        for k in range(len(text_arr)-1):
            if (text_arr[k], text_arr[k+1]) in transition_dictionary.keys():
                transition_dictionary[(text_arr[k], text_arr[k+1])] += 1
        
        freq = np.array([[transition_dictionary[(alphabet[i], alphabet[j])] for j in range(len(alphabet))] 
                         for i in range(len(alphabet))])
        
        return freq
     
    def transition_probabilities(self, alphabet: tp.List[str],
                                 transition_frequencies: tp.Optional[np.ndarray] = None) -> np.ndarray:
        """
        :param alphabet:
        :param transition_frequencies:
        :return transition probabilities in text for each pair of alphabet symbols 
        """
        if transition_frequencies is None:
            transition_frequencies = self.transition_frequencies(alphabet)
           
        m = len(alphabet)
        
        result = np.array([[transition_frequencies[i, j]/sum(transition_frequencies[i, :]) 
                            if sum(transition_frequencies[i, :]) > 0 else 0 for j in range(m)] for i in range(m)])
        return result
    
    def unique_word_process(self, mode: tp.Optional[str] = None) -> np.ndarray:
        """
        :param mode: forward (None by default) or reverse.
        :return:
        """
        words = []
        if mode in {None, 'forward'}:
            words = self.text.split(" ")
        elif mode == 'reverse':
            words = self.text.split(" ")
            words.reverse()
        elif mode not in {None, 'forward', 'reverse'}:
            raise NameError

        unique_words = []
        unique_proc = []
        unique_counter = 0

        # подсчет уникальных слов
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
                unique_counter += 1
            unique_proc.append(unique_counter)
        return np.array(unique_proc)
    
    def unique_word_process_plot(self, mode: tp.Optional[str] = None, name: tp.Optional[str] = None,
                                 change_points: tp.Optional[bool] = False,
                                 show: tp.Optional[bool] = False) -> go.Figure:
        """
        :param mode:
        :param name:
        :param change_points:
        :param show:
        :return:
        """
        y_forward = self.unique_word_process(mode='forward')
        y_reverse = self.unique_word_process(mode='reverse')
        fig = go.Figure(layout=go.Layout(
            width=800,
            height=600,
            title="Количество уникальных слов",
            template="none",
            font={'color': 'black', 'family': 'Times New Roman', 'size': 14},
            xaxis={'title': '$k$'},
            yaxis={'title': '$R_{n}(k)$'}
        ))
        if mode not in {'forward', 'reverse', 'both', None}:
            raise NameError
        if mode in {'forward', 'both', None}:
            if name is None:
                name_forward = "Прямой обход"
            else:
                name_forward = name + ", прямой обход"
            fig = fig.add_trace(go.Scatter(
                name=name_forward,
                x=np.arange(len(y_forward)),
                y=y_forward,
                mode='lines',
                marker=dict(color="red"),
                line=dict(width=1.5),
                showlegend=True)
            )
        if mode in {'reverse', 'both', None}:
            if name is None:
                name_backward = "Обратный обход"
            else:
                name_backward = name + ", обратный обход"
            fig = fig.add_trace(go.Scatter(
                name=name_backward,
                x=np.arange(len(y_reverse)),
                y=y_reverse,
                mode='lines',
                marker=dict(color="blue"),
                line=dict(width=1.5),
                showlegend=True)
            )
        if change_points:
            for i in self.change_points:
                fig.add_vline(x=i, line_width=1, line_dash="dash", line_color="red")
        if show:
            fig.show()
        return fig
    
    def once_word_process(self, mode: tp.Optional[str] = None) -> np.ndarray:
        
        """
        :param mode:
        :return:
        """
        if mode in {None, 'forward'}:
            words = self.text.split(" ")
        elif mode == 'reverse':
            words = self.text.split(" ")
            words.reverse()
        else:
            raise NameError

        answ = [0]
        seen_words: tp.Dict[str, int] = {}
        for word in words:
            if word not in seen_words:
                seen_words[word] = 1
                answ.append(answ[-1] + 1)
            else:
                if seen_words[word] == 1:
                    answ.append(answ[-1] - 1)
                    seen_words[word] += 1
                else:
                    answ.append(answ[-1])
        return np.array(answ[1:])
    
    def once_word_process_plot(self, mode: tp.Optional[str] = None) -> None:
        """
        :param mode:
        :return:
        """
        if mode == 'forward':
            y_forward = self.once_word_process(mode='forward')
            fig = px.line(pd.DataFrame(data=pd.DataFrame({'forward': y_forward})), title='R1 plot')
        elif mode == 'reverse':
            y_reverse = self.once_word_process(mode='reverse')
            fig = px.line(pd.DataFrame(data=pd.DataFrame({'reverse': y_reverse})), title='R1 plot')
        elif mode in {'both', None}:
            y_forward = self.once_word_process(mode='forward')
            y_reverse = self.once_word_process(mode='reverse')
            fig = px.line(pd.DataFrame(data=pd.DataFrame({'reverse': y_reverse, 'forward': y_forward})),
                          title='R1 plot')
        else:
            raise ValueError

        for i in self.change_points:
            fig.add_vline(x=i, line_width=3, line_dash="dash", line_color="red")
        fig.show()
         
    @classmethod
    def invariant_naive_test(cls, text: 'Text', text1: 'Text', text2: 'Text',
                             invariant: tp.List[str] = None) -> tp.Tuple[float, float, float]:
        """
        :param text:
        :param text1:
        :param text2:
        :param invariant:
        :return: return tp.Tuple of frequencies of words in invariant for the three texts
        """
        
        if invariant is None:
            invariant = Text.special_words

        size_0 = text.size
        size_1 = text1.size
        size_2 = text2.size

        invariant_0 = text.words_count(invariant)
        invariant_1 = text1.words_count(invariant)
        invariant_2 = text2.words_count(invariant)

        frequency_0 = invariant_0 / size_0
        frequency_1 = invariant_1 / size_1
        frequency_2 = invariant_2 / size_2
        return frequency_0, frequency_1, frequency_2
    
    @classmethod
    def invariant_attribution_test(cls, text1: 'Text', text2: 'Text',
                                   invariant: tp.Optional[tp.List[str]] = None) -> tp.Tuple[float, float]:

        """
        :param text1:
        :param text2:
        :param invariant:
        :return: tp.Tuple of attribution test statistic and p-value
        """
        if invariant is None:
            invariant = Text.special_words

        n1 = text1.size
        n2 = text2.size
        x = text1.words_count(invariant) / n1
        y = text2.words_count(invariant) / n2
        p = (n1 * x + n2 * y) / (n1 + n2)
        statistics = abs(x - y) / np.sqrt((p * (1 - p) * (1 / n1 + 1 / n2)))
        return statistics, 2 * (1 - st.norm.cdf(statistics))
    
    def empiric_bridge_test(self, invariant: tp.List[str] = None) -> tp.Tuple[float, float]:

        """
        :param invariant:
        :return: tp.Tuple of empiric bridge test statistic and p-value
        """
        if invariant is None:
            invariant = self.special_words
        summ = 0
        m = self.empiric_bridge_maximum_norm(invariant)
        for k in range(1, 1000):
            summ += 2 * (-1) ** (k + 1) * np.exp(-2 * k ** 2 * m ** 2)
        return m, summ
    
    def best_invariant(self, words: tp.Optional[tp.List[str]] = None, max_iter: int = 5,
                       mode: bool = False) -> tp.List[str]:
        """
        :param words:
        :param max_iter:
        :param mode: for printing intermediate results
        :return: return best invariant (greedy algorithm)
        """
        if words is None:
            words = self.special_words
        best_inv = []
        for i in range(max_iter):
            eps = 10000
            new_word = ''
            for word in words:
                cur_invariant = best_inv + [word]
                m = self.empiric_bridge_maximum_norm(cur_invariant)
                if m < eps:
                    eps = m
                    new_word = word
                if mode:
                    print(cur_invariant, m)
            if new_word in best_inv:
                return best_inv
            best_inv.append(new_word)
        return best_inv

    @classmethod
    def burrows_delta(cls, text1: 'Text', text2: 'Text', words: tp.Optional[tp.List[str]] = None,
                      texts: tp.Optional[tp.List['Text']] = None) -> float:
        """
        :param text1:
        :param text2:
        :param words:
        :param texts:
        :return Burrow's delta between two texts (text1 and text2)
        """
        if words is None:
            words = Text.special_words

        if texts is None:
            texts = [text1, text2]
        
        learned_dict = Text.mse_words_relative_frequency(words=words, texts=texts)
        dict2 = text1.words_relative_frequency(words)
        dict1 = text2.words_relative_frequency(words)
    
        delta = 0
        for word in words:
            if learned_dict[word] > 0:
                delta += abs(dict1[word] - dict2[word])/learned_dict[word]
            
        delta = delta / len(words)
        return delta

    @classmethod
    def one_sided_khmelev_statistics(cls, text1: 'Text', text2: 'Text') -> float:
        """
        :param text1:
        :param text2:
        :return left and right Khmelev statistics for text1 and text2
        """
        # Делаем список из символов первого текста и добавляем в конец пробел
        text1_arr = list(str(text1))
        if text1_arr[-1] != " ":
            text1_arr.append(" ")
    
        # Формируем алфавит
        alphabet = list(set(text1_arr))
        alphabet.sort()
    
        # Формируем массив частот для первого текста         
        nu = text1.transition_frequencies(alphabet)
        # Подсчитываем вероятности для первого текста
        trans_prob_matr1 = text1.transition_probabilities(alphabet=alphabet, transition_frequencies=nu)
    
        # Подсчитываем вероятности для второго текста
        trans_prob_matr2 = text2.transition_probabilities(alphabet=alphabet)
    
        # Делаем меру для первого текста абсолютно непрерывной относительно меры для второго текста
        trans_prob_matr1[trans_prob_matr2 == 0] = 0
    
        # Обуславливаем меру, чтобы получить вероятностное распределение
        trans_prob_matr1 = np.array([[trans_prob_matr1[i, j]/np.sum(trans_prob_matr1[i])
                                      if np.sum(trans_prob_matr1[i]) > 0 else 0
                                      for j in range(trans_prob_matr1.shape[1])]
                                     for i in range(trans_prob_matr1.shape[0])])

        # Функция для вычисления статистики Хмелёва
        func = np.vectorize(lambda x, y: 0.0 if x == 0 or y == 0 else np.log(x/y))
        
        h_12 = np.sum(nu * func(trans_prob_matr1, trans_prob_matr2))
    
        return h_12/np.sum(nu)
    
    @classmethod
    def khmelev_statistics(cls, text1: 'Text', text2: 'Text') -> tp.Tuple[float, float]:
        """
        :param text1:
        :param text2:
        :return:
        """
        
        return Text.one_sided_khmelev_statistics(text1, text2), Text.one_sided_khmelev_statistics(text2, text1)

    def unique_word_process_test(self) -> tp.Tuple[float, float]:
        """
        :return: tp.Tuple of unique test statistic and p-value
        """

        def theta_hat(unique_proc_arg: np.ndarray, unique_proc_rev_arg: np.ndarray) -> float:
            word_amount_temp = len(unique_proc_arg)
            return np.log2(unique_proc_arg[word_amount_temp - 1] / np.sqrt(
                unique_proc_arg[(word_amount_temp - 1) // 2] * unique_proc_rev_arg[(word_amount_temp - 1) // 2]))
            # подсчет K со страницы 204

        unique_proc = self.unique_word_process('forward')
        unique_proc_rev = self.unique_word_process('reverse')

        word_amount = len(unique_proc)
        j_obs = 0
        for i in range(word_amount):
            j_obs += unique_proc[i] - unique_proc_rev[i]
        j_obs = abs(j_obs / (word_amount * np.sqrt(unique_proc[word_amount - 1])))

        theta = theta_hat(unique_proc, unique_proc_rev)
        return j_obs * np.sqrt(1 + 2 / theta), 1 - st.norm.cdf(j_obs * np.sqrt(1 + 2 / theta))
