def car_listing(car_prices):
    result = ""
    for car in car_prices.keys():
        result += f"\n{car} costs ${car_prices[car]:,.2f} dollars"
    return result


print(car_listing({
    "Kia Soul": 19000,
    "Lamborghini Diablo": 55000,
    "Ford Fiesta": 13000,
    "Toyota": 24000
}))