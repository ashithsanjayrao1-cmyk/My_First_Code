# def double_number(x):
#     return x*2


# double_number = lambda x: x * 2

# lambda
get_area = lambda length , width : length * width

print(get_area(5,4))

clean_name = lambda text : text.strip().title()

print(clean_name("         ashItH                          "))

#map

prices = [10,20,30]

texed_prices = list(map(lambda x: x + 2, prices))

print(texed_prices)

#filter

ages = [14, 18 , 21 ,12, 30]

adults = list(filter(lambda x : x >= 18 , ages))

print(adults)