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

def dependance_accuracy_from_data(df, model):
    accuracy_train = []
    accuracy_test = []
    size_of_train = []
    size_of_test = []
    for data in range(1, 5):
        train_temp = []
        test_temp = []
        for shift in range(0, 10, 2):
            authors_seen = []
            train_ixs = []
            for ixs in range(len(df)):
                aut = df['targets'][ixs]
                if authors_seen.count(aut) < data:
                    authors_seen += [aut]
                    if (ixs+shift) < len(df):
                        train_ixs += [ixs + shift]
            test_ixs = list(set(range(len(df))) - set(train_ixs))
            y_test = df.loc[test_ixs]['targets']
            x_test = df.loc[test_ixs].drop(columns=["targets"])
            y_train = df.loc[train_ixs]['targets']
            x_train = df.loc[train_ixs].drop(columns=["targets"])

            rfc = model
            rfc.fit(x_train, y_train)
            test_temp.append(accuracy_score(y_test, rfc.predict(x_test)))
            train_temp.append(accuracy_score(y_train, rfc.predict(x_train)))
        accuracy_train.append(mean(train_temp))
        accuracy_test.append(mean(test_temp))
        size_of_test.append(len(x_test))
        size_of_train.append(len(x_train))
    return accuracy_test, accuracy_train, size_of_test, size_of_train

print(dependance_accuracy_from_data(df, ExtraTreesClassifier()))