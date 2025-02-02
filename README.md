### AirBnB Clone

# Description
This team project is part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

# Description of the command interpreter:
Create objects and translate it to JSON strings that can be stored, readed, and updated from a file.

# Usage
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

| Command| Example|
| ----- | ---- |
| Run the console | ./console.py |
| Quit the console | (hbnb) quit |
| Display the help for a command | (hbnb) help <command> |
| Create an object (prints its id) | (hbnb) create <class> |
| Show an object | (hbnb) show <class> <id> or (hbnb) <class>.show(<id>) |
| Destroy an object | (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>) |
| Show all objects, or all instances of a class | (hbnb) all or (hbnb) all <class> |
| Update an attribute of an object | (hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") |

# Models

The folder models contains all the classes used in this project.

| File| Description| Attributes|
| ----- | ---- | ---- |
| base_model.py | BaseModel class for all the other classes | id, created_at, updated_at |
| user.py | User class for future user information | email, password, first_name, last_name |
| amenity.py | Amenity class for future amenity information | name |
| city.py | City class for future location information | state_id, name |
| state.py | State class for future location information | name |
| place.py | Place class for future accomodation information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| review.py | Review class for future user/host review information | place_id, user_id, text |

# Examples
**modo no-interactive**

(hbnb) help

Documented commands (type help <topic>):

======================================

EOF  all  create  destroy  help  quit  show  update



**Mode interactive**

**create**:

(hbnb) create User
64be5ef5-0ed1-40ea-a875-c06f999c6d73

**all**:

(hbnb) all
["[User] (a1d3378b-0d7e-439c-8698-2dabba9f91d0) {'id': 'a1d3378b-0d7e-439c-8698-2dabba9f91d0', 'created_at': datetime.datetime(2022, 3, 7, 19, 28, 34, 785476), 'updated_at': datetime.datetime(2022, 3, 7, 19, 28, 34, 785490)}", "[City] (e596a16f-2fca-4f57-822a-d7fddc931489) {'id': 'e596a16f-2fca-4f57-822a-d7fddc931489', 'created_at': datetime.datetime(2022, 3, 7, 19, 31, 10, 105824), 'updated_at': datetime.datetime(2022, 3, 7, 19, 31, 10, 105837)}", "[User] (a75b3922-ff49-4fdb-8f76-7c03e3ed2510) {'id': 'a75b3922-ff49-4fdb-8f76-7c03e3ed2510', 'created_at': datetime.datetime(2022, 3, 7, 19, 35, 37, 288931), 'updated_at': datetime.datetime(2022, 3, 7, 19, 35, 37, 288947)}", "[City] (21a7c366-163a-428c-a0c7-5b1a28458cb3) {'id': '21a7c366-163a-428c-a0c7-5b1a28458cb3', 'created_at': datetime.datetime(2022, 3, 7, 19, 35, 44, 79948), 'updated_at': datetime.datetime(2022, 3, 7, 19, 35, 44, 79963)}", "[User] (1a4fb60d-a7f7-4d6f-a9a1-a381bdc8bd3f) {'id': '1a4fb60d-a7f7-4d6f-a9a1-a381bdc8bd3f', 'created_at': datetime.datetime(2022, 3, 8, 12, 43, 26, 806884), 'updated_at': datetime.datetime(2022, 3, 8, 12, 43, 26, 806896)}", "[User] (64be5ef5-0ed1-40ea-a875-c06f999c6d73) {'id': '64be5ef5-0ed1-40ea-a875-c06f999c6d73', 'created_at': datetime.datetime(2022, 3, 8, 13, 31, 50, 498804), 'updated_at': datetime.datetime(2022, 3, 8, 13, 31, 50, 498820)}"]

# Authors

Hernán Echeverri R <3883@holbertonschool.com>
Andres Felipe Duque <3504@holbertonschool.com