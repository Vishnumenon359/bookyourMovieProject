#!/usr/bin/env python3
import sys
import copy

class Movie():
    def __init__(self,rows=0, seats=0):
        self.rows = rows
        self.seats = seats
        self.total_seats = self.rows*self.seats
        self.seat_matrix = [None] * self.rows
        self.total_bookings = 0
        self.current_income = 0

    def compute_price(self, row):
        if (self.total_seats>60 and row <=self.rows//2) or self.total_seats<=60:
            return 10
        else:
            return 8


    def build_seats(self):
        for x in range(self.rows):
            self.seat_matrix[x] = ["S"] * self.seats
        self.reservations = copy.deepcopy(self.seat_matrix)
        return self.seat_matrix

    def show_seats(self):
        #printing the matrix
        print(end=" ")
        print(*range(1,self.seats+1))
        for row in range(self.rows):
            print(row+1, end="")
            for seat in range(self.seats):
                print(self.seat_matrix[row][seat], end = " " )
            print()

    def buy_ticket(self, row, seat, name, gender, age, mobile):
        if self.seat_matrix[row-1][seat-1] == "B":
            return "Seat is already booked by another person, please pick another seat"

        customer_details = {
            "Name": name,
            "Gender": gender,
            "Age": age,
            "Phone No.": mobile
        }
        self.seat_matrix[row-1][seat-1] = "B"
        self.reservations[row-1][seat-1] = customer_details
        self.total_bookings+=1
        self.current_income+=(self.compute_price(row))
        return self.show_booking(row,seat)


    def show_booking(self,row,seat):
        return self.reservations[row-1][seat-1]

    def show_stats(self):
        print(f"Number of Purchased Tickets: {self.total_bookings}")
        pb = round((self.total_bookings/self.total_seats)*100,2)
        print(f"Percentage of Tickets booked: {pb}%")
        print(f"Current Income: ${self.current_income}")
        if self.total_seats<=60:
            print("Total Income: $" +str(self.total_seats*10))
        else:
            front_rows = self.rows//2
            back_rows = self.rows-front_rows
            expected_revenue = front_rows*self.seats*10 + back_rows*self.seats*8
            print("Total Income: $" +str(expected_revenue))



def show_menu(t):
    print("""
    ______________________________________________
    Ticket Booking:

    1. Show the seats
    2. Buy a Ticket
    3. Statistics
    4. Show booked Tickets User Info
    0. Exit
    """)
    answer = input(f'Please make a selection: ')
    if answer == "1":
        if t.rows>0 and t.seats>0:
            t.show_seats()
            show_menu(t)

        rows = int(input("Enter the number of rows: "))
        seats = int(input("Enter the number of seats in each row: "))
        t = Movie(rows,seats)
        t.build_seats()
        t.show_seats()
        show_menu(t)
    elif answer == "2":
        row = int(input("Enter the row number: "))
        seat = int(input("Enter the seat number: "))
        print(f"Ticket Price for row:{row}, seat:{seat} is $"+ str(t.compute_price(row)))
        confirmation = input("Do you want to book the ticket (yes/no): ")
        if "yes" == confirmation.lower():
            name  = input("Enter your Name: ")
            age  = input("Enter your Age: ")
            gender  = input("Enter your Gender: ")
            mobile  = input("Enter your Mobile Number: ")
            t.buy_ticket(row,seat,name,gender,age,mobile)
            print("Booked Successfully")
        show_menu(t)
    elif answer == "3":
        t.show_stats()
        show_menu(t)
    elif answer == "4":
        row = int(input("Enter the row number: "))
        seat = int(input("Enter the seat number: "))
        print(t.show_booking(row, seat))
        show_menu(t)
    elif answer =="0":
        sys.exit()
    else:
        print("Please select a number for the list that is provided.")

def main():
    t=Movie()
    show_menu(t)


if __name__ == "__main__":
    main()
