from data import *
from linkedlist import LinkedList

# create a linkedlist of the console data
def create_company_linkedlist():
  company_list = LinkedList()
  for company_name in consoles:
    company_list.insert_beginning(company_name)
  return company_list

# create a linkedlist of the games data, linking it to the console data
def create_console_linkedlist():
  console_list = LinkedList()
  for company_name in consoles:
    console_sublist = LinkedList()
    for console in games:
      if console[0] == company_name:
        console_sublist.insert_beginning(console)
    console_list.insert_beginning(console_sublist)
  return console_list


companys_list = create_company_linkedlist()
consoles_list = create_console_linkedlist()
company_choice = ""


def intro():
  print("\n          Welcome to Retro Game Index.")
  print("------------------------------------------------")
  print("Choose a company and console to see a collection")
  print("     of great games to try on that system.")
  print("------------------------------------------------")
  print("        The companies to search for are:")
  print("  Atari - Mattel - NEC - Nintendo - Sega - SNK")
  print("------------------------------------------------")
  print("                Happy viewing\n\n")

  start = input("Type s to start and press enter: ")
  if start == "s":
    selection_software()
  else:
    intro()
  

def selection_software():
  global company_choice

  while len(company_choice) == 0:
    user_input = str(input("\nChoose a console company's name. Type the first letter and press enter: ")).lower()

    matching_companys = []
    choosing_company = []
    company_list_head = companys_list.get_head_node()
    # loop through the companys to find any that start with the letter you input
    # if found, append the company to the matching_companys list
    while company_list_head is not None:
      if str(company_list_head.get_value()).startswith(user_input):
        matching_companys.append(company_list_head.get_value())
      company_list_head = company_list_head.get_next_node()

    for company in matching_companys:
      choosing_company.append(company)
      print(company.upper())

    # if one company is found. ask if you want the games displayed
    if len(matching_companys) == 1:
      select_company = str(input("\nThere is only one company that starts with that letter. Do you want" +
                                 " to look at it.\nPress y for yes or n for no: ")).lower()
      if select_company == "y":
        company_choice = matching_companys[0]
        display_games()
      elif select_company == "n":
        choice = input("Do you want to search for another company. press Y for yes or n for no: ").lower()
        if choice == "y":
          selection_software()
        elif choice == "n":
          print("\nThankyou for using this software. Goodbye.")
          exit()
    # if more than one company is found. ask for more input then display the games
    elif len(matching_companys) > 1:
      choose_company = str(input("Choose a company. Type the first two letters and press enter: ")).lower()
      for company in choosing_company:
        if str(company).startswith(choose_company):
          company_choice = company
          display_games()

# function to loop through linkedlist and display chosen companys games
def display_games():
  print("\nSelected company: " + company_choice.title() + "\n")
  console_list_head = consoles_list.get_head_node()
        
  while console_list_head.get_next_node() is not None:
    sublist_head = console_list_head.get_value().get_head_node()
          
    if sublist_head.get_value()[0] == company_choice:
      while sublist_head.get_next_node() is not None:
        print("Console name: " + sublist_head.get_value()[1])
        print("Game name: " + sublist_head.get_value()[2])
        print("Genre: " + sublist_head.get_value()[3])
        print("\n")
        sublist_head = sublist_head.get_next_node()
    console_list_head = console_list_head.get_next_node()
  replay()
  
def replay():
  global company_choice
  continue_choice = str(input("Do you want to look at other consoles?\
  Press y for yes or press any other key to quit: ")).lower()
  if continue_choice == "y":
    company_choice = ""
  

intro()
