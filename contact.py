from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f"{self.first_name} {self.last_name}"

db.connect()
db.create_tables([Contact])

# class Contact:

#   contacts =[]
#   next_id = 1

  # def __init__(self, first_name, last_name, email, note):
  #   """This method should initialize the contact's attributes"""
  #   self.first_name = first_name
  #   self.last_name = last_name
  #   self.email = email
  #   self.note = note

  #   self.id = Contact.next_id
  #   Contact.next_id += 1

  # def __repr__(self):
  #   return f"{self.first_name},{self.last_name},{self.email},{self.note},{self.id}"

  # @classmethod
  # def create(cls, first_name, last_name, email, note):
  #   """This method should call the initializer,
  #   store the newly created contact, and then return it
  #   """
  #   new_contact = Contact(first_name, last_name, email, note)
  #   cls.contacts.append(new_contact)
  #   return new_contact

  # @classmethod
  # def all(cls):
  #   """This method should return all of the existing contacts"""
  #   return cls.contacts

  # @classmethod
  # def find(cls, id):
  #   """ This method should accept an id as an argument
  #   and return the contact who has that id
  #   """
  #   for contact in cls.contacts:
  #     if contact.id == id:
  #       return contact
        
  # def update(self, attribute, new_value):
  #   """ This method should allow you to specify
  #   1. which of the contact's attributes you want to update
  #   2. the new value for that attribute
  #   and then make the appropriate change to the contact
  #   """
  #   return setattr(self, attribute, new_value)
    
  # @classmethod
  # def find_by(cls,key, value):
  #   """This method should work similarly to the find method above
  #   but it should allow you to search for a contact using attributes other than id
  #   by specifying both the name of the attribute and the value
  #   eg. searching for 'first_name', 'Betty' should return the first contact named Betty
  #   """
  #   for contact in cls.contacts:
  #     if getattr(contact, key) == value:
  #       return contact

  # @classmethod
  # def delete_all(cls):
  #   """This method should delete all of the contacts"""
  #   return cls.contacts.clear()

  # def delete(self):
  #   """This method should delete the contact
  #   HINT: Check the Array class docs for built-in methods that might be useful here
  #   """
  #   Contact.contacts.remove(self)
  #   return Contact.contacts
  # Feel free to add other methods here, if you need them.

# contact = Contact('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Zero', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)
# print(Contact.all())
# print(Contact.find(2))
# contact1.update("last_name", "Yang")
# print(Contact.all())
# print(Contact.find_by("first_name", "Betty"))
# print(contact1.full_name())
# print(contact2.delete())
# print(Contact.all())
# Contact.delete_all()
# print(Contact.all())