import json

class Cars:
    def __init__(self, brand, model, year, engine_volume, color, body_type, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price

    def to_dict(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'engine_volume': float(self.engine_volume),
            'color': self.color,
            'body_type': self.body_type,
            'mileage': self.mileage,
            'price': float(self.price)
        }


class CarsMixin:
    def create(self, car):
        cars = self.listing()
        cars.append(car.to_dict())
        self.save_cars(cars)

    def listing(self):
        cars = self.retrieve_all()
        return cars

    def retrieve(self, brand, model):
        cars = self.retrieve_all()
        for car in cars:
            if car['brand'] == brand and car['model'] == model:
                return car
        return None

    def update(self, brand, model, data):
        cars = self.retrieve_all()
        for car in cars:
            if car['brand'] == brand and car['model'] == model:
                car.update(data)
                self.save_cars(cars)
                return True
        return False

    def delete(self, brand, model):
        cars = self.retrieve_all()
        for car in cars:
            if car['brand'] == brand and car['model'] == model:
                cars.remove(car)
                self.save_cars(cars)
                return True
        return False

    def retrieve_all(self):
        raise NotImplementedError

    def save_cars(self, cars):
        raise NotImplementedError


class CarsDatabase(CarsMixin):
    def __init__(self, database_name):
        self.database_name = database_name

    def retrieve_all(self):
        try:
            with open(self.database_name, 'r') as file:
                cars = json.load(file)
        except FileNotFoundError:
            cars = []
        return cars

    def save_cars(self, cars):
        with open(self.database_name, 'w') as file:
            json.dump(cars, file, indent=4)


# Пример использования

database = CarsDatabase('cars_database.json')

while True:
    print('--- Управление запасами автомобилей ---')
    print('1. Add a Car') # Добавить автомобиль
    print('2. List All Cars') # Список всех автомобилей
    print('3. Retrieve a Car') # Извлечь автомобиль
    print('4. Update a Car') # Обновление автомобиля
    print('5. Delete a Car') # Удалить автомобиль
    print('6. Exit') # Выход

    choice = input('Enter your choice: ')

    if choice == '1':
        brand = input('Введите бренд: ')
        model = input('Введите модель: ')
        year = int(input('Введите год производства: '))
        engine_volume = float(input('Введите объем двигателя: '))
        color = input('Введите цвет: ')
        body_type = input('Введите тип кузова: ')
        mileage = int(input('Введите пробег: ')) 
        price = float(input('Введите цену: '))  

        car = Cars(brand, model, year, engine_volume, color, body_type, mileage, price)
        database.create(car)  # Добавление автомобиля в базу данных

    elif choice == '2':
        cars = database.listing()  # Получение списка всех автомобилей
        if cars:
            print('--- Список автомобилей ---')
            for car in cars:
                print(f"Brand: {car['brand']}, Model: {car['model']}, Year: {car['year']}, Price: {car['price']}")
        else:
            print('Автомобили не найдены.')

    elif choice == '3':
        brand = input('Введите бренд: ')
        model = input('Введите модель: ')
        car = database.retrieve(brand, model)  # Получение информации об одном автомобиле
        if car:
            print('--- Извлеченный автомобиль ---')
            print(f"Brand: {car['brand']}, Model: {car['model']}, Year: {car['year']}, Price: {car['price']}")
        else:
            print('Автомобиль не найден.')

    elif choice == '4':
        brand = input('Введите бренд: ')
        model = input('Введите модель: ')
        car = database.retrieve(brand, model)  # Получение информации об одном автомобиле
        if car:
            print('--- Обновить автомобиль ---')
            print('Введите новую информацию (оставить пустым, чтобы сохранить существующий):')
            new_brand = input(f"Brand ({car['brand']}): ") or car['brand']
            new_model = input(f"Model ({car['model']}): ") or car['model']
            new_year = int(input(f"Year ({car['year']}): ") or car['year'])
            new_engine_volume = float(input(f"Engine Volume ({car['engine_volume']}): ") or car['engine_volume'])
            new_color = input(f"Color ({car['color']}): ") or car['color']
            new_body_type = input(f"Body Type ({car['body_type']}): ") or car['body_type']
            new_mileage = int(input(f"Mileage ({car['mileage']}): ") or car['mileage'])
            new_price = float(input(f"Price ({car['price']}): ") or car['price'])

            updated_data = {
                'brand': new_brand,
                'model': new_model,
                'year': new_year,
                'engine_volume': new_engine_volume,
                'color': new_color,
                'body_type': new_body_type,
                'mileage': new_mileage,
                'price': new_price
            }

            if database.update(brand, model, updated_data):  # Обновление информации об автомобиле
                print('Автомобиль успешно обновлен.')
            else:
                print('Не удалось обновить автомобиль.')
        else:
            print('Автомобиль не найден.')

    elif choice == '5':
        brand = input('Введите бренд: ')
        model = input('Введите модель: ')
        if database.delete(brand, model):  # Удаление автомобиля
            print('Автомобиль успешно удален.')
        else:
            print('Автомобиль не найден.')

    elif choice == '6':
        break  # Выход из программы

    else:
        print('Неверный выбор. Пожалуйста, попробуйте еще раз.')



