user_weight = float(input('Weight: '))
kg_lbs = input('kg(k) or lbs(l)')

if kg_lbs.lower() == 'k':
    lbs = user_weight * 2.205
    print(f'You are {lbs} pounds')

if kg_lbs.lower() == 'l':
    kg = user_weight / 2.205
    print(f'You are {kg} kilograms')
