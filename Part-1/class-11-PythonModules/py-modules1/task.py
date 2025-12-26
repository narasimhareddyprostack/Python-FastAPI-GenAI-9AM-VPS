from random import choice
coin_flip=['Head', 'Tail']

head_count=0
tail_count=0
for value in range(100):
    result=choice(coin_flip)
    if result == 'Head':
        head_count=head_count+1
    else:
        tail_count=tail_count+1

print("No of Head Count:",head_count)
print("No of Tail Count:",tail_count)