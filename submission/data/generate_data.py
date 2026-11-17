import csv
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

data_dir = Path(__file__).resolve().parent
cutoff_date = date(2026, 10, 31)

columns = {
    "Farms": ["farm_id", "farm_name", "street_address", "city", "state", "zip_code", "total_acres", "established_date", "phone"],
    "Crops": ["crop_id", "crop_name", "variety", "yield_unit"],
    "Customers": ["customer_id", "customer_name", "customer_type", "street_address", "city", "state", "zip_code", "phone", "email"],
    "Vendors": ["vendor_id", "vendor_name", "street_address", "city", "state", "zip_code", "phone", "email"],
    "Products": ["product_id", "product_name", "product_category", "unit_of_measure", "list_price"],
    "Buildings": ["building_id", "building_name", "building_type", "square_feet", "capacity", "capacity_unit", "year_built", "condition_status", "farm_id"],
    "Equipment": ["equipment_id", "equipment_name", "equipment_type", "manufacturer", "model", "serial_number", "purchase_date", "purchase_price", "condition_status", "last_service_date", "farm_id", "building_id"],
    "Animals": ["animal_id", "species", "breed", "sex", "birth_date", "weight_lbs", "health_status", "acquisition_date", "purpose", "farm_id", "building_id", "move_in_date"],
    "Plantings": ["planting_id", "field_number", "acres_planted", "planting_date", "expected_harvest_date", "actual_harvest_date", "yield_amount", "growth_status", "farm_id", "crop_id"],
    "Workers": ["worker_id", "first_name", "last_name", "job_title", "hire_date", "hourly_wage", "employment_type", "phone", "email", "farm_id"],
    "Orders": ["order_id", "order_date", "delivery_date", "order_status", "payment_status", "customer_id", "farm_id"],
    "Bills": ["bill_id", "bill_category", "issue_date", "due_date", "amount_due", "farm_id", "vendor_id"],
    "Payments": ["payment_id", "payment_date", "payment_amount", "payment_method", "bill_id"],
    "Contains": ["order_id", "product_id", "quantity", "unit_price"],
    "Stocks": ["farm_id", "product_id", "quantity_on_hand"],
}

towns = [
    ("Ames", "IA", "50010", "515"),
    ("Kearney", "NE", "68847", "308"),
    ("Salina", "KS", "67401", "785"),
    ("Sedalia", "MO", "65301", "660"),
    ("Viroqua", "WI", "54665", "608"),
    ("Mankato", "MN", "56001", "507"),
    ("Wooster", "OH", "44691", "330"),
    ("Goshen", "IN", "46526", "574"),
    ("Decatur", "IL", "62521", "217"),
    ("Brookings", "SD", "57006", "605"),
    ("Columbia", "MO", "65201", "573"),
    ("Lincoln", "NE", "68508", "402"),
    ("Cedar Rapids", "IA", "52401", "319"),
    ("Topeka", "KS", "66603", "785"),
    ("Springfield", "IL", "62701", "217"),
    ("Eau Claire", "WI", "54701", "715"),
    ("Rochester", "MN", "55901", "507"),
    ("Findlay", "OH", "45840", "419"),
    ("Lafayette", "IN", "47901", "765"),
    ("Fargo", "ND", "58102", "701"),
]

name_stems = ["Aspen", "Birch", "Clover", "Dogwood", "Elm", "Fox", "Golden", "Hickory", "Ivy", "Juniper", "Laurel", "Mill", "North", "Pine", "Quail", "Rolling"]
name_endings = ["Bluff", "Brook", "Crossing", "Field", "Glen", "Grove", "Haven", "Hill", "Knoll", "Meadows", "Pond", "Springs", "Valley"]
street_names = ["County Road 4", "Mill Road", "Church Street", "Highway 20", "Prairie Avenue", "River Road", "Orchard Lane", "Depot Street", "Township Road 8", "Lake Road", "Fairview Drive", "School Road"]
first_names = ["Amy", "Brian", "Carmen", "David", "Erin", "Frank", "Grace", "Henry", "Isabel", "Jamal", "Karen", "Liam", "Maria", "Nathan", "Olivia", "Paul", "Quinn", "Rachel", "Steven", "Tara", "Victor", "Wendy", "Xavier", "Yuki"]
last_names = ["Anderson", "Baker", "Castillo", "Dawson", "Evans", "Foster", "Garcia", "Hansen", "Ibrahim", "Jensen", "Kim", "Lindqvist", "Mitchell", "Nguyen", "Olsen", "Patel", "Reed"]

