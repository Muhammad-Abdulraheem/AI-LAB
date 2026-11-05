def rule(height):
    if rule == True:
        if height >= 5:
            return "review"
        else:
            return "hold"
def rule_citizenship(citizenship):
    if citizenship == "Local":
        return "review"
    else:
        return "hold"
def probability_based(probability): 
    if probability >= 0.70:
        return "Review"
    else:
        return "Hold" 
def rule_based(score, documents_complete, height, citizenship):
    if (documents_complete and score >= 70 and rule(height) == "review" and 
        rule_citizenship(citizenship) == "review"):
        return "Review"
    else:
        return "Hold"
print(rule)
print(rule_based)