__author__ = 'akaash'
# A simple to do program
import os

items = []

# Adds an item to your list
def add_todo(item):
    items.append(item)
    print item + " has been added"

# Views the items in your list
def view_list(list_contents):
    for item in list_contents:
        print item

# Removes an item from your list
def remove_todo(item):
    confirm = input("Are you sure you want to remove the following task: %s? Press 1 to do so. " % item)
    if confirm == 1:
        items.remove(item)
        "That item has been removed from your list"
    else:
        pass


def save():
    desktop = os.path.expanduser("~/Desktop/Todo.txt")
    saved = open(desktop, 'a')
    counter = 1
    for item in items:
        saved.write('%i. %s \n' % (counter, item))
        counter += 1

add_todo("Make a business")
add_todo("??")
add_todo("Profit")

save()