equipment_models = [
    ("tractor", "John Deere", "5075E", 72000),
    ("harvester", "Case IH", "Axial-Flow 6150", 340000),
    ("irrigation", "Valley", "8120 Pivot", 92000),
    ("trailer", "Timpte", "Super Hopper", 62000),
    ("tractor", "Massey Ferguson", "4710", 55000),
    ("harvester", "Claas", "Lexion 6700", 480000),
    ("irrigation", "Reinke", "Electrogator", 84000),
    ("trailer", "Big Tex", "70TV", 7800),
    ("tractor", "New Holland", "T4.120", 68000),
    ("harvester", "John Deere", "S660", 395000),
    ("irrigation", "Zimmatic", "9500P", 88000),
    ("trailer", "Neville", "3000 Series", 38000),
    ("tractor", "Kubota", "M5-111", 61000),
    ("harvester", "New Holland", "CR8.90", 450000),
    ("irrigation", "T-L Irrigation", "Hydro Pivot", 81000),
    ("trailer", "Wilson", "Pacesetter", 56000),
]

animal_breeds = [
    ("Cattle", "Holstein", "dairy", "barn", "1400.00", 2200),
    ("Cattle", "Jersey", "dairy", "barn", "950.00", 2200),
    ("Cattle", "Angus", "meat", "barn", "1200.00", 900),
    ("Cattle", "Hereford", "breeding", "barn", "1700.00", 2500),
    ("Chicken", "Rhode Island Red", "eggs", "coop", "6.00", 500),
    ("Chicken", "Leghorn", "eggs", "coop", "4.50", 500),
    ("Pig", "Duroc", "meat", "barn", "240.00", 300),
    ("Pig", "Yorkshire", "breeding", "barn", "450.00", 1200),
    ("Sheep", "Suffolk", "meat", "barn", "150.00", 500),
    ("Sheep", "Dorset", "breeding", "barn", "160.00", 1500),
    ("Goat", "Nubian", "dairy", "barn", "135.00", 2000),
    ("Goat", "Boer", "meat", "barn", "170.00", 900),
]

crop_varieties = [
    ("Corn", "Golden Bantam", "bushels"), ("Soybeans", "Williams 82", "bushels"), ("Winter wheat", "Hard Red", "bushels"), ("Oats", "Horizon", "bushels"),
    ("Alfalfa", "Vernal", "tons"), ("Sweet potato", "Beauregard", "lbs"), ("Tomato", "Roma", "lbs"), ("Winter squash", "Butternut", "lbs"),
    ("Cabbage", "Early Jersey", "lbs"), ("Potato", "Yukon Gold", "lbs"),
    ("Corn", "Silver Queen", "bushels"), ("Corn", "Peaches and Cream", "bushels"), ("Corn", "Bodacious", "bushels"), ("Corn", "Incredible", "bushels"),
    ("Corn", "Honey Select", "bushels"), ("Corn", "Kandy Korn", "bushels"), ("Corn", "Hickory King", "bushels"), ("Corn", "Bloody Butcher", "bushels"),
    ("Soybeans", "Hutcheson", "bushels"), ("Soybeans", "Essex", "bushels"), ("Soybeans", "Jack", "bushels"), ("Soybeans", "Harosoy", "bushels"),
    ("Soybeans", "Clark", "bushels"), ("Soybeans", "Forrest", "bushels"), ("Soybeans", "Bragg", "bushels"), ("Soybeans", "Amsoy", "bushels"),
    ("Winter wheat", "Turkey Red", "bushels"), ("Winter wheat", "Jagger", "bushels"), ("Winter wheat", "Karl", "bushels"), ("Winter wheat", "Everest", "bushels"),
    ("Winter wheat", "Overley", "bushels"), ("Winter wheat", "Fuller", "bushels"), ("Winter wheat", "TAM 111", "bushels"), ("Winter wheat", "Soft Red", "bushels"),
    ("Oats", "Ogle", "bushels"), ("Oats", "Jerry", "bushels"), ("Oats", "Rodeo", "bushels"), ("Oats", "Shelby", "bushels"), ("Oats", "Saber", "bushels"),
    ("Barley", "Conlon", "bushels"), ("Barley", "Tradition", "bushels"), ("Barley", "Legacy", "bushels"), ("Barley", "Robust", "bushels"), ("Barley", "Morex", "bushels"),
    ("Alfalfa", "Ranger", "tons"), ("Alfalfa", "Buffalo", "tons"), ("Alfalfa", "Apollo", "tons"), ("Alfalfa", "Saranac", "tons"),
    ("Timothy", "Climax", "tons"), ("Timothy", "Clair", "tons"),
    ("Tomato", "Cherokee Purple", "lbs"), ("Tomato", "Brandywine", "lbs"), ("Tomato", "Better Boy", "lbs"), ("Tomato", "Early Girl", "lbs"),
    ("Tomato", "Celebrity", "lbs"), ("Tomato", "Beefsteak", "lbs"), ("Tomato", "San Marzano", "lbs"), ("Tomato", "Amish Paste", "lbs"),
    ("Potato", "Russet Burbank", "lbs"), ("Potato", "Red Norland", "lbs"), ("Potato", "Kennebec", "lbs"), ("Potato", "Katahdin", "lbs"), ("Potato", "Superior", "lbs"), ("Potato", "Atlantic", "lbs"),
    ("Sweet potato", "Covington", "lbs"), ("Sweet potato", "Georgia Jet", "lbs"), ("Sweet potato", "Jewel", "lbs"), ("Sweet potato", "Centennial", "lbs"), ("Sweet potato", "Vardaman", "lbs"),
    ("Winter squash", "Acorn", "lbs"), ("Winter squash", "Spaghetti", "lbs"), ("Winter squash", "Delicata", "lbs"), ("Winter squash", "Hubbard", "lbs"), ("Winter squash", "Kabocha", "lbs"), ("Winter squash", "Buttercup", "lbs"),
    ("Cabbage", "Savoy", "lbs"), ("Cabbage", "Danish Ballhead", "lbs"), ("Cabbage", "Copenhagen Market", "lbs"), ("Cabbage", "Red Acre", "lbs"), ("Cabbage", "Napa", "lbs"),
    ("Pepper", "California Wonder", "lbs"), ("Pepper", "Jalapeno", "lbs"), ("Pepper", "Poblano", "lbs"), ("Pepper", "Cayenne", "lbs"), ("Pepper", "Banana", "lbs"), ("Pepper", "Serrano", "lbs"),
    ("Onion", "Yellow Granex", "lbs"), ("Onion", "Walla Walla", "lbs"), ("Onion", "Red Burgundy", "lbs"), ("Onion", "Candy", "lbs"), ("Onion", "Texas Sweet", "lbs"),
    ("Carrot", "Danvers", "lbs"), ("Carrot", "Nantes", "lbs"), ("Carrot", "Imperator", "lbs"), ("Carrot", "Chantenay", "lbs"),
    ("Green bean", "Blue Lake", "lbs"), ("Green bean", "Provider", "lbs"), ("Green bean", "Contender", "lbs"), ("Green bean", "Kentucky Wonder", "lbs"), ("Green bean", "Roma II", "lbs"),
]

