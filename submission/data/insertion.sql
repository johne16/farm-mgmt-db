copy Farms (farm_id, farm_name, street_address, city, state, zip_code, total_acres, established_date, phone)
from '/farm_data/farms.csv' with (format csv, header true);

copy Crops (crop_id, crop_name, variety, yield_unit)
from '/farm_data/crops.csv' with (format csv, header true);

copy Customers (customer_id, customer_name, customer_type, street_address, city, state, zip_code, phone, email)
from '/farm_data/customers.csv' with (format csv, header true);

copy Vendors (vendor_id, vendor_name, street_address, city, state, zip_code, phone, email)
from '/farm_data/vendors.csv' with (format csv, header true);

copy Products (product_id, product_name, product_category, unit_of_measure, list_price)
from '/farm_data/products.csv' with (format csv, header true);

copy Buildings (building_id, building_name, building_type, square_feet, capacity, capacity_unit, year_built, condition_status, farm_id)
from '/farm_data/buildings.csv' with (format csv, header true);

copy Equipment (equipment_id, equipment_name, equipment_type, manufacturer, model, serial_number, purchase_date, purchase_price, condition_status, last_service_date, farm_id, building_id)
from '/farm_data/equipment.csv' with (format csv, header true);

copy Animals (animal_id, species, breed, sex, birth_date, weight_lbs, health_status, acquisition_date, purpose, farm_id, building_id, move_in_date)
from '/farm_data/animals.csv' with (format csv, header true);

copy Plantings (planting_id, field_number, acres_planted, planting_date, expected_harvest_date, actual_harvest_date, yield_amount, growth_status, farm_id, crop_id)
from '/farm_data/plantings.csv' with (format csv, header true);

copy Workers (worker_id, first_name, last_name, job_title, hire_date, hourly_wage, employment_type, phone, email, farm_id)
from '/farm_data/workers.csv' with (format csv, header true);

copy Orders (order_id, order_date, delivery_date, order_status, payment_status, customer_id, farm_id)
from '/farm_data/orders.csv' with (format csv, header true);

copy Bills (bill_id, bill_category, issue_date, due_date, amount_due, farm_id, vendor_id)
from '/farm_data/bills.csv' with (format csv, header true);

copy Payments (payment_id, payment_date, payment_amount, payment_method, bill_id)
from '/farm_data/payments.csv' with (format csv, header true);

copy Contains (order_id, product_id, quantity, unit_price)
from '/farm_data/contains.csv' with (format csv, header true);

copy Stocks (farm_id, product_id, quantity_on_hand)
from '/farm_data/stocks.csv' with (format csv, header true);
