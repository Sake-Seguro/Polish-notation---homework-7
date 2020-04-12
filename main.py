
# We are going to realize so-called Polish notation

print('\nFor two positive integers you could play with the Polish notation.')

your_input = list(input('\n\nEnter your Polish notation: one arythmetic symbol followed by two positive integers separated with spaces to start the game,\n e.g. + 2 9: ').split(' '))

operation_sym = your_input[0]

number_1 = int(your_input[1])
number_2 = int(your_input[2])

operation_symbols = ['+', '-', '*', '/']

result = 0

assert operation_sym in operation_symbols, 'Incorrect symbol of arithmetic operations. Please, check and try again.'

assert number_1 >= 0 and number_2 >= 0, 'The number you entered is not a positive integer, Please, check and try again.'

try:

  if operation_sym == '+':
    result = number_1 + number_2
  elif operation_sym == '-':
    result = number_1 - number_2
  elif operation_sym == '*':
    result = number_1 * number_2
  elif operation_sym == '/':
    result = number_1 / number_2

  print(f'\nThe result of your Polish notation is {result}.')


except ZeroDivisionError:
  print('\nIt is impossible to divide by 0.')
except ValueError:
  print('\nThe meanings you tried to use are incorrect.')
except UnboundLocalError:
  print('\nIt seems you tried to apply some incorrect command.')
except Exception as e:
  print(f'\nYour error is {e}.')

else:
  print('\nWe did this exercise in a good manner :).')






###### Some additions to our shelves - the second task - function - n ########





documents = [
  {"type" : "passport", "number" : "2207 876234", "name" : "Vasilliy Gupkin"},
  {"type" : "invoice", "number" : "11-2", "name" : "Gennadiy Pokemonov"},
  {"type" : "insurance", "number" : "10006", "name" : "Aristarch Pavlov"}
]

directories = {
  '1' : ['2207 876234', '11-2', '5455 028765'],
  '2' : ['10006', '5400 028765', '5455 002299'],
  '3' : []
}


def people(numbers):
  for doc_number in documents:
    if doc_number['number'] == numbers:
      print(f'\nThe document you entered belongs to {doc_number["name"]}.')
      break

  else:
    print('\nThe number of the document you entered does not exist in our system.')


def people_list():
  for person in documents:
    print('\n',person['type'],'-', person['number'],'-', person['name'])
    
def shelves_attributes():
  docs_shelves = 0
  input_number = input('Enter the number of the document you need: ')
  for shelf in directories:
    docs_shelves  += 1
    if input_number in directories.get(shelf):
      print('\nThis document is on the shelf', shelf)
      break
    elif docs_shelves == len(directories):
      print('\nThe document with the number you entered does not exist in our system.')
      break

def adding_docs(ndoc_type, ndoc_number, ndoc_name, ndoc_shelf):
  if int(ndoc_shelf) == 1 or int(ndoc_shelf) == 2 or int(ndoc_shelf) == 3:
    documents.append({"type" : ndoc_type, "number" : ndoc_number, "name" : ndoc_name})
    directories[ndoc_shelf].append(ndoc_shelf)
    print('\nYour document has been added to shelf', ndoc_shelf,'.')
  else:
    print('\nThe shelf you entered does not exist within our catalogue. Your entrance is invalid. Please, check the shelf you need.')

def some_name():
  input_number = input('\nEnter the number of the document you would like to check the owner: ')
  for doc in documents:
    if doc['number'] == input_number:
      try:
        print(f'\nThe document you entered belongs to {doc["name"]}.')
      except KeyError:
        print(f'\nUnfortunately, the owner of this document {input_number} is not found. The attribute does not exist.')
    else:
      print(f'\nThe document with attribute {input_number} you entered is not found in our system.')
      break
      

def main():
  
  while True:
    print('\n\n\n Welcome to our working electronic catalogue! \n\n Please, enter one of the following commands to start your work with the system: \n\n p - command for asking a number of a document and printing the name of its owner; \n l - command for printing all documents within the system; \n s - command to print out the shelf of a document by its number; \n a - command for adding a new document to our working catalogue and to the list of shelves; \n n - command for printing the name of the owner of the document by its number with checking the presence of the attribute; \n q - command for finishing your work within the catalogue. \n \n')
    
    user_input = input('Enter your command to start your working with the catalogue: ')
    if user_input == 'p':
      people(input('\nEnter the number of the document you need: '))
      break
    elif user_input == 'l':
      people_list()
      break
    elif user_input == 's':
      shelves_attributes()
      break
    elif user_input == 'a':
      adding_docs(input('\nEnter the type of the document you wish to add: '), input('\nEnter the number of the document being added: '), input('\nEnter the name of this document: '), input('\nEnter the number of the shelf where you would like to place the document (e.g. 10, 3014):'))
      break  
    elif user_input == 'n':
      some_name()
      break
    elif user_input == 'q':
      print('Thank you for working with us! The session is over.')
      break
    else:
      print('\nYou have enetered a wrong command. Please, check its correctness and try again.')
      break

main()











