#online_train_ticket_booking_system

class Train:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = [100]

    def show_available(self):
        available = self.total_seats - len(self.booked_seats)
        print(f"\nAvailable seats: {available}/{self.total_seats}")
        print("Booked seats:", self.booked_seats if self.booked_seats else "None")

    def book_seat(self, seat_no):
        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number.")
        elif seat_no in self.booked_seats:
            print("Seat already booked.")
        else:
            self.booked_seats.append(seat_no)
            print(f"Seat {seat_no} booked successfully
            total cost = 135.")

    def cancel_seat(self, seat_no):
        if seat_no in self.booked_seats:
            self.booked_seats.remove(seat_no)
            print(f"Seat {seat_no} cancelled successfully.")
        else:
            print("Seat not booked yet.")

train = Train(100)   

while True:
    print("\n Train Booking Menu ")
    print("1. Show Available Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        train.show_available()

    elif choice == "2":
        try:
            seat = int(input("Enter seat number to book: "))
            train.book_seat(seat)
        except ValueError:
            print("Enter a valid number.")

    elif choice == "3":
        try:
            seat = int(input("Enter seat number to cancel: "))
            train.cancel_seat(seat)
        except ValueError:
            print("Enter a valid number.")

    elif choice == "4":
        print("Thank you for using Train Booking System.")
        break

    else:
        print("Invalid choice. Try again.")
