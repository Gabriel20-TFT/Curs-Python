employee = {
    1: {'name':'Andrei', 'salary':100},
    2: {'name':'Vlad', 'salary':500},
    3: {'name':'Ioana', 'salary':330}
}

employee_modificat = {identification: {'name': emp['name'], 'salary': int(input(f"Care vrei sa fie noul salariu al lui {emp['name']}? "))} for identification, emp in employee.items()}

print(employee_modificat)