product_list = [
    ("Tomatoes", "produce", "lb", "2.50"), ("Sweet potatoes", "produce", "lb", "1.20"), ("Butternut squash", "produce", "lb", "1.40"), ("Hard red wheat", "grain", "bushel", "7.10"),
    ("Yellow corn", "grain", "bushel", "4.60"), ("Whole milk", "dairy", "gallon", "5.25"), ("Cheddar cheese", "dairy", "lb", "8.50"), ("Ground beef", "meat", "lb", "6.75"),
    ("Brown eggs", "eggs", "dozen", "4.50"), ("Feeder calf", "livestock", "head", "1450.00"),
    ("Cherry tomatoes", "produce", "lb", "3.25"), ("Heirloom tomatoes", "produce", "lb", "3.75"), ("Russet potatoes", "produce", "lb", "0.80"), ("Red potatoes", "produce", "lb", "0.95"),
    ("Yukon Gold potatoes", "produce", "lb", "1.10"), ("Acorn squash", "produce", "lb", "1.25"), ("Spaghetti squash", "produce", "lb", "1.30"), ("Delicata squash", "produce", "lb", "1.60"),
    ("Green cabbage", "produce", "lb", "0.70"), ("Red cabbage", "produce", "lb", "0.85"), ("Napa cabbage", "produce", "lb", "1.15"), ("Bell peppers", "produce", "lb", "2.25"),
    ("Jalapeno peppers", "produce", "lb", "2.75"), ("Poblano peppers", "produce", "lb", "2.60"), ("Yellow onions", "produce", "lb", "0.90"), ("Red onions", "produce", "lb", "1.05"),
    ("Sweet onions", "produce", "lb", "1.20"), ("Carrots", "produce", "lb", "1.00"), ("Green beans", "produce", "lb", "2.40"), ("Sweet corn", "produce", "dozen", "6.00"),
    ("Cucumbers", "produce", "lb", "1.35"), ("Zucchini", "produce", "lb", "1.45"), ("Spinach", "produce", "lb", "3.50"), ("Kale", "produce", "lb", "3.25"),
    ("Lettuce", "produce", "head", "2.00"), ("Broccoli", "produce", "lb", "2.10"), ("Cauliflower", "produce", "lb", "2.20"), ("Beets", "produce", "lb", "1.30"),
    ("Radishes", "produce", "bunch", "1.75"), ("Pumpkins", "produce", "lb", "0.65"),
    ("Soft red wheat", "grain", "bushel", "6.40"), ("Durum wheat", "grain", "bushel", "8.20"), ("White corn", "grain", "bushel", "5.10"), ("Soybeans", "grain", "bushel", "11.30"),
    ("Oats", "grain", "bushel", "4.20"), ("Barley", "grain", "bushel", "5.50"), ("Rye", "grain", "bushel", "6.10"), ("Sorghum", "grain", "bushel", "5.20"),
    ("Alfalfa hay", "grain", "ton", "210.00"), ("Timothy hay", "grain", "ton", "240.00"), ("Wheat straw", "grain", "ton", "120.00"), ("Sunflower seed", "grain", "bushel", "9.75"),
    ("Cornmeal", "grain", "lb", "1.10"), ("Whole wheat flour", "grain", "lb", "1.35"), ("Rolled oats", "grain", "lb", "1.50"),
    ("Two percent milk", "dairy", "gallon", "5.00"), ("Skim milk", "dairy", "gallon", "4.75"), ("Heavy cream", "dairy", "quart", "5.50"), ("Unsalted butter", "dairy", "lb", "6.25"),
    ("Salted butter", "dairy", "lb", "6.40"), ("Plain yogurt", "dairy", "quart", "4.80"), ("Cottage cheese", "dairy", "lb", "3.90"), ("Mozzarella", "dairy", "lb", "7.75"),
    ("Gouda", "dairy", "lb", "9.25"), ("Swiss cheese", "dairy", "lb", "9.00"), ("Goat milk", "dairy", "gallon", "9.50"), ("Goat cheese", "dairy", "lb", "13.50"),
    ("Ribeye steak", "meat", "lb", "16.50"), ("Sirloin steak", "meat", "lb", "12.75"), ("Chuck roast", "meat", "lb", "8.25"), ("Brisket", "meat", "lb", "9.50"),
    ("Pork chops", "meat", "lb", "6.90"), ("Pork shoulder", "meat", "lb", "5.25"), ("Bacon", "meat", "lb", "8.40"), ("Pork sausage", "meat", "lb", "6.10"),
    ("Ham", "meat", "lb", "6.80"), ("Whole chicken", "meat", "lb", "3.95"), ("Chicken breast", "meat", "lb", "6.20"), ("Chicken thighs", "meat", "lb", "3.80"),
    ("Lamb chops", "meat", "lb", "15.25"), ("Ground lamb", "meat", "lb", "10.50"), ("Goat meat", "meat", "lb", "10.75"),
    ("White eggs", "eggs", "dozen", "3.90"), ("Free range eggs", "eggs", "dozen", "5.50"), ("Duck eggs", "eggs", "dozen", "8.00"), ("Quail eggs", "eggs", "dozen", "7.25"),
    ("Jumbo brown eggs", "eggs", "dozen", "5.25"), ("Medium white eggs", "eggs", "dozen", "3.50"),
    ("Dairy heifer", "livestock", "head", "2100.00"), ("Angus heifer", "livestock", "head", "1900.00"), ("Angus bull", "livestock", "head", "4800.00"), ("Bottle calf", "livestock", "head", "350.00"),
    ("Feeder pig", "livestock", "head", "120.00"), ("Breeding sow", "livestock", "head", "450.00"), ("Market lamb", "livestock", "head", "240.00"), ("Breeding ewe", "livestock", "head", "320.00"),
    ("Dairy goat", "livestock", "head", "380.00"), ("Meat goat", "livestock", "head", "260.00"), ("Laying hen", "livestock", "head", "22.00"), ("Broiler chick", "livestock", "head", "3.50"),
]


