# Exercise #1

from datetime import datetime, date
import random, re

print ('Exercise #1 :')
def get_days_from_today(user_date):
    user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
    today = date.today()
    qty_days = today - user_date
    print (f'User date: {user_date}', f'Today: {today}', f'Qty days between them: {qty_days.days}', sep='\n')
    return qty_days.days

user_date = '2025-09-14'

get_days_from_today(user_date)

# Exercise #2

print('-'*30, 'Exercise #2 :', sep='\n')
def get_numbers_ticket(min, max, quantity):
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int) and min >= 1 and min < max <= 1000 and quantity <= max - min:
         ticket = set()
         while len(ticket) < quantity:
             number = random.randrange(min, max, 1)
             ticket.add(number)
         ticket = list(ticket)
         ticket.sort()
         print("Ваші лотерейні числа:", ticket)
         return ticket
    else:
        ticket = []
        print ("Ваші лотерейні числа:", ticket)
        return ticket
   
get_numbers_ticket(2, 4, 2)

# Exercise #3

print('-'*30, 'Exercise #3 :', sep='\n')

phone_number = "    +38(050)123-32-34"

def normalize_phone(phone_number):
    pattern = r'\D'
    repl = ""
    modified_number = re.sub(pattern, repl, phone_number)
    if modified_number.startswith('380'):
        modified_number = '+' + modified_number
    else:
        modified_number = '+380' + modified_number
    modified_number = re.sub(r"(\d{2})(\d{3})(\d{3})(\d{4})", r"\1 (\2) \3-\4", modified_number)

    print (modified_number)

    return modified_number

normalize_phone(phone_number)
