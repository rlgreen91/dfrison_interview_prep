import sqlite3

# Database structure
sqlite_file = 'restaurant_recommendation.sqlite'
table_name = 'restaurants'
new_field = 'place_ID'
field_type = 'INTEGER'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating the restaurants table with the place_ID column as its primary key
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()