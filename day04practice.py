# 7.1

year_list = [1999,2000,2001,2002,2003,2004]

# 7.2
print(year_list[2])

#7.3
print(year_list[-1])

# 7.7
things = ['mozzarella', 'cinderella', 'salmonella']
things.remove('salmonella')
print(things)

#7.8, 7.9,
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()
surprise.reverse()
surprise[-3] = surprise[-3].title()
print(surprise)

#7.10
number_list = [number for number in range(10) if number % 2 == 0 ]
print(number_list)

#7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop','get a mop'),
    ('fope','trun the rope'),
    ('fa','get your ma'),
    ('fudge','call the judge'),
    ('fat','pet the dog'),
    ('fog', 'walk the dog'),
    ("fun", "say we're done"),
]
start2 = 'someone better'

start1_list = list(start1)

a = (f'{start1[0].title()}! {start1[1].title()}! {start1[2].title()}! ')

for i in rhymes:
    print(a,i[0].title())
    print(start2,i[1])

# 8.1
e2f = {'dog': 'chien','cat': 'chat','walrus': 'morse'}
#8.2
print(e2f.get('walrus'))
#8.3
print(list(e2f.items()))
#8.4
print(e2f.get('chien'))
#8.5
print(e2f.keys())
#8.14

titles = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']

movies = list(zip(titles,plots))
print(movies)








































