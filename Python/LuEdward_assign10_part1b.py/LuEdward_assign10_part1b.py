valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

try:
    new_pokemon = open('saved_file', 'r')
    alldata = new_pokemon.read()
    pokemon = {}
    for i in alldata.split('\n'):
        names = {}

        types = []
        for j in range(1, len(i.split(','))):
            
            if j == 1:
                names['quantity'] = int(i.split(',')[j])
               
                
            elif j == 2:
                names['fee'] = int(i.split(',')[j])
                
            else:
                types += [i.split(',')[j]]
                names['types'] = types
                
                

        pokemon[i.split(',')[0]] = names
    del pokemon['']
        
except:
    pokemon = {
                         'charmander':{'quantity':3,'fee':100,'types':['fire']},
                         'squirtle':{'quantity':2,'fee':50,'types':['water']},
                         'bulbasaur':{'quantity':5,'fee':25,'types':['grass']},
                         'gyrados':{'quantity':1,'fee':1000,'types':['water','flying']}
                }



print('Welcome to the Pokemon Center!')
while True:
    choice = input('(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit:')
    if choice == 'l':
        print('Name                    Amount Available        Adoption Fee Type(s)')
        for i in sorted(pokemon):
            types = ''
            for j in pokemon[i]['types']:
                types += str.capitalize(j) + ' ' 
            print(format(str.capitalize(i), '<15'), format(pokemon[i]['quantity'], '>24'), format(pokemon[i]['fee'], '>19,.2f'), format(types, '>2'))

    elif choice == 'a':
        name = str.lower(input('Enter name of new pokemon:'))
        name1 = {}
        while True:
            number = int(input('How many of these Pokemon are you adding?'))
           
            if number > 0:
                name1['quantity'] = number
                break

            elif number <= 0:
                print('Invalid, please try again')
                continue

            else:
                print('Not a valid integer, try again')
                continue
        while True:
            fee = int(input('What is the adoption fee for this Pokemon?'))

            if fee > 0:
                name1['fee'] = fee
                break

            elif fee <= 0:
                print('Invalid, please try again')
                continue

            else:
                print('Not a valid integer, try again')
                continue


        print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
        added_type = []
        while True:
            new_type = input('What type of Pokemon is this?')
            if new_type in valid_pokemon_types:
                print('Type', new_type, 'added')
                added_type += [new_type]
            elif new_type == 'end':
                name1['types'] = added_type
                pokemon[name] = name1
                print('Pokemon Added!')
                break
            else:
                print('This is not a valid type, please try again')

    elif choice == 't':
        type = input('Enter Pokemon type:')
        print('Name                    Amount Available        Adoption Fee Type(s)')
        for i in sorted(pokemon):
            types = ''
            if type in pokemon[i]['types']:
                for j in pokemon[i]['types']:
                    types += str.capitalize(j) + ' ' 
                print(format(i, '<15'), format(pokemon[i]['quantity'], '>24'), format(pokemon[i]['fee'], '>19'), format(types, '>2'))

    elif choice == 's':
        search = str.lower(input('Enter a name to search:'))

        if search in pokemon:
            print('We do have this one')
            print('We have', pokemon[search]['quantity'], 'of this one')
            print('It will cost $' + format(pokemon[search]['fee'], ',.2f'), 'to adopt this Pokemon')
            types = ''
            for t in pokemon[search]['types']:
                types += str.capitalize(t) + ' '
            print('Pikachu has the following types:', types)
        else:
            print("We don't have that one")

    elif choice == 'e':
        all_fees = []
        for i in pokemon:
            all_fees.append(pokemon[i]['fee'])
            

        max_fee = max(all_fees)
        min_fee = min(all_fees)
        max_poke = ''
        min_poke = ''
        for i in pokemon:
            if pokemon[i]['fee'] == max_fee:
                max_poke = str.capitalize(i)
            elif pokemon[i]['fee'] == min_fee:
                min_poke = str.capitalize(i)
        
        print('Highest priced Pokemon:', max_poke, '@ $' + format(max_fee, ',.2f'), 'per Pokemon')
        print('Highest priced Pokemon:', min_poke, '@ $' + format(min_fee, ',.2f'), 'per Pokemon')

    elif choice == 'r':
        remove = str.lower(input('Enter name of Pokemon to remove:'))
        del pokemon[remove]
        print('Pokemon removed')
        
    elif choice == 'q':
        print('See you next time!')
        save_method = open('saved_file', 'w')
        names = pokemon.keys()
        for i in sorted(names):
            save_method.write(i +  ',')
            value = list(pokemon[i].values()) 
            for j in range(len(value)-1):
                save_method.write(str(value[j]) + ',')
            save_method.write(','.join(value[2]))
    
            save_method.write('\n')
        save_method.close()
        
        break