def add_days(start_date, days):
    return start_date + timedelta(days=days)


def gen_farms():
    farms = []
    for i in range(1, 9):
        city, state, zip_code, area_code = towns[i - 1]
        farm_name = f"{name_stems[i * 5 % len(name_stems)]} {name_endings[i % len(name_endings)]} Farm"
        street_address = f"{1000 + i * 389 % 9000} {street_names[i % len(street_names)]}"
        total_acres = Decimal(150 + i * 173 % 1200) + (i % 4) * Decimal("0.25")
        established_date = add_days(date(1960, 1, 1), i * 2711 % 20000)
        phone = f"{area_code}-555-01{i:02d}"
        farms.append((i, farm_name, street_address, city, state, zip_code, total_acres, established_date, phone))
    return farms


def gen_crops():
    crops = []
    for crop_id, (crop_name, variety, yield_unit) in enumerate(crop_varieties, start=1):
        crops.append((crop_id, crop_name, variety, yield_unit))
    return crops


def gen_customers():
    customers = []
    for i in range(1, 101):
        customer_type = ["individual", "restaurant", "grocer", "distributor"][i % 4]
        city, state, zip_code, area_code = towns[i * 3 % 20]
        first_name = first_names[i % len(first_names)]
        last_name = last_names[i % len(last_names)]
        name_stem = name_stems[i % len(name_stems)]
        if customer_type == "individual":
            customer_name = f"{first_name} {last_name}"
        elif customer_type == "restaurant":
            customer_name = name_stem + [" Kitchen", " Bistro", " Table", " Cafe"][i % 4]
        elif customer_type == "grocer":
            customer_name = name_stem + [" Market", " Grocers", " Foods"][i % 3]
        else:
            customer_name = name_stem + " Food Distributors"
        if customer_type == "individual" and i % 8 == 0:
            street_address = None
        else:
            street_address = f"{100 + i * 53 % 9000} {street_names[i % len(street_names)]}"
        if customer_type == "individual" and i % 5 == 0:
            phone = None
        else:
            phone = f"{area_code}-555-01{i * 3 % 100:02d}"
        if customer_type == "individual" and i % 5 == 1:
            email = None
        elif customer_type == "individual":
            email = f"{first_name}.{last_name}".lower() + "@example.com"
        else:
            email = f"orders{i}@example.com"
        customers.append((i, customer_name, customer_type, street_address, city, state, zip_code, phone, email))
    return customers


def gen_vendors():
    vendors = []
    for i in range(1, 101):
        city, state, zip_code, area_code = towns[i * 7 % 20]
        vendor_name = name_stems[i % len(name_stems)] + [" Feed and Grain", " Seed Co.", " Electric Co-op", " Ag Repair", " Farm Supply"][i % 5]
        street_address = f"{200 + i * 61 % 7000} {street_names[i % len(street_names)]}"
        phone = f"{area_code}-555-01{i * 7 % 100:02d}"
        vendors.append((i, vendor_name, street_address, city, state, zip_code, phone, f"office{i}@example.com"))
    return vendors


