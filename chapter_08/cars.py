def make_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer.title(), 'model': model.title()}
    for key, value in options.items():
        car[key] = value
    return car
print(make_car('subaru', 'outback', color='blue', tow_package=True))
