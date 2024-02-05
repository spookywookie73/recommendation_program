from data import *
from linkedlist import LinkedList

def create_company_linkedlist():
  company_list = LinkedList()
  for company_name in company:
    company_list.insert_beginning(company_name)
  return company_list

def create_console_linkedlist():
  console_list = LinkedList()
  for company_name in company:
    console_sublist = LinkedList()
    for console in consoles:
      if console[0] == company_name:
        console_sublist.insert_beginning(console)
    console_list.insert_beginning(console_sublist)
  return console_list

def create_games_linkedlist():
  games_list = LinkedList()
  for console in consoles:
    games_sublist = LinkedList()
    for game in games:
      if game[0] == console[1]:
        games_sublist.insert_beginning(game)
    games_list.insert_beginning(games_sublist)
  return games_list

companys_list = create_company_linkedlist()
consoles_list = create_console_linkedlist()
games_list = create_games_linkedlist()

def selection_software():
  company_choice = ""

  while len(company_choice) == 0:
    user_input = str(input("choose a console company's name. type a letter and press enter: ")).lower()

    matching_types = []
    company_list_head = companys_list.get_head_node()
    while company_list_head is not None:
      if str(company_list_head.get_value()).startswith(user_input):
        matching_types.append(company_list_head.get_value())
      company_list_head = company_list_head.get_next_node()

    for company in matching_types:
      print(company)

    if len(matching_types) == 1:
      select_company = str(input("\nThere is only one company that starts with that letter. Do you want" +
                                 " to look at it.\nPress y for yes or n for no: ")).lower()
      if select_company == "y":
        company_choice = matching_types[0]
        print("Selected company: " + company_choice)
        console_list_head = consoles_list.get_head_node()

        while console_list_head.get_next_node() is not None:
          sublist_head = console_list_head.get_value().get_head_node()
          
          if sublist_head.get_value()[0] == company_choice:
            while sublist_head.get_next_node() is not None:
              print("Console name: " + sublist_head.get_value()[1])
              sublist_head = sublist_head.get_next_node()
          console_list_head = console_list_head.get_next_node()

selection_software()
