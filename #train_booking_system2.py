#train_booking_system
import datetime
import time 
class BookingSystem:
    def __init__(self):
        self.bookings = []
    
    def book(self, name, date):
        booking = {"name": name, "date": date}
        self.bookings.append(booking)
        print(f"Booking confirmed for {name} on {date}.")
    
    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        print("Current Bookings:")
        for booking in self.bookings:
            print(f"{booking['name']} - {booking['date']}")




