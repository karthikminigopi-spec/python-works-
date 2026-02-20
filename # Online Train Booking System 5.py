# Online Train Booking System

class TrainBooking:
    def __init__(self, train_name, source, destination, fare_per_ticket):
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.fare = fare_per_ticket

    def book_ticket(self, passenger_name, tickets):
        total_cost = tickets * self.fare

        # Confirmation Page
        print("\n===== BOOKING CONFIRMATION =====")
        print(f"Passenger Name   : {passenger_name}")
        print(f"Train Name       : {self.train_name}")
        print(f"Route            : {self.source} ➜ {self.destination}")
        print(f"Number of Tickets: {tickets}")
        print(f"Fare per Ticket  : ₹{self.fare}")
        print("--------------------------------")
        print(f"TOTAL BOOKING COST: ₹{total_cost}")
        print("Status           : CONFIRMED ✅")
        print("================================")



train = TrainBooking("Kerala Express", "Kochi", "Delhi", 750)

name = input("Enter passenger name: ")
tickets = int(input("Enter number of tickets: "))

train.book_ticket(name, tickets)
