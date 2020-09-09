def latest(scores):
    return scores[len(scores)-1]
    pass


def personal_best(scores):
    scores.sort(reverse = True)
    return scores[0]



def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[:3]

