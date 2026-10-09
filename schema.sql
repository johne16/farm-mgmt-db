drop table if exists Stocks;
drop table if exists Contains;
drop table if exists Payments;
drop table if exists Bills;
drop table if exists Orders;
drop table if exists Workers;
drop table if exists Plantings;
drop table if exists Animals;
drop table if exists Equipment;
drop table if exists Buildings;
drop table if exists Products;
drop table if exists Vendors;
drop table if exists Customers;
drop table if exists Crops;
drop table if exists Farms;

create table Farms (
 farm_id integer primary key,
 farm_name varchar(64) not null,
 street_address varchar(128) not null,
 city varchar(64) not null,
 state char(2) not null,
 zip_code varchar(10) not null,
 total_acres numeric(10, 2) not null,
 established_date date not null,
 phone varchar(20) not null
);

create table Crops (
 crop_id integer primary key,
 crop_name varchar(64) not null,
 variety varchar(64) not null,
 yield_unit varchar(16) not null,
 check (yield_unit in ('bushels', 'tons', 'lbs'))
);

create table Customers (
 customer_id integer primary key,
 customer_name varchar(64) not null,
 customer_type varchar(16) not null,
 street_address varchar(128),
 city varchar(64),
 state char(2),
 zip_code varchar(10),
 phone varchar(20),
 email varchar(128),
 check (customer_type in ('individual', 'restaurant', 'grocer', 'distributor')),
 check (phone is not null or email is not null)
);

create table Vendors (
 vendor_id integer primary key,
 vendor_name varchar(64) not null,
 street_address varchar(128) not null,
 city varchar(64) not null,
 state char(2) not null,
 zip_code varchar(10) not null,
 phone varchar(20) not null,
 email varchar(128) not null
);

create table Products (
 product_id integer primary key,
 product_name varchar(64) not null,
 product_category varchar(16) not null,
 unit_of_measure varchar(16) not null,
 list_price numeric(10, 2) not null,
 check (product_category in ('produce', 'grain', 'dairy', 'meat', 'eggs', 'livestock'))
);

create table Buildings (
 building_id integer primary key,
 building_name varchar(64),
 building_type varchar(16) not null,
 square_feet integer not null,
 capacity numeric(10, 2) not null,
 capacity_unit varchar(16) not null,
 year_built integer not null,
 condition_status varchar(32) not null,
 farm_id integer not null,
 foreign key (farm_id) references Farms(farm_id),
 check (building_type in ('barn', 'silo', 'greenhouse', 'storage shed', 'coop')),
 check (capacity_unit in ('animals', 'tons', 'bushels', 'machines'))
);

create table Equipment (
 equipment_id integer primary key,
 equipment_name varchar(64) not null,
 equipment_type varchar(16) not null,
 manufacturer varchar(64) not null,
 model varchar(64) not null,
 serial_number varchar(64) not null,
 purchase_date date not null,
 purchase_price numeric(12, 2) not null,
 condition_status varchar(16) not null,
 last_service_date date,
 farm_id integer not null,
 building_id integer,
 foreign key (farm_id) references Farms(farm_id),
 foreign key (building_id) references Buildings(building_id),
 check (equipment_type in ('tractor', 'harvester', 'irrigation', 'trailer')),
 check (condition_status in ('operational', 'in repair', 'retired'))
);

create table Animals (
 animal_id integer primary key,
 species varchar(32) not null,
 breed varchar(64) not null,
 sex varchar(8) not null,
 birth_date date not null,
 weight_lbs numeric(8, 2) not null,
 health_status varchar(32) not null,
 acquisition_date date not null,
 purpose varchar(16) not null,
 farm_id integer not null,
 building_id integer,
 move_in_date date,
 foreign key (farm_id) references Farms(farm_id),
 foreign key (building_id) references Buildings(building_id),
 check (purpose in ('dairy', 'meat', 'breeding', 'eggs'))
);

create table Plantings (
 planting_id integer primary key,
 field_number integer not null,
 acres_planted numeric(10, 2) not null,
 planting_date date not null,
 expected_harvest_date date not null,
 actual_harvest_date date,
 yield_amount numeric(12, 2),
 growth_status varchar(16) not null,
 farm_id integer not null,
 crop_id integer not null,
 foreign key (farm_id) references Farms(farm_id),
 foreign key (crop_id) references Crops(crop_id),
 check (growth_status in ('planted', 'growing', 'harvested'))
);

create table Workers (
 worker_id integer primary key,
 first_name varchar(32) not null,
 last_name varchar(32) not null,
 job_title varchar(32) not null,
 hire_date date not null,
 hourly_wage numeric(6, 2) not null,
 employment_type varchar(16) not null,
 phone varchar(20) not null,
 email varchar(128) not null,
 farm_id integer not null,
 foreign key (farm_id) references Farms(farm_id),
 check (job_title in ('equipment operator', 'livestock handler', 'field hand', 'mechanic', 'manager')),
 check (employment_type in ('full time', 'part time', 'seasonal'))
);

create table Orders (
 order_id integer primary key,
 order_date date not null,
 delivery_date date,
 order_status varchar(16) not null,
 payment_status varchar(8) not null,
 customer_id integer not null,
 farm_id integer not null,
 foreign key (customer_id) references Customers(customer_id),
 foreign key (farm_id) references Farms(farm_id),
 check (order_status in ('pending', 'shipped', 'delivered', 'cancelled')),
 check (payment_status in ('paid', 'unpaid'))
);

create table Bills (
 bill_id integer primary key,
 bill_category varchar(16) not null,
 issue_date date not null,
 due_date date not null,
 amount_due numeric(12, 2) not null,
 farm_id integer not null,
 vendor_id integer not null,
 foreign key (farm_id) references Farms(farm_id),
 foreign key (vendor_id) references Vendors(vendor_id),
 check (bill_category in ('feed', 'seed', 'utilities', 'repairs', 'supplies'))
);

create table Payments (
 payment_id integer primary key,
 payment_date date not null,
 payment_amount numeric(12, 2) not null,
 payment_method varchar(16) not null,
 bill_id integer not null,
 foreign key (bill_id) references Bills(bill_id),
 check (payment_method in ('cash', 'check', 'card', 'transfer'))
);

create table Contains (
 order_id integer,
 product_id integer,
 quantity numeric(10, 2) not null,
 unit_price numeric(10, 2) not null,
 primary key (order_id, product_id),
 foreign key (order_id) references Orders(order_id) on delete cascade,
 foreign key (product_id) references Products(product_id)
);

create table Stocks (
 farm_id integer,
 product_id integer,
 quantity_on_hand numeric(12, 2) not null,
 primary key (farm_id, product_id),
 foreign key (farm_id) references Farms(farm_id) on delete cascade,
 foreign key (product_id) references Products(product_id) on delete cascade
);
