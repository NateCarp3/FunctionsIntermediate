x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James' , 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']

}
z = [ {'x':10, 'y':20} ]

x[1][0] = 15

print(x)


students[0]["last_name"] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

def iterateDictionary(l):
    for i in l:
        for q in i:
            print(q + ' - ' +i[q])
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
print(iterateDictionary2("first_name", students))

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in some_dict:
        for q in i:
            print(i[q])
print(print(dojo["locations"]), print(dojo["instructors"]))
print(len(dojo["locations"]),len(dojo["instructors"]))
    