def gen_products():
    products = []
    for product_id, (product_name, product_category, unit_of_measure, list_price) in enumerate(product_list, start=1):
        products.append((product_id, product_name, product_category, unit_of_measure, list_price))
    return products


def gen_buildings():
    buildings = []
    for i in range(1, 101):
        building_type = ["barn", "silo", "greenhouse", "storage shed", "coop"][i % 5]
        if i % 17 == 0:
            building_name = None
        else:
            building_name = ["North", "South", "East", "West", "Upper", "Lower"][i % 6] + " " + building_type
        square_feet = {
            "barn": 6000 + i * 83 % 10000,
            "silo": 800 + i * 11 % 700,
            "greenhouse": 2000 + i * 29 % 4000,
            "storage shed": 3000 + i * 47 % 4000,
            "coop": 1200 + i * 19 % 1800,
        }[building_type]
        capacity = {
            "barn": 40 + i * 7 % 130,
            "silo": 10000 + i * 211 % 20000,
            "greenhouse": 20 + i % 40,
            "storage shed": 4 + i % 8,
            "coop": 150 + i * 13 % 500,
        }[building_type]
        capacity_unit = {
            "barn": "animals",
            "silo": "bushels",
            "greenhouse": "tons",
            "storage shed": "machines",
            "coop": "animals",
        }[building_type]
        year_built = 1960 + i * 41 % 64
        condition_status = ["good", "good", "fair", "good", "poor"][i * 3 % 5]
        buildings.append((i, building_name, building_type, square_feet, capacity, capacity_unit, year_built, condition_status, 1 + i % 8))
    return buildings


def gen_equipment():
    buildings = gen_buildings()
    equipment = []
    for i in range(1, 101):
        equipment_type, manufacturer, model, base_price = equipment_models[i % 16]
        farm_id = 1 + i // 11 % 8
        purchase_date = add_days(date(2008, 1, 1), i * 311 % 6500)
        if i % 11 == 0:
            condition_status = "retired"
        elif i % 7 == 0:
            condition_status = "in repair"
        else:
            condition_status = "operational"
        equipment_name = ["Main", "North field", "South field", "East field", "West field", "Backup"][i % 6] + " " + equipment_type
        serial_number = manufacturer.replace(" ", "")[:3].upper() + "-" + f"{i * 911 % 100000:05d}"
        purchase_price = round(base_price * (Decimal("0.90") + (i % 5) * Decimal("0.05")), 2)
        if condition_status == "retired":
            last_service_date = add_days(purchase_date, 200)
        elif i % 13 == 0:
            last_service_date = None
        else:
            last_service_date = add_days(cutoff_date, -(i * 29 % 300))
        if equipment_type == "irrigation":
            building_id = None
        else:
            building_id = min((row[0] for row in buildings if row[8] == farm_id and row[5] == "machines"), default=None)
        equipment.append((i, equipment_name, equipment_type, manufacturer, model, serial_number, purchase_date, purchase_price, condition_status, last_service_date, farm_id, building_id))
    return equipment


def gen_animals():
    buildings = gen_buildings()
    animals = []
    for i in range(1, 101):
        species, breed, purpose, home_type, base_weight, max_age_days = animal_breeds[i % 12]
        farm_id = 1 + i // 12 % 8
        birth_date = add_days(date(2026, 9, 1), -(120 + i * 37 % max_age_days))
        building_id = min((row[0] for row in buildings if row[8] == farm_id and row[2] == home_type), default=None)
        sex = "female" if purpose in ("eggs", "dairy") or i % 2 == 0 else "male"
        weight_lbs = round(Decimal(base_weight) * (Decimal("0.85") + (i % 7) * Decimal("0.05")), 2)
        if i % 17 == 0:
            health_status = "sick"
        elif i % 19 == 0:
            health_status = "injured"
        elif i % 23 == 0:
            health_status = "under treatment"
        else:
            health_status = "healthy"
        acquisition_date = add_days(birth_date, i % 60)
        move_in_date = None if building_id is None else add_days(birth_date, i % 60 + i % 14)
        animals.append((i, species, breed, sex, birth_date, weight_lbs, health_status, acquisition_date, purpose, farm_id, building_id, move_in_date))
    return animals


