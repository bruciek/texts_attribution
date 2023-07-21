# офигеть какая важная функция
def get_only_doc(dataset):
    only_doc = []
    for element in dataset["books"]:
        only_doc.append(Doc(element))
    return only_doc
