grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Использую функцию sorted() для сортировки списка по алфавиту
res = sorted(students)
# Использую функции sum(), чтобы найти сумму всех элементов
# и len(), чтобы получить кол-во элементов в списке
avg0 = (sum(grades[0]) / len(grades[0]))
avg1 = (sum(grades[1]) / len(grades[1]))
avg2 = (sum(grades[2]) / len(grades[2]))
avg3 = (sum(grades[3]) / len(grades[3]))
avg4 = (sum(grades[4]) / len(grades[4]))

result = {sorted(students)[0]: avg2,
          sorted(students)[1]: avg1,
          sorted(students)[2]: avg4,
          sorted(students)[3]: avg3,
          sorted(students)[4]: avg0, }
print(result)
