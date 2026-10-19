"""
Class Support
represents support tickets.
Reads a csv file
added features:
Låt användaren ändra status på en instans

Programmet ska:
1. Innehålla klassen som ni har utformat.
2. Öppna och läsa CSV-filen.
3. Skapa en instans av klassen för varje rad.
4. Lagra instanserna i en lista eller annan lämplig samling.
5. Använda klassens metod.
6. Visa information från de skapade instanserna.
"""

import csv
support_tickets = []

def load_csv():
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

    @classmethod
    def update_status(self, new_status: str, input_from_user):
        for support_ticket in support_tickets:
            if support_ticket.ticket == input_from_user:
                print(support_ticket)
                support_ticket.status = new_status
                return support_ticket
        print("Ärende hittas ej!")
        return None
            




load_csv()
print(support_tickets)
ticket_number = input("Vilket ärendenummer vill du ändra?")
new_status = input("Vad är ärendets nya status?")
print(Support.update_status(new_status, ticket_number))

