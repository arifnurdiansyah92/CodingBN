class Ticket:
    """
    The base class for a cinema ticket.
    Encapsulates the core details of a ticket.
    """
    def __init__(self, movie_title, seat_number, price=12.00):
        self.movie_title = movie_title
        self.base_price = price
        # Encapsulation: The seat number is private and cannot be changed.
        self.__seat_number = seat_number

    def get_seat_number(self):
        """A public method to safely access the private seat number."""
        return self.__seat_number

    def get_final_price(self):
        """Polymorphism: This is the base method for getting the price."""
        return self.base_price

    def print_ticket(self):
        """Polymorphism: This is the base method for printing ticket details."""
        print("--- Cinema Ticket ---")
        print(f"Movie: {self.movie_title}")
        print(f"Seat: {self.get_seat_number()}")

class StandardTicket(Ticket):
    """
    Inheritance: A standard ticket. It inherits all functionality
    from the base Ticket class without modification.
    """
    pass

class VIPTicket(Ticket):
    """
    Inheritance: A special VIP ticket with extra features.
    """
    def __init__(self, movie_title, seat_number, price=12.00, vip_charge=7.50):
        # Call the parent's constructor
        super().__init__(movie_title, seat_number, price)
        self.vip_charge = vip_charge
        self.complimentary_drink = "Sparkling Water"

    def get_final_price(self):
        """Polymorphism: Overrides the parent method to add the VIP charge."""
        return self.base_price + self.vip_charge

    def print_ticket(self):
        """
        Polymorphism: Overrides the parent method to add VIP-specific details.
        """
        # Call the parent's method first to print the common info
        super().print_ticket()
        print("--- VIP ACCESS ---")
        print(f"Includes: {self.complimentary_drink}")
        print(f"Final Price: ${self.get_final_price():.2f}")

class Cinema:
    """A manager class to hold and manage tickets sold."""
    def __init__(self, name):
        self.name = name
        self.tickets_sold = []

    def sell_ticket(self, movie, seat, ticket_type):
        """Creates the correct ticket object and adds it to the list."""
        ticket = None
        if ticket_type.lower() == 'standard':
            ticket = StandardTicket(movie, seat)
        elif ticket_type.lower() == 'vip':
            ticket = VIPTicket(movie, seat)
        
        if ticket:
            self.tickets_sold.append(ticket)
            print(f"\nSuccessfully sold a {ticket_type} ticket for '{movie}'.")
            ticket.print_ticket()
        else:
            print("Error: Invalid ticket type specified.")

    def view_all_tickets(self):
        """Displays details for all tickets sold."""
        print(f"\n--- All Tickets Sold at {self.name} ---")
        if not self.tickets_sold:
            print("No tickets sold yet.")
        else:
            for ticket in self.tickets_sold:
                ticket.print_ticket()
                print("-" * 20)
        print("--------------------------------" + "-" * len(self.name))

def main():
    """The main function to run the interactive program."""
    my_cinema = Cinema("OOP Megaplex")

    while True:
        print("\nCinema Box Office")
        print("1. Sell Standard Ticket")
        print("2. Sell VIP Ticket")
        print("3. View All Tickets Sold")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice in ['1', '2']:
            movie = input("Enter movie title: ")
            seat = input("Enter seat number (e.g., F7): ")
            if choice == '1':
                my_cinema.sell_ticket(movie, seat, 'standard')
            else:
                my_cinema.sell_ticket(movie, seat, 'vip')
        elif choice == '3':
            my_cinema.view_all_tickets()
        elif choice == '4':
            print("Closing system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

main()