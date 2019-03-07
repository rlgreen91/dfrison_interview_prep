Welcome to our first interview challenge!  As part of your mock interview, you'll be working on a coding exercise related to recommendation systems.  This exercise consists of 2 scenarios, easy and hard - the hard scenario will build on top of the work completed for the easy scenario.

You are limited to 45 minutes for this coding exercise.  If you're not able to complete both scenarios, that's ok!  We would prefer that you prioritize well-written, working code for only the easy scenario over messy, broken code for both scenarios.  

Easy Scenario:
  In this repo is a directory titled `sample_data`, which contains 5 CSV files describing information about restaurants.  Your coworkers will be creating a recommendation system for restaurants, but first they need the data.  

  Your job is to import the data in the CSV files into a database.  By the time you complete this scenario, you should be able to run the script titled `import_data.py` that will get the data stored in the CSVs and insert it into a database containing a table `Restaurants`.

  The CSVs follow the format listed below.  Notice that each restaurant is linked to a place ID - the import script is already set up to use the place ID as the primary key for the table.

  | File name 				 | Instances | Attributes 		  		|
  | chefmozaccepts.csv | 1314			 | placeID, payment			|
	|	chefmozcuisine.csv | 916			 | placeID, cuisine 		|
  | chefmozhours4.csv  | 2339			 | placeID, hours, days |
	| chefmozparking.csv | 702			 | placeID, parking_lot |
	| geoplaces2.csv 		 | 130			 | placeID, latitude,
	|										 |					 | longitude, 
	|										 |					 | the_geom_meter, name,
	|										 |					 | address, city, state,
	|										 |						 country, fax, zip,
	|										 |						 alcohol, smoking_area,
	|										 |						 dress_code,
	|										 |						 accessibility, price,
	|										 |						 url, ambience,
	|										 |						 franchise, area,
	|										 |						 other_services

	Hint: The recommendation system will only compare restaurants based on cuisine, payment methods, and parking.  Whatever else you want to store is up to you.


 Hard Scenario:
 	So, it turns out that the coworker that's creating the recommendation system is, well, you.  Using the database you created in the previous scenario, create a recommendation system that will suggest up to 5 restaurants based on the user data provided below.

 	| Person 	 | Preferred Payment Method | Preferred Cuisine | Transportation Options
 	| Monica 	 | Cash 										| Mexican						| Owns Car
 	| D'Angelo | VISA 										|	Burgers						| Bus
 	| Joe			 | bank_debit_cards 				| Seafood						| Walking

