subjects = ['Matematicas', 'Fisica', 'Quimica', 'Programacion', 'Ingles']
scores = [ ]
for subject in subjects:
    score = input('Que nota has sacado en '+ subject + "? ")
    scores.append(score)
for i in range(len(subjects)):
    print('En ' + subjects[i]+ ' su calificacion es '+ scores[1])



