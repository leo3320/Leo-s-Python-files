
# make a list of things to do
to_do_list = []

def show_help():
    # instructions on how to use the app
    print("What would be our next appointment?")
    print("""
Enter 'DONE' to stop adding appointments.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
# print out the list
    print("Here's your list:")

    for item in to_do_list:
      print(item)

def add_to_list(new_item):
    to_do_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(to_do_list)))

show_help()

while True:
    
    new_item = input("> ")

    if new_item == 'DONE':
      break
    elif new_item == 'HELP':
      show_help()
      continue
    elif new_item == 'SHOW':
       show_list()
       continue
    add_to_list(new_item)

show_list()
