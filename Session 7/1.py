employees = ['Michal', 'Harry', 'Susan', 'Dan', 'Christen']
emails = ['michal@comp.com', 'harryf@comp.com', 'susan@comp.com', 'dan2@comp.com', 'chris@comp.com']

employees_details = {}

for i in range(len(employees)):
    employees_details[employees[i]] = emails[i]

print(employees_details)

# print(employees)
# print(emails)
#
# for employee in employees_details.items():
#     print(f"{employee[0]}: {employee[1]}")