'''
Ali Mohammed

'''

def getLetterGrade (score):
    score = round(score)
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'
    
score=int(input("Enter a grade from 0 to 100: ")) 
print ('Your grade is',getLetterGrade(score))