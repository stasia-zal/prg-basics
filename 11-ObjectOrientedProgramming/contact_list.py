from contact import Contact

class Contact_List:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,name,email,telephone):
        contact=Contact(name,email,telephone)
        self.contacts.append(contact)
    def display(self):
        print()
        print("CONTACT LIST")
        print('-'*50)
        for contact in self.contacts:
            print(contact)
        print()