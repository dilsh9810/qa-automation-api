def getgrades(score):
    if score >= 70 and score < 100:
        return "Excellent"
    
    if score >= 60 and score < 69:
        return "Good"

    if score >= 50 and score < 59:
        return "Normal"

    if score < 40:
        return "Fail" 
