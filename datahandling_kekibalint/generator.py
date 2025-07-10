from faker import Faker
import random


class Courier:
    def __init__(self, courier_id, name, phone):
        self.courier_id = courier_id
        self.name = name
        self.phone = phone

    def write(self):
        return [self.courier_id, self.name, self.phone]

    @staticmethod
    def read(data):
        return Courier(data[0], data[1], data[2])


class Delivery:
    def __init__(self, delivery_id, courier_id, address, delivery_date):
        self.delivery_id = delivery_id
        self.courier_id = courier_id
        self.address = address
        self.delivery_date = delivery_date

    def write(self):
        return [self.delivery_id, self.courier_id, self.address, self.delivery_date]

    @staticmethod
    def read(data):
        return Delivery(data[0], data[1], data[2], data[3])


class Package:
    def __init__(self, package_id, delivery_id, weight, size, product_type):
        self.package_id = package_id
        self.delivery_id = delivery_id
        self.weight = weight
        self.size = size
        self.product_type = product_type

    def write(self):
        return [self.package_id, self.delivery_id, self.weight, self.size, self.product_type]

    @staticmethod
    def read(data):
        return Package(data[0], data[1], data[2], data[3], data[4])


def generate_couriers(num):
    fake = Faker()
    couriers = []
    for i in range(1, num + 1):
        country_code = f"+{random.randint(1, 99)}"
        provider_code = f"{random.randint(10, 99)}"
        phone_number = f"{country_code}-{provider_code}-{random.randint(10000000, 99999999)}"
        couriers.append(Courier(f"C{str(i).zfill(4)}", fake.name(), phone_number))
    return couriers


def generate_deliveries(num, max_couriers):
    fake = Faker()
    return [
        Delivery(
            f"D{str(i).zfill(4)}",
            random.choice([f"C{str(j).zfill(4)}" for j in range(1, max_couriers + 1)]),
            fake.address(),
            fake.date_this_decade(),
        )
        for i in range(1, num + 1)
    ]


def generate_packages(num, max_deliveries):
    product_types = ["Electronics", "Clothing", "Books", "Home", "Toys", "Beauty", "Tools"]

    def generate_size():
        width = random.randint(15, 35)
        height = random.randint(15, 40)
        depth = random.randint(15, 30)
        return f"{width} x {height} x {depth} cm"

    def generate_weight():
        weight = round(random.uniform(0.1, 21.0), 2)
        return f"{weight} kg"

    return [
        Package(
            f"P{str(i).zfill(4)}",
            random.choice([f"D{str(j).zfill(4)}" for j in range(1, max_deliveries + 1)]),
            generate_weight(),
            generate_size(),
            random.choice(product_types)
        )
        for i in range(1, num + 1)
    ]