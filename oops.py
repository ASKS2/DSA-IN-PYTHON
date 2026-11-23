class Movie:
    movie_name = ""
    total_seats = 0
    ticket_price = 0
    booked_seats = 0


    def book_ticket(self, number_of_tickets):
        if self.booked_seats + number_of_tickets <= self.total_seats:
            self.booked_seats += number_of_tickets
            print(f"Successfully booked {number_of_tickets} tickets for {self.movie_name}.")
        else:
            print(f"Booking failed. Not enough available seats for {self.movie_name}.")