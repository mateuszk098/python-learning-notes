'''
Use dictionary instead of if-elif-... clause.
'''

season: str = 'Summer'
holiday: str = ''

if season == 'Winter':
    holiday = 'New Year'
elif season == 'Spring':
    holiday = 'Easter'
elif season == 'Summer':
    holiday = 'Corpus Christi'
elif season == 'Autumn':
    holiday = "All Saints' Day"
else:
    holiday = 'Free day'

print(holiday)

# Use of dictionary
holiday_with_dict: str = {'Winter': 'New Year', 'Spring': 'Easter',
                          'Summer': 'Corpus Christi', 'Autumn': "All Saints' Day"}.get(season, 'Free day')
print(holiday_with_dict)
