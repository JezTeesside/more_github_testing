numbers = [23,323,5,34,2,42,5,25,5,23,42,342,52,44,77]
total_numbers = len(numbers)
even_numbers = 0
odd_numbers = 0
for number in numbers:
    if(number % 2 == 0):
        even_numbers = even_numbers+1
    else:
        odd_numbers = odd_numbers+1
print(f"Total nos {total_numbers} \n Even nos {even_numbers} \n Odd nos {odd_numbers}")
