""" Given the name and grades for each student in a class of N students, store them in a nested list and print the names(s) of any students (s) having the second lowest grade. 
Note: if there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line"""

if __name__ == "__main__":
    data = [] # Almacenar data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score]) # Creo array de name y scores
    
    data_grades = [sub_array[1] for sub_array in data] # Creo subarray de los score de data.
    data_grades_sorted = sorted(set(data_grades)) #Creo un set con los data_grades para que no se repita el valor y luego ordeno los valores en orden menor a mayor.
    second_lowest = data_grades_sorted[1]
    name_second_lowest = [name for name, grade in data if grade == second_lowest] # Creo un array con los nombres que coincidan el second_lowest con grade de data.
    name_second_lowest.sort() #ordeno los nombres alfabeticamente

    for name in name_second_lowest:
        print(name)

