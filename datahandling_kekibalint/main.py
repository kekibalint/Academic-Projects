from generator import generate_couriers, generate_deliveries, generate_packages, Courier, Delivery, Package
from handler import save_csv, save_json, save_xlsx


if __name__ == "__main__":

    couriers = generate_couriers(10)
    deliveries = generate_deliveries(20, len(couriers))
    packages = generate_packages(30, len(deliveries))


    courier_fields = ["courier_id", "name", "phone"]
    delivery_fields = ["delivery_id", "courier_id", "address", "delivery_date"]
    package_fields = ["package_id", "delivery_id", "weight", "size", "product_type"]


    save_csv(couriers, "couriers.csv", courier_fields)
    save_csv(deliveries, "deliveries.csv", delivery_fields)
    save_csv(packages, "packages.csv", package_fields)


    save_json(couriers, "couriers.json", courier_fields)
    save_json(deliveries, "deliveries.json", delivery_fields)
    save_json(packages, "packages.json", package_fields)


    save_xlsx(couriers, "Couriers", "couriers.xlsx", courier_fields)
    save_xlsx(deliveries, "Deliveries", "deliveries.xlsx", delivery_fields)
    save_xlsx(packages, "Packages", "packages.xlsx", package_fields)

    print("Adatok mentése kész")