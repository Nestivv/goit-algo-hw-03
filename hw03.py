# Exercise #1

from datetime import datetime, date
import random, re

print ('Exercise #1 :')
def get_days_from_today(user_date):
    try:
        if not isinstance(user_date, str):
            print('user_date must be a string')
            return None
        user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
        today = date.today()
        qty_days = today - user_date
        print (f'User date: {user_date}', f'Today: {today}', f'Qty days between them: {qty_days.days}', sep='\n')
        return qty_days.days
    except ValueError:
        print('Invalid date, please use YYYY-MM-DD.')
        return None

user_date = '2025-10-14'

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
   
get_numbers_ticket(1, 20, 5)

# Exercise #3

print('-'*30, 'Exercise #3 :', sep='\n')

raw_number = "38050-111-22-22"

def normalize_phone(raw_number):
    pattern = r'\D'
    repl = ""
    modified_number = re.sub(pattern, repl, raw_number)
    if modified_number.startswith('380'):
        modified_number = '+' + modified_number
    elif modified_number.startswith('0'):
        modified_number = '+38' + modified_number
    else:
        modified_number = '+380' + modified_number
    modified_number = re.sub(r"(\d{2})(\d{3})(\d{3})(\d{4})", r"\1 (\2) \3-\4", modified_number)

    return modified_number

modified_number = normalize_phone(raw_number)
print ('Option #1:', modified_number)

print('-'*30, 'Exercise #3 :', sep='\n')

def normalize_phone_2(raw_number):
    pattern = r'\D'
    repl = ""
    modified_number = re.sub(pattern, repl, raw_number)
    modified_number = '+380' + modified_number[-9:]
    modified_number = re.sub(r"(\d{2})(\d{3})(\d{3})(\d{4})", r"\1 (\2) \3-\4", modified_number)

    return modified_number

modified_number_2 = normalize_phone_2(raw_number)
print ('Option #2:', modified_number_2)
