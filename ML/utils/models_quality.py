from sklearn.metrics import accuracy_score


def cross_val(df, model):
    accuracy = []
    for shift in range(0, 10, 2):
        authors_seen = []
        test_ixs = []
        for ixs in range(len(df)):
            aut = df['targets'][ixs]
            if authors_seen.count(aut) < 2:
                authors_seen += [aut]
                test_ixs += [ixs + shift]
        train_ixs = list(set(range(len(df))) - set(test_ixs))
        y_test = df.iloc[test_ixs]['target']
        x_test = df.iloc[test_ixs].drop(columns=["target"])
        y_train = df.iloc[train_ixs]['target']
        x_train = df.iloc[train_ixs].drop(columns=["target"])

        rfc = model
        rfc.fit(x_train, y_train)
        accuracy.append(accuracy_score(y_test, rfc.predict(x_test)))
    return accuracy


def cross_val_test(df, model):
    accuracy = []
    train_last, test_last = 0, 0
    for shift in range(0, 10, 2):
        authors_seen = []
        test_ixs = []
        for ixs in range(len(df)):
            aut = df['targets'][ixs]
            if authors_seen.count(aut) < 2:
                authors_seen += [aut]
                test_ixs += [ixs + shift]
        train_ixs = list(set(range(len(df))) - set(test_ixs))
        if shift != 8:
            y_test = df.iloc[test_ixs]['targets']
            x_test = df.iloc[test_ixs].drop(columns=["targets"])
            y_train = df.iloc[train_ixs]['targets']
            x_train = df.iloc[train_ixs].drop(columns=["targets"])

            rfc = model
            rfc.fit(x_train, y_train)
            accuracy.append(accuracy_score(y_test, rfc.predict(x_test)))
        else:
            train_last = train_ixs
            test_last = test_ixs

    return accuracy, train_last, test_last