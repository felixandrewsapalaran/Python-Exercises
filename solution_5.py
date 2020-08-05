# Challenge: Cats With Hats

def get_cats_with_hats(array_of_cats):
    # store all cat with hats on
    cats_with_hats_on = []
    # stops for every 2 cats
    for num in range(1, 100 + 1):
        for cat in range(1, 100 + 1):
            # stops on e# Challenge: Cats With Hats


def get_cats_with_hats(array_of_cats):
    # store all cat with hats on
    cats_with_hats_on = []
    for num in range(1, 100 + 1):
    		# stops for every 2 cats
        for cat in range(1, 100 + 1):
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
	# stops for every 3rd cats
    for cat in range(1, 100 + 1):
        if cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on


cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))



# alternative solution B
number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

# We want the laps to be perform 1 to 100 instead of 
# 0 to 99
for lap in range(1, number_of_laps + 1):
	for cat in range(1, number_of_cats):		
		# only took at cats that are divisible by the lap
		if cat % lap == 0:
			if cat in cats_with_hats:
					cats_with_hats.remove(cat)
			else:
					cats_with_hats.append(cat)

print(cats_with_hats)


# alternative solution C

theCats = {}

for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True
for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless")
very second cat only
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
    for cat in range(1, 100 + 1):
        if cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on


cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))


