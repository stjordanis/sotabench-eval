import numpy as np

def top_k_accuracy_score(y_true, y_pred, k=5, normalize=True):
    """Top k Accuracy classification score.
    """
    assert(y_true.shape == 1) # should be 1D, each index is obs true label

    num_obs, num_labels = y_pred.shape

    idx = num_labels - k - 1
    counter = 0
    argsorted = np.argsort(y_pred, axis=1)

    for i in range(num_obs):
        if y_true[i] in argsorted[i, idx+1:]:
            counter += 1
    if normalize:
        return counter / num_obs
    else:
        return counter