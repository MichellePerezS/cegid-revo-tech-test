from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    @abstractmethod
    def get_charge(self, days_rented):
        pass
    
    def get_frequent_renter_points(self, days_rented):
        return 1
    
class RegularPrice(PriceStrategy):
    def get_charge(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += (days_rented - 2) * 1.5
        return amount
    
class NewReleasePrice(PriceStrategy):
    def get_charge(self, days_rented):
        return days_rented * 3.0
    
    def get_frequent_renter_points(self, days_rented):
        return 2 if days_rented > 1 else 1 

class ChildrensPrice(PriceStrategy):
    def get_charge(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += (days_rented - 3) * 1.5
        return amount
    
# CORE CLASSES

class Movie:
    def __init__(self, title, price_strategy: PriceStrategy):
        self._title = title
        self._price_strategy = price_strategy

    @property
    def title(self):
        return self._title

    def get_charge(self, days_rented):
        return self._price_strategy.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        return self._price_strategy.get_frequent_renter_points(days_rented)

class Rental:
    def __init__(self, movie: Movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def movie(self):
        return self._movie

    @property
    def days_rented(self):
        return self._days_rented

    def get_charge(self):
        return self._movie.get_charge(self._days_rented)

    def get_frequent_renter_points(self):
        return self._movie.get_frequent_renter_points(self._days_rented)
    
#STATEMENT STRATEGIES
class StatementFormatter(ABC):
    @abstractmethod
    def generate(self, customer_name, rentals):
        pass

class TextStatement(StatementFormatter):
    def generate(self, customer_name, rentals):
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental Record for {customer_name}\n"

        for rental in rentals:
            charge = rental.get_charge()
            frequent_renter_points += rental.get_frequent_renter_points()
            result += f"\t{rental.movie.title}\t{charge}\n"
            total_amount += charge

        result += f"Amount owed is {total_amount}\n"
        result += f"You earned {frequent_renter_points} frequent renter points"
        return result

class HtmlStatement(StatementFormatter):
    def generate(self, customer_name, rentals):
        total_amount = sum(r.get_charge() for r in rentals)
        frequent_renter_points = sum(r.get_frequent_renter_points() for r in rentals)
        
        result = f"<h1>Rental Record for <em>{customer_name}</em></h1>\n<ul>\n"
        for rental in rentals:
            result += f"  <li>{rental.movie.title}: {rental.get_charge()}</li>\n"
        result += f"</ul>\n<p>Amount owed is <b>{total_amount}</b></p>\n"
        result += f"<p>You earned <b>{frequent_renter_points}</b> frequent renter points</p>"
        return result
    
#CUSTOMER
class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)

    @property
    def name(self):
        return self._name

    def statement(self, formatter: StatementFormatter = TextStatement()):
        return formatter.generate(self.name, self._rentals)