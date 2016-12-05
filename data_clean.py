
def convert_to_para(X_train):
    for i in range(0,X_train.shape[0]):
        X_train['review'][i] = ' '.join(str(r) for v in X_train['review'][i] for r in v)
    return X_train
