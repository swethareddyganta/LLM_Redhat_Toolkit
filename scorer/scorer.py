# scorer/scorer.py
def compute_risk(regex_flag, clf_label, clf_score):
    if regex_flag or (clf_label in ["dangerous", "harmful"] and clf_score > 0.7):
        return "High"
    elif clf_label == "sensitive":
        return "Medium"
    return "Low"