def freq_of_symbol(text: str, symbols_for_freq: set[str]) -> float:
    symbols_count = 0
    for symbol in symbols_for_freq:
        symbols_count += text.count(symbol)

    return symbols_count / len(text)