def gen_plantings():
    crops = gen_crops()
    plantings = []
    crop_count = len(crops)
    crop_by_id = {row[0]: row for row in crops}
    for i in range(1, 101):
        crop_id = 1 + i % crop_count
        crop_name = crop_by_id[crop_id][1]
        yield_unit = crop_by_id[crop_id][3]
        is_winter_wheat = crop_name == "Winter wheat"
        acres_planted = Decimal(5 + i * 13 % 200) + (i % 4) * Decimal("0.25")
        if is_winter_wheat:
            planting_date = add_days(date(2025 + i % 2, 9, 20), i % 30)
            expected_harvest_date = add_days(planting_date, 240 + i % 30)
        else:
            planting_date = add_days(date(2025 + i % 2, 4, 1), i * 23 % 120)
            expected_harvest_date = add_days(planting_date, 80 + i * 7 % 70)
        is_harvested = add_days(expected_harvest_date, 5) <= cutoff_date
        actual_harvest_date = add_days(expected_harvest_date, i % 6) if is_harvested else None
        if not is_harvested:
            yield_amount = None
        elif yield_unit == "bushels":
            yield_amount = acres_planted * (40 + i % 130)
        elif yield_unit == "tons":
            yield_amount = acres_planted * (2 + i % 4)
        else:
            yield_amount = acres_planted * (8000 + i * 7 % 22000)
        if is_harvested:
            growth_status = "harvested"
        elif (cutoff_date - planting_date).days >= 14 and not is_winter_wheat:
            growth_status = "growing"
        else:
            growth_status = "planted"
        plantings.append((i, 1 + i % 20, acres_planted, planting_date, expected_harvest_date, actual_harvest_date, yield_amount, growth_status, 1 + i % 8, crop_id))
    return plantings


