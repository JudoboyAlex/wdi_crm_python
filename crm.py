from contact import Contact

class CRM:

  def main_menu(self):
  
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)
  
  def print_main_menu(self):

      print('[1] Add a new contact')
      print('[2] Modify an existing contact')
      print('[3] Delete a contact')
      print('[4] Display all the contacts')
      print('[5] Search by attribute')
      print('[6] Exit')
      print('Enter a number: ')
  
  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      quit()
  
  def add_new_contact(self):
     # get all the required info from our user:
    print('Enter First Name: ')
    first_name = input()

    print('Enter Last Name: ')
    last_name = input()

    print('Enter Email Address: ')
    email = input()

    print('Enter a Note: ')
    note = input()

    # call the appropriate method from the contact class (remember we imported it?):
    Contact.create(first_name, last_name, email, note)
  
  def modify_existing_contact(self):

    print("Eneter the ID of the contact that you want to modify")  
    id = int(input())
    contact = Contact.find(id)
    print("what do you want to modify?")
    attribute = input()
    print("what is the value that you want to change to?")
    value = input()
    print(contact.update(attribute, value))

  def delete_contact(self):
     print("Enter the ID of the contact that you want to delete")
     contact_id = int(input())
     contact = Contact.find(contact_id)
     contact.delete()

  def display_all_contacts(self):
     
      print(Contact.all())

  def search_by_attribute(self):
      print("Input the attribute that you want to search by")
      attribute = input()
      print("Input the value for that attribute")
      value = input()
      print(Contact.find_by(attribute, value))



a_crm_app = CRM()
a_crm_app.main_menu()