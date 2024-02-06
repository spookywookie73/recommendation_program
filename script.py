from data import *
from linkedlist import LinkedList

def create_company_linkedlist():
  company_list = LinkedList()
  for company_name in consoles:
    company_list.insert_beginning(company_name)
  return company_list

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

def selection_software():
  company_choice = ""
  console_choice = ""

  while len(company_choice) == 0:
    user_input = str(input("choose a console company's name. type a letter and press enter: ")).lower()

    matching_companys = []
    company_list_head = companys_list.get_head_node()
    while company_list_head is not None:
      if str(company_list_head.get_value()).startswith(user_input):
        matching_companys.append(company_list_head.get_value())
      company_list_head = company_list_head.get_next_node()

    for company in matching_companys:
      print(company.upper())

    if len(matching_companys) == 1:
      select_company = str(input("\nThere is only one company that starts with that letter. Do you want" +
                                 " to look at it.\nPress y for yes or n for no: ")).lower()
      if select_company == "y":
        company_choice = matching_companys[0]
        print("Selected company: " + company_choice.title())
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



selection_software()
