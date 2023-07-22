{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "\n",
    "\n",
    "def foo(freq_words: Counter) -> float:\n",
    "    return len(freq_words.keys())\n",
    "\n",
    "def frequency_of_a(freq_words: Counter) -> float:\n",
    "    keys = freq_words['а']\n",
    "    return keys\n",
    "\n",
    "def frequency_of_o(freq_words: Counter) -> float:\n",
    "    keys = freq_words['о']\n",
    "    return keys\n",
    "\n",
    "def frequency_of_e(freq_words: Counter) -> float:\n",
    "    keys = freq_words['е']\n",
    "    return keys\n",
    "\n",
    "def frequency_of_n(freq_words: Counter) -> float:\n",
    "    keys = freq_words['н']\n",
    "    return keys\n",
    "\n",
    "def frequency_of_t(freq_words: Counter) -> float:\n",
    "    keys = freq_words['т']\n",
    "    return keys\n",
    "\n",
    "def frequency_of_longest_word(freq_words: Counter) -> float:\n",
    "    keys = freq_words.keys()\n",
    "    longest = freq_words[sorted(keys)[0]]\n",
    "    return longest / len(keys)\n",
    "\n",
    "def count_upper_words(freq_words: Counter) -> float:\n",
    "    keys = freq_words.keys()\n",
    "    up_count = 0\n",
    "    for key in keys:\n",
    "        if key.isupper():\n",
    "            up_count += freq_words[key]\n",
    "\n",
    "    return up_count\n",
    "\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-07-22T07:13:52.651108700Z",
     "start_time": "2023-07-22T07:13:52.637145200Z"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "outputs": [],
   "source": [
    "freq_words = Counter(['а', 'qfqfq', 'FAFAFSASF', 'FAFAFSASF', 'AIOP' ])"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-07-22T07:13:53.594702100Z",
     "start_time": "2023-07-22T07:13:53.557701600Z"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
