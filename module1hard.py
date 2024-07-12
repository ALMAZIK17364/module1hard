grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #Оценки
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Имена
students = sorted(list(students))
averageScore = {}

for i in range(5):

    averageScore[students[i]] = grades[i]

print(averageScore)
