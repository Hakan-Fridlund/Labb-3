"""
Class Support
represents a support ticket.
Reads a csv file and creates a list of tickets directly.
class method to change status added via ticket number.
class method to show list of objects with status filtering.
suggested features:
* add a method that checks if a ticket is still active.
• Save simple information from objets as json. Do not save objects themselves.
• Implement the class as a dataclass and compare the versions.
• Use a proterty to control which values a attribute can contain.
"""

import csv
support_tickets = []

def load_csv():
    """reads csv file and makes each row into a support_ticket"""
    with open("supportarenden.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) # hoppar över första rubrikraden
        for row in reader:
            ticket = row[0]
            customer = row[1]
            category = row[2]
            priority = row[3]
            status = row[4]
            support_ticket = Support(ticket, customer, category, priority, status)
            support_tickets.append(support_ticket)


class Support:
    """support class, represents a support ticket"""
    def __init__(self, ticket: str, customer: str, category: str, priority: str, status: str):
        self.ticket = ticket
        self.customer = customer
        self.category = category
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Ärende-id: {self.ticket},kund: {self.customer}, kategori: {self.category}, prioritet: {self.priority}, status: {self.status}\n"

    def __repr__(self):
        return f"Ärende-id: {self.ticket}, kund: {self.customer}, kategori: {self.category}, prioritet: {self.priority}, status: {self.status}\n"

    @classmethod #lets us use this class method without creating a object of the class
    def update_status(self, new_status: str, input_from_user):
        """ updates the status varible if found"""
        for support_ticket in support_tickets:
            if support_ticket.ticket == input_from_user:
                print(support_ticket)
                support_ticket.status = new_status
                return support_ticket
        print("Ärende hittas ej!")
        return None

    @classmethod #lets us use this class method without creating a object of the class
    def show_status(self, input_from_user):
        """ prints object in loop if status is correct"""
        found = False
        for support_ticket in support_tickets:
            if support_ticket.status == input_from_user:
                print(support_ticket)
                found = True
        if not found:
            print(f"Inga ärenden med status: {input_from_user}")



load_csv()
print(support_tickets)
ticket_number = input("Vilket ärendenummer vill du ändra?")
new_status = input("Vad är ärendets nya status?")
print(Support.update_status(new_status, ticket_number))
status = input("Välj status för att visa alla ärenden:")
Support.show_status(status)
