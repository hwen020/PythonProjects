card_no = "5610591081018250"
odd_sum = 0
number = list(card_no)
for (idx,val) in enumerate(number):
    if idx %2 !=0: # this is an odd number
        odd_sum += int(val)
    else:pass
print(odd_sum)