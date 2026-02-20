#train_booking_system
import datetime
import time 
class BookingSystem:

    def __init__(self):
        self.bookings = []
    def book(self):
        name = input("enter your name :")
        date_str = input("enter booking date (YYYY-MM-DD):")
        
        try:     
            booking_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("invalid date format. please use YYYY-MM-DD.")
            return
        if booking_date < datetime.date.today():
            print("booking date cannot be in the past.")
            return
        self.bookings.append((name, booking_date))
        print(f"booking confirmed for {name} on {booking_date}.") 
        def view_bookings(self):
        if not self.bookings:
            print("no bookings found.")
        else:
            print("current bookings:")
            for name, date in self.bookings:
                print(f"{name} - {date}")
if __name__ == "__main__":
    system = BookingSystem()
    while True:
        print("\n1. Book a ticket")
        print("2. View bookings")
        print("3. Exit")
        choice = input("enter your choice:")
        if choice == "1":
            system.book()
        elif choice == "2":
            system.view_bookings()
        elif choice == "3":
            print("exiting the booking system.")
            break
        else:
            print("invalid choice. please try again.")
        