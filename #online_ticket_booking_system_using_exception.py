#online_ticket_booking_system_using_exception_handling.property

TOTAL_SEATS = 100

try:
    print("Total seats available:", TOTAL_SEATS)

    # input tickets
    tickets_input = input("Enter number of tickets required: ")
    if not tickets_input.isdigit():
        raise ValueError("Tickets must be a numeric value!")

    tickets = int(tickets_input)

    # tickets must be > 0
    if tickets <= 0:
        raise ArithmeticError("Number of tickets must be greater than zero!")

    # input price
    price_input = input("Enter ticket price per passenger: ")
    try:
        price = float(price_input)
    except:
        raise ValueError("Ticket price must be numeric!")

    # price must be > 0
    if price <= 0:
        raise RuntimeError("Ticket price must be greater than zero!")

    # check availability
    if tickets > TOTAL_SEATS:
        raise Exception("Not enough seats available!")

    # calculate cost
    total_cost = tickets * price

    # cost limit check
    if total_cost > 20000:
        raise Exception("Total booking cost exceeds ₹20000 limit!")

    # remaining seats
    remaining = TOTAL_SEATS - tickets

    # confirmation message
    print("\n===== BOOKING CONFIRMED =====")
    print("Tickets booked:", tickets)
    print("Price per ticket:", price)
    print("Total booking cost: ₹", total_cost)
    print("Remaining seats:", remaining)
    print("Thank you for booking with us!")

# non-numeric errors
except ValueError as e:
    print("Input Error:", e)

# tickets <= 0
except ArithmeticError as e:
    print("Arithmetic Error:", e)

# price <= 0
except RuntimeError as e:
    print("Runtime Error:", e)

# other booking errors
except Exception as e:
    print("Booking Error:", e)