def gen_workers():
    workers = []
    base_wages = {
        "manager": Decimal("28.00"),
        "mechanic": Decimal("25.00"),
        "equipment operator": Decimal("22.00"),
        "livestock handler": Decimal("19.00"),
        "field hand": Decimal("16.00"),
    }
    for i in range(1, 101):
        first_name = first_names[i * 5 % len(first_names)]
        last_name = last_names[i * 3 % len(last_names)]
        job_title = ["field hand", "livestock handler", "field hand", "equipment operator", "field hand", "livestock handler", "mechanic", "manager"][i % 8]
        employment_type = ["full time", "full time", "part time", "seasonal"][i * 3 % 4]
        if employment_type == "seasonal":
            hire_date = add_days(date(2026, 4, 1), i % 60)
        else:
            hire_date = add_days(date(2005, 1, 1), i * 113 % 7700)
        hourly_wage = base_wages[job_title] + (i % 8) * Decimal("0.50")
        area_code = towns[i % 20][3]
        phone = f"{area_code}-555-01{i * 9 % 100:02d}"
        email = f"{first_name}.{last_name}".lower() + f"{i}@example.com"
        workers.append((i, first_name, last_name, job_title, hire_date, hourly_wage, employment_type, phone, email, 1 + i // 8 % 8))
    return workers


def gen_orders():
    orders = []
    for i in range(1, 101):
        age_days = i * 17 % 360
        order_date = add_days(date(2026, 10, 30), -age_days)
        if i % 13 == 0:
            order_status = "cancelled"
        elif age_days < 20:
            order_status = "pending"
        elif age_days < 45:
            order_status = "shipped"
        else:
            order_status = "delivered"
        if order_status == "delivered":
            delivery_date = add_days(order_date, 1 + i % 5)
        elif order_status == "shipped":
            delivery_date = add_days(cutoff_date, 1 + i % 6)
        else:
            delivery_date = None
        is_paid = (
            (order_status == "delivered" and i % 7 != 0)
            or (order_status == "shipped" and i % 2 == 0)
            or (order_status == "pending" and i % 3 == 0)
        )
        payment_status = "paid" if is_paid else "unpaid"
        orders.append((i, order_date, delivery_date, order_status, payment_status, 1 + i * 7 % 100, 1 + i % 8))
    return orders


def gen_bills():
    bills = []
    for i in range(1, 101):
        bill_category = ["feed", "seed", "utilities", "repairs", "supplies"][i % 5]
        issue_date = add_days(date(2026, 10, 25), -(i * 19 % 420))
        due_date = add_days(issue_date, 30)
        amount_due = Decimal([3000, 2500, 900, 1200, 600][i % 5] + i * 67 % 3000) + (i % 4) * Decimal("0.25")
        vendor_id = 11 + (i % 5 + 4) % 5 + 5 * (i % 18)
        bills.append((i, bill_category, issue_date, due_date, amount_due, 1 + i % 8, vendor_id))
    return bills


def gen_payments():
    bills = gen_bills()
    payments = []
    payment_parts = []
    for bill_id, _, issue_date, _, amount_due, _, _ in bills:
        if bill_id % 6 == 0:
            continue
        first_share = round(amount_due * Decimal("0.6"), 2)
        if bill_id % 2 == 1:
            payment_parts.append((bill_id, issue_date, 12 + bill_id % 15, first_share))
            payment_parts.append((bill_id, issue_date, 30 + bill_id % 8, amount_due - first_share))
        else:
            payment_parts.append((bill_id, issue_date, 12 + bill_id % 15, amount_due))
    for payment_id, (bill_id, issue_date, day_offset, payment_amount) in enumerate(payment_parts, start=1):
        payment_date = min(add_days(issue_date, day_offset), cutoff_date)
        payment_method = ["cash", "check", "card", "transfer"][bill_id % 4]
        payments.append((payment_id, payment_date, payment_amount, payment_method, bill_id))
    return payments


def gen_stocks():
    stocks = []
    for farm_id in range(1, 9):
        for k in range(13):
            product_id = 1 + (farm_id * 7 + k * 13) % 100
            stocks.append((farm_id, product_id, 20 + (farm_id * 97 + k * 41) % 4000))
    return stocks


def gen_contains():
    customers = gen_customers()
    products = gen_products()
    orders = gen_orders()
    stocks = gen_stocks()
    contains = []
    customer_type_by_id = {row[0]: row[2] for row in customers}
    product_by_id = {row[0]: row for row in products}
    for order_id, _, _, _, _, customer_id, farm_id in orders:
        customer_type = customer_type_by_id[customer_id]
        farm_product_ids = [row[1] for row in stocks if row[0] == farm_id]
        farm_product_ids.sort(key=lambda product_id: ((product_id + order_id) % 7, product_id))
        for product_id in farm_product_ids[:1 + order_id % 3]:
            _, _, product_category, unit_of_measure, list_price = product_by_id[product_id]
            if customer_type == "individual" or product_category == "livestock" or unit_of_measure == "ton":
                quantity = 1 + order_id * product_id % 6
            else:
                quantity = 20 + order_id * product_id * 31 % 480
            if customer_type == "individual":
                price_factor = Decimal("1.00")
            else:
                price_factor = Decimal("0.90") + (order_id % 3) * Decimal("0.05")
            contains.append((order_id, product_id, quantity, round(Decimal(list_price) * price_factor, 2)))
    return contains


def write_csv(table_name, rows):
    csv_path = data_dir / f"{table_name.lower()}.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(columns[table_name])
        for row in rows:
            writer.writerow(["" if value is None else value for value in row])
    print(f"Wrote {csv_path.name}.")


def main():
    tables = {
        "Farms": gen_farms(),
        "Crops": gen_crops(),
        "Customers": gen_customers(),
        "Vendors": gen_vendors(),
        "Products": gen_products(),
        "Buildings": gen_buildings(),
        "Equipment": gen_equipment(),
        "Animals": gen_animals(),
        "Plantings": gen_plantings(),
        "Workers": gen_workers(),
        "Orders": gen_orders(),
        "Bills": gen_bills(),
        "Payments": gen_payments(),
        "Contains": gen_contains(),
        "Stocks": gen_stocks(),
    }
    for table_name, rows in tables.items():
        write_csv(table_name, rows)
    print("Data generation complete.")


if __name__ == "__main__":
    main()
