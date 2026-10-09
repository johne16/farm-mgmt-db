# Entity Attributes

## Farms
- farm_id: primary key
- farm_name
- street_address
- city
- state
- zip_code
- total_acres
- established_date
- phone

## Equipment
- equipment_id: primary key
- equipment_name
- equipment_type: tractor, harvester, irrigation, trailer
- manufacturer
- model
- serial_number
- purchase_date
- purchase_price
- condition_status: operational, in repair, retired
- last_service_date: nullable
- farm_id: foreign key to Farms
- building_id: foreign key to Buildings, nullable

## Animals
- animal_id: primary key
- species
- breed
- sex
- birth_date
- weight_lbs
- health_status
- acquisition_date
- purpose: dairy, meat, breeding, eggs
- farm_id: foreign key to Farms
- building_id: foreign key to Buildings, nullable
- move_in_date: nullable

## Crops
- crop_id: primary key
- crop_name
- variety
- yield_unit: bushels, tons, lbs

## Plantings
- planting_id: primary key
- field_number
- acres_planted
- planting_date
- expected_harvest_date
- actual_harvest_date: nullable
- yield_amount: nullable
- growth_status: planted, growing, harvested
- farm_id: foreign key to Farms
- crop_id: foreign key to Crops

## Workers
- worker_id: primary key
- first_name
- last_name
- job_title: equipment operator, livestock handler, field hand, mechanic, manager
- hire_date
- hourly_wage
- employment_type: full time, part time, seasonal
- phone
- email
- farm_id: foreign key to Farms

## Customers
- customer_id: primary key
- customer_name
- customer_type: individual, restaurant, grocer, distributor
- street_address: nullable
- city: nullable
- state: nullable
- zip_code: nullable
- phone: nullable
- email: nullable
- constraint: CHECK (phone IS NOT NULL OR email IS NOT NULL)

## Buildings
- building_id: primary key
- building_name: nullable
- building_type: barn, silo, greenhouse, storage shed, coop
- square_feet
- capacity
- capacity_unit: animals, tons, bushels, machines
- year_built
- condition_status
- farm_id: foreign key to Farms

## Orders
- order_id: primary key
- order_date
- delivery_date: nullable
- order_status: pending, shipped, delivered, cancelled
- payment_status: paid, unpaid
- customer_id: foreign key to Customers
- farm_id: foreign key to Farms

## Products
- product_id: primary key
- product_name
- product_category: produce, grain, dairy, meat, eggs, livestock
- unit_of_measure
- list_price

## Bills
- bill_id: primary key
- bill_category: feed, seed, utilities, repairs, supplies
- issue_date
- due_date
- amount_due
- farm_id: foreign key to Farms
- vendor_id: foreign key to Vendors

## Vendors
- vendor_id: primary key
- vendor_name
- street_address
- city
- state
- zip_code
- phone
- email

## Payments
- payment_id: primary key
- payment_date
- payment_amount
- payment_method: cash, check, card, transfer
- bill_id: foreign key to Bills

# Relationship Sets (Business Rules)

| Relationship | Entities | Cardinality | Participation | Description |
|---|---|---|---|---|
| Employs | Farms, Workers | one farm to many workers | every worker has exactly one farm | A farm employs any number of workers. Each worker works at one farm. |
| Owns | Farms, Equipment | one to many | every piece of equipment has exactly one farm | A farm owns any number of pieces of equipment. Each piece of equipment belongs to one farm. |
| Has | Farms, Buildings | one to many | every building has exactly one farm | A farm has any number of buildings. Each building sits on one farm. |
| Grows | Farms, Plantings | one farm to many plantings | every planting has exactly one farm | A farm grows any number of plantings. Each planting is grown on one farm. |
| Planting_of | Plantings, Crops | many plantings to one crop | every planting has exactly one crop | Each planting is of one crop. A crop can be planted any number of times. |
| Raises | Farms, Animals | one to many | every animal has exactly one farm | A farm raises any number of animals. Each animal is raised on one farm. |
| Housed_in | Animals, Buildings | many animals to one building | animal has at most one building | An animal is housed in one building or in none. A building can house any number of animals. |
| Stored_in | Equipment, Buildings | many to one | equipment has at most one building | A piece of equipment is stored in one building or in none. A building can store any number of pieces of equipment. |
| Places | Customers, Orders | one customer to many orders | every order has exactly one customer | A customer places any number of orders. Each order is placed by one customer. |
| Fulfills | Farms, Orders | one farm to many orders | every order has exactly one farm | A farm fulfills any number of orders. Each order is fulfilled by one farm. |
| Contains | Orders, Products | many to many | every order has at least one product | An order contains one or more products, each with a quantity and a unit price. A product can appear in any number of orders. |
| Stocks | Farms, Products | many to many | optional on both sides | A farm stocks any number of products, each with a quantity on hand. A product can be stocked by any number of farms. |
| Owes | Farms, Bills | one farm to many bills | every bill has exactly one farm | A farm owes any number of bills. Each bill is owed by one farm. |
| Issues | Vendors, Bills | one vendor to many bills | every bill has exactly one vendor | A vendor issues any number of bills. Each bill is issued by one vendor. |
| Applied_to | Payments, Bills | many payments to one bill | every payment has exactly one bill | Each payment is applied to one bill. A bill can receive any number of payments. |

# Relationship Set Attributes

## Contains
- order_id: primary key, foreign key to Orders, on delete cascade
- product_id: primary key, foreign key to Products
- quantity
- unit_price

## Stocks
- farm_id: primary key, foreign key to Farms, on delete cascade
- product_id: primary key, foreign key to Products, on delete cascade
- quantity_on_hand

# User Interactions

1. The owner can see what is planted and which livestock are on each of their farms.
2. The mechanic can check and update the status of the equipment.
3. The manager can check which products are in stock for a particular farm.
4. The manager can keep track of bills.
5. The owner can see which products are in stock to bring to the farmers market.
