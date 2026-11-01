insert into Farms (farm_id, farm_name, street_address, city, state, zip_code, total_acres, established_date, phone) values
 (1, 'Cedar Creek Farm', '2140 County Road 12', 'Ames', 'IA', '50010', 640.00, '1978-04-12', '515-555-0101'),
 (2, 'Stony Hollow Ranch', '8815 Hollow Road', 'Kearney', 'NE', '68847', 1280.00, '1965-09-03', '308-555-0102'),
 (3, 'Willow Bend Farm', '417 Willow Lane', 'Salina', 'KS', '67401', 160.50, '2004-03-22', '785-555-0103'),
 (4, 'Prairie Wind Grain', '30221 Route 9', 'Sedalia', 'MO', '65301', 950.00, '1989-06-15', '660-555-0104'),
 (5, 'Blue Heron Dairy', '6620 Ridge Road', 'Viroqua', 'WI', '54665', 320.00, '1996-05-01', '608-555-0105'),
 (6, 'Lone Oak Farm', '1192 Oak Street', 'Mankato', 'MN', '56001', 410.75, '2001-08-20', '507-555-0106'),
 (7, 'Harvest Moon Acres', '755 Township Road 40', 'Wooster', 'OH', '44691', 275.00, '2010-02-11', '330-555-0107'),
 (8, 'Maple Run Farm', '3304 Maple Run', 'Goshen', 'IN', '46526', 198.25, '2013-10-07', '574-555-0108'),
 (9, 'Red Barn Farm', '5078 Prairie Road', 'Decatur', 'IL', '62521', 520.00, '1982-07-29', '217-555-0109'),
 (10, 'Silver Creek Farm', '2467 Creek Road', 'Brookings', 'SD', '57006', 730.00, '1974-11-18', '605-555-0110');

insert into Crops (crop_id, crop_name, variety, yield_unit) values
 (1, 'Corn', 'Golden Bantam', 'bushels'),
 (2, 'Soybeans', 'Williams 82', 'bushels'),
 (3, 'Winter wheat', 'Hard Red', 'bushels'),
 (4, 'Oats', 'Horizon', 'bushels'),
 (5, 'Alfalfa', 'Vernal', 'tons'),
 (6, 'Sweet potato', 'Beauregard', 'lbs'),
 (7, 'Tomato', 'Roma', 'lbs'),
 (8, 'Winter squash', 'Butternut', 'lbs'),
 (9, 'Cabbage', 'Early Jersey', 'lbs'),
 (10, 'Potato', 'Yukon Gold', 'lbs');

insert into Customers (customer_id, customer_name, customer_type, street_address, city, state, zip_code, phone, email) values
 (1, 'Harvest Table', 'restaurant', '112 Main Street', 'Ames', 'IA', '50010', '515-555-0121', 'orders@harvesttable.example.com'),
 (2, 'The Copper Skillet', 'restaurant', '48 Commerce Street', 'Kearney', 'NE', '68847', '308-555-0122', 'kitchen@copperskillet.example.com'),
 (3, 'Northside Grocers', 'grocer', '900 North Avenue', 'Salina', 'KS', '67401', '785-555-0123', 'buying@northside.example.com'),
 (4, 'Corner Market', 'grocer', '305 Elm Street', 'Ames', 'IA', '50014', '515-555-0124', 'owner@cornermarket.example.com'),
 (5, 'Valley Distributors', 'distributor', '7700 Industrial Parkway', 'Sedalia', 'MO', '65301', '660-555-0125', 'purchasing@valleydist.example.com'),
 (6, 'Heartland Foods Distribution', 'distributor', '1500 Depot Road', 'La Crosse', 'WI', '54601', '608-555-0126', 'supply@heartlandfoods.example.com'),
 (7, 'Dana Whitfield', 'individual', '621 Birch Lane', 'Salina', 'KS', '67401', '785-555-0127', 'dana.whitfield@example.com'),
 (8, 'Marcus Bell', 'individual', null, null, null, null, '308-555-0128', null),
 (9, 'Priya Nair', 'individual', null, 'Ames', 'IA', null, null, 'priya.nair@example.com'),
 (10, 'Fresh Basket', 'grocer', '84 Market Square', 'Columbia', 'MO', '65201', '573-555-0130', 'produce@freshbasket.example.com');

insert into Vendors (vendor_id, vendor_name, street_address, city, state, zip_code, phone, email) values
 (1, 'Prairie Feed Supply', '410 Mill Road', 'Ames', 'IA', '50010', '515-555-0141', 'sales@prairiefeed.example.com'),
 (2, 'Good Seed Co.', '28 Depot Street', 'Salina', 'KS', '67401', '785-555-0142', 'orders@goodseed.example.com'),
 (3, 'Three Rivers Electric', '1000 Power Drive', 'Kearney', 'NE', '68847', '308-555-0143', 'billing@threerivers.example.com'),
 (4, 'Hartley Tractor Repair', '5512 Highway 30', 'Ames', 'IA', '50014', '515-555-0144', 'service@hartleytractor.example.com'),
 (5, 'Midland Farm Supply', '2300 Commerce Drive', 'Sedalia', 'MO', '65301', '660-555-0145', 'sales@midlandfarm.example.com'),
 (6, 'Big Sky Feed and Grain', '77 Elevator Road', 'Kearney', 'NE', '68845', '308-555-0146', 'office@bigskyfeed.example.com'),
 (7, 'County Water District', '150 Courthouse Square', 'Viroqua', 'WI', '54665', '608-555-0147', 'billing@countywater.example.com'),
 (8, 'Ridgeline Seed', '906 Ridgeline Road', 'Sedalia', 'MO', '65302', '660-555-0148', 'orders@ridgelineseed.example.com'),
 (9, 'Ace Ag Mechanics', '3120 Shop Road', 'Salina', 'KS', '67402', '785-555-0149', 'repairs@aceag.example.com'),
 (10, 'Homestead Fencing and Supply', '64 Post Road', 'Viroqua', 'WI', '54665', '608-555-0150', 'sales@homesteadfence.example.com');

insert into Products (product_id, product_name, product_category, unit_of_measure, list_price) values
 (1, 'Tomatoes', 'produce', 'lb', 2.50),
 (2, 'Sweet potatoes', 'produce', 'lb', 1.20),
 (3, 'Butternut squash', 'produce', 'lb', 1.40),
 (4, 'Hard red wheat', 'grain', 'bushel', 7.10),
 (5, 'Yellow corn', 'grain', 'bushel', 4.60),
 (6, 'Whole milk', 'dairy', 'gallon', 5.25),
 (7, 'Cheddar cheese', 'dairy', 'lb', 8.50),
 (8, 'Ground beef', 'meat', 'lb', 6.75),
 (9, 'Brown eggs', 'eggs', 'dozen', 4.50),
 (10, 'Feeder calf', 'livestock', 'head', 1450.00);

insert into Buildings (building_id, building_name, building_type, square_feet, capacity, capacity_unit, year_built, condition_status, farm_id) values
 (1, 'Main dairy barn', 'barn', 12000, 120.00, 'animals', 1998, 'good', 1),
 (2, 'North coop', 'coop', 1800, 300.00, 'animals', 2012, 'good', 1),
 (3, 'Machine shed', 'storage shed', 6000, 8.00, 'machines', 2005, 'fair', 1),
 (4, 'Grain silo', 'silo', 1200, 20000.00, 'bushels', 1990, 'fair', 2),
 (5, 'Cattle barn', 'barn', 15000, 150.00, 'animals', 2001, 'good', 2),
 (6, 'Equipment shed', 'storage shed', 5000, 6.00, 'machines', 2010, 'good', 2),
 (7, 'Propagation greenhouse', 'greenhouse', 4000, 40.00, 'tons', 2018, 'good', 3),
 (8, 'Layer coop', 'coop', 2400, 500.00, 'animals', 2015, 'good', 3),
 (9, 'Hay barn', 'barn', 8000, 200.00, 'tons', 1985, 'fair', 4),
 (10, 'Machinery shed', 'storage shed', 4500, 5.00, 'machines', 1996, 'poor', 4),
 (11, 'Milking barn', 'barn', 9000, 80.00, 'animals', 2008, 'good', 5),
 (12, null, 'silo', 900, 15000.00, 'bushels', 1978, 'fair', 7);

insert into Equipment (equipment_id, equipment_name, equipment_type, manufacturer, model, serial_number, purchase_date, purchase_price, condition_status, last_service_date, farm_id, building_id) values
 (1, 'North field tractor', 'tractor', 'John Deere', '6120M', 'JD6120M-10482', '2019-03-14', 118500.00, 'operational', '2026-08-20', 1, 3),
 (2, 'Main combine', 'harvester', 'Case IH', 'Axial-Flow 7250', 'CIH7250-22817', '2017-07-02', 412000.00, 'operational', '2026-09-05', 1, 3),
 (3, 'Grain trailer', 'trailer', 'Wilson', 'Pacesetter', 'WIL-PS-50311', '2015-05-20', 54000.00, 'in repair', '2026-10-12', 1, 3),
 (4, 'Utility tractor', 'tractor', 'Kubota', 'M7060', 'KUB7060-66120', '2021-04-09', 46800.00, 'operational', '2026-06-18', 2, 6),
 (5, 'Center pivot', 'irrigation', 'Valley', '8000 Series', 'VAL8K-90215', '2014-04-01', 87500.00, 'operational', '2026-04-22', 2, null),
 (6, 'Old forage harvester', 'harvester', 'New Holland', 'FX 40', 'NHFX40-12094', '2003-08-15', 165000.00, 'retired', '2021-09-30', 2, 6),
 (7, 'Row crop tractor', 'tractor', 'New Holland', 'T7.210', 'NHT7-44871', '2020-02-25', 142000.00, 'operational', '2026-07-30', 4, 10),
 (8, 'Greenhouse drip system', 'irrigation', 'Netafim', 'DripNet PC', 'NET-DN-31876', '2018-05-16', 12400.00, 'operational', '2026-03-11', 3, 7),
 (9, 'Flatbed trailer', 'trailer', 'Big Tex', '14ET', 'BT14-77310', '2018-06-11', 9800.00, 'operational', null, 4, 10),
 (10, 'East pivot', 'irrigation', 'Reinke', 'Electrogator II', 'REI-EG-58402', '2016-03-28', 79200.00, 'in repair', '2026-09-17', 6, null),
 (11, 'Compact tractor', 'tractor', 'Kubota', 'L3902', 'KUBL39-20915', '2022-09-13', 28900.00, 'operational', '2026-05-06', 5, null),
 (12, 'Grain combine', 'harvester', 'John Deere', 'S770', 'JDS770-81134', '2021-08-19', 498000.00, 'operational', '2026-08-28', 7, null);

insert into Animals (animal_id, species, breed, sex, birth_date, weight_lbs, health_status, acquisition_date, purpose, farm_id, building_id, move_in_date) values
 (1, 'Cattle', 'Holstein', 'female', '2022-03-18', 1480.00, 'healthy', '2022-03-18', 'dairy', 1, 1, '2023-01-10'),
 (2, 'Cattle', 'Jersey', 'female', '2023-05-02', 960.00, 'under treatment', '2023-11-14', 'dairy', 1, 1, '2023-11-14'),
 (3, 'Chicken', 'Rhode Island Red', 'female', '2025-02-20', 6.20, 'healthy', '2025-03-05', 'eggs', 1, 2, '2025-03-05'),
 (4, 'Cattle', 'Angus', 'male', '2024-04-11', 1250.00, 'healthy', '2024-10-22', 'meat', 2, 5, '2024-10-22'),
 (5, 'Cattle', 'Angus', 'female', '2021-02-27', 1190.00, 'healthy', '2021-02-27', 'breeding', 2, 5, '2021-12-01'),
 (6, 'Cattle', 'Hereford', 'male', '2019-06-09', 1920.00, 'injured', '2020-08-30', 'breeding', 2, 5, '2020-08-30'),
 (7, 'Chicken', 'Plymouth Rock', 'female', '2025-04-06', 7.10, 'healthy', '2025-04-20', 'eggs', 3, 8, '2025-04-20'),
 (8, 'Chicken', 'Leghorn', 'female', '2025-08-15', 4.40, 'sick', '2025-09-01', 'eggs', 3, 8, '2025-09-01'),
 (9, 'Cattle', 'Holstein', 'female', '2021-09-30', 1525.00, 'healthy', '2021-09-30', 'dairy', 5, 11, '2022-07-15'),
 (10, 'Cattle', 'Brown Swiss', 'female', '2022-12-05', 1340.00, 'healthy', '2024-02-19', 'dairy', 5, 11, '2024-02-19'),
 (11, 'Pig', 'Duroc', 'male', '2026-02-14', 245.00, 'healthy', '2026-04-03', 'meat', 6, null, null),
 (12, 'Goat', 'Nubian', 'female', '2023-03-21', 135.00, 'healthy', '2024-05-17', 'dairy', 7, null, null);

insert into Plantings (planting_id, field_number, acres_planted, planting_date, expected_harvest_date, actual_harvest_date, yield_amount, growth_status, farm_id, crop_id) values
 (1, 1, 120.00, '2026-04-28', '2026-09-25', '2026-09-29', 21600.00, 'harvested', 1, 1),
 (2, 2, 85.00, '2026-05-12', '2026-10-05', '2026-10-08', 4420.00, 'harvested', 1, 2),
 (3, 6, 60.00, '2026-05-02', '2026-08-30', '2026-09-02', 210.00, 'harvested', 2, 5),
 (4, 3, 12.00, '2026-07-12', '2026-11-04', null, null, 'growing', 3, 6),
 (5, 7, 8.50, '2026-07-20', '2026-11-09', null, null, 'growing', 3, 8),
 (6, 4, 6.00, '2026-05-05', '2026-08-15', '2026-08-18', 132000.00, 'harvested', 3, 7),
 (7, 9, 240.00, '2026-10-12', '2027-06-20', null, null, 'planted', 4, 3),
 (8, 10, 150.00, '2025-10-08', '2026-06-22', '2026-06-25', 9000.00, 'harvested', 4, 3),
 (9, 5, 40.00, '2026-04-10', '2026-07-15', '2026-07-19', 2640.00, 'harvested', 6, 4),
 (10, 2, 6.25, '2026-08-01', '2026-11-12', null, null, 'growing', 7, 9),
 (11, 8, 18.00, '2026-05-20', '2026-09-20', '2026-09-24', 720000.00, 'harvested', 8, 10),
 (12, 3, 200.00, '2026-05-01', '2026-10-10', '2026-10-15', 34000.00, 'harvested', 9, 1);

insert into Workers (worker_id, first_name, last_name, job_title, hire_date, hourly_wage, employment_type, phone, email, farm_id) values
 (1, 'Elena', 'Marsh', 'manager', '2011-03-07', 32.50, 'full time', '515-555-0161', 'elena.marsh@example.com', 1),
 (2, 'Tom', 'Okafor', 'equipment operator', '2017-05-22', 24.00, 'full time', '515-555-0162', 'tom.okafor@example.com', 1),
 (3, 'Lucy', 'Hart', 'livestock handler', '2021-08-16', 19.75, 'full time', '515-555-0163', 'lucy.hart@example.com', 1),
 (4, 'Ben', 'Sorensen', 'manager', '2008-02-11', 34.00, 'full time', '308-555-0164', 'ben.sorensen@example.com', 2),
 (5, 'Rosa', 'Delgado', 'livestock handler', '2019-04-29', 20.50, 'full time', '308-555-0165', 'rosa.delgado@example.com', 2),
 (6, 'Andre', 'Lewis', 'mechanic', '2015-10-05', 27.25, 'part time', '308-555-0166', 'andre.lewis@example.com', 2),
 (7, 'Mei', 'Tanaka', 'manager', '2014-06-02', 30.00, 'full time', '785-555-0167', 'mei.tanaka@example.com', 3),
 (8, 'Caleb', 'Young', 'field hand', '2026-05-18', 16.50, 'seasonal', '785-555-0168', 'caleb.young@example.com', 3),
 (9, 'Nora', 'Hughes', 'equipment operator', '2020-03-09', 23.50, 'full time', '660-555-0169', 'nora.hughes@example.com', 4),
 (10, 'Sam', 'Petrov', 'field hand', '2026-04-20', 16.00, 'seasonal', '660-555-0170', 'sam.petrov@example.com', 4),
 (11, 'Ivy', 'Larsen', 'livestock handler', '2018-07-23', 21.00, 'full time', '608-555-0171', 'ivy.larsen@example.com', 5),
 (12, 'Omar', 'Haddad', 'field hand', '2023-09-11', 17.25, 'part time', '507-555-0172', 'omar.haddad@example.com', 6);

insert into Orders (order_id, order_date, delivery_date, order_status, payment_status, customer_id, farm_id) values
 (1, '2026-09-14', '2026-09-16', 'delivered', 'paid', 3, 3),
 (2, '2026-09-22', '2026-09-24', 'delivered', 'paid', 1, 1),
 (3, '2026-10-01', '2026-10-05', 'delivered', 'paid', 5, 4),
 (4, '2026-10-06', '2026-10-08', 'delivered', 'unpaid', 4, 1),
 (5, '2026-10-10', '2026-10-13', 'delivered', 'paid', 2, 2),
 (6, '2026-10-14', '2026-10-15', 'delivered', 'paid', 7, 3),
 (7, '2026-10-19', null, 'cancelled', 'unpaid', 8, 2),
 (8, '2026-10-22', '2026-11-02', 'shipped', 'unpaid', 6, 5),
 (9, '2026-10-26', '2026-11-03', 'shipped', 'paid', 3, 1),
 (10, '2026-10-28', null, 'pending', 'unpaid', 9, 1),
 (11, '2026-10-29', null, 'pending', 'paid', 2, 3),
 (12, '2026-10-30', null, 'pending', 'unpaid', 10, 4);

insert into Bills (bill_id, bill_category, issue_date, due_date, amount_due, farm_id, vendor_id) values
 (1, 'feed', '2026-06-01', '2026-07-01', 4280.00, 1, 1),
 (2, 'seed', '2026-03-15', '2026-04-15', 6150.00, 4, 8),
 (3, 'utilities', '2026-07-01', '2026-07-31', 1840.50, 2, 3),
 (4, 'repairs', '2026-08-22', '2026-09-21', 2675.00, 1, 4),
 (5, 'supplies', '2026-05-10', '2026-06-09', 915.25, 4, 5),
 (6, 'feed', '2026-08-05', '2026-09-04', 7320.00, 2, 6),
 (7, 'utilities', '2026-09-01', '2026-10-01', 1260.75, 5, 7),
 (8, 'seed', '2026-06-20', '2026-07-20', 3480.00, 3, 2),
 (9, 'repairs', '2026-09-18', '2026-10-18', 1495.00, 3, 9),
 (10, 'supplies', '2026-09-02', '2026-10-02', 2230.00, 5, 10),
 (11, 'feed', '2026-10-05', '2026-11-04', 5140.00, 1, 1),
 (12, 'utilities', '2026-10-01', '2026-10-31', 1975.40, 2, 3);

insert into Payments (payment_id, payment_date, payment_amount, payment_method, bill_id) values
 (1, '2026-06-26', 4280.00, 'check', 1),
 (2, '2026-04-10', 6150.00, 'transfer', 2),
 (3, '2026-07-20', 1000.00, 'card', 3),
 (4, '2026-08-05', 840.50, 'card', 3),
 (5, '2026-09-18', 2675.00, 'check', 4),
 (6, '2026-06-02', 915.25, 'cash', 5),
 (7, '2026-09-01', 7320.00, 'transfer', 6),
 (8, '2026-09-28', 1260.75, 'transfer', 7),
 (9, '2026-07-15', 2000.00, 'check', 8),
 (10, '2026-10-14', 1495.00, 'card', 9);

insert into Contains (order_id, product_id, quantity, unit_price) values
 (1, 1, 200.00, 2.40),
 (1, 3, 150.00, 1.35),
 (2, 9, 60.00, 4.50),
 (2, 7, 25.00, 8.25),
 (3, 4, 800.00, 7.05),
 (4, 6, 100.00, 5.10),
 (4, 9, 80.00, 4.40),
 (5, 8, 120.00, 6.50),
 (6, 2, 20.00, 1.20),
 (7, 8, 15.00, 6.75),
 (8, 6, 400.00, 4.95),
 (8, 7, 90.00, 8.00),
 (9, 9, 100.00, 4.40),
 (10, 9, 5.00, 4.50),
 (11, 1, 40.00, 2.50),
 (12, 5, 500.00, 4.55);

insert into Stocks (farm_id, product_id, quantity_on_hand) values
 (1, 5, 18400.00),
 (1, 6, 650.00),
 (1, 7, 310.00),
 (1, 9, 420.00),
 (2, 8, 1275.00),
 (2, 10, 34.00),
 (3, 1, 960.00),
 (3, 2, 5200.00),
 (3, 3, 2100.00),
 (4, 4, 7600.00),
 (4, 5, 11250.00),
 (5, 6, 880.00),
 (5, 7, 540.00);

create temp table Towns as
select * from (values
 (0, 'Ames', 'IA', '50010', '515'),
 (1, 'Kearney', 'NE', '68847', '308'),
 (2, 'Salina', 'KS', '67401', '785'),
 (3, 'Sedalia', 'MO', '65301', '660'),
 (4, 'Viroqua', 'WI', '54665', '608'),
 (5, 'Mankato', 'MN', '56001', '507'),
 (6, 'Wooster', 'OH', '44691', '330'),
 (7, 'Goshen', 'IN', '46526', '574'),
 (8, 'Decatur', 'IL', '62521', '217'),
 (9, 'Brookings', 'SD', '57006', '605'),
 (10, 'Columbia', 'MO', '65201', '573'),
 (11, 'Lincoln', 'NE', '68508', '402'),
 (12, 'Cedar Rapids', 'IA', '52401', '319'),
 (13, 'Topeka', 'KS', '66603', '785'),
 (14, 'Springfield', 'IL', '62701', '217'),
 (15, 'Eau Claire', 'WI', '54701', '715'),
 (16, 'Rochester', 'MN', '55901', '507'),
 (17, 'Findlay', 'OH', '45840', '419'),
 (18, 'Lafayette', 'IN', '47901', '765'),
 (19, 'Fargo', 'ND', '58102', '701')
) as t(town_id, city, state, zip_code, area_code);

create temp table Word_lists as
select
 array['Aspen', 'Birch', 'Clover', 'Dogwood', 'Elm', 'Fox', 'Golden', 'Hickory', 'Ivy', 'Juniper', 'Laurel', 'Mill', 'North', 'Pine', 'Quail', 'Rolling'] as name_stems,
 array['Bluff', 'Brook', 'Crossing', 'Field', 'Glen', 'Grove', 'Haven', 'Hill', 'Knoll', 'Meadows', 'Pond', 'Springs', 'Valley'] as name_endings,
 array['County Road 4', 'Mill Road', 'Church Street', 'Highway 20', 'Prairie Avenue', 'River Road', 'Orchard Lane', 'Depot Street', 'Township Road 8', 'Lake Road', 'Fairview Drive', 'School Road'] as street_names,
 array['Amy', 'Brian', 'Carmen', 'David', 'Erin', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jamal', 'Karen', 'Liam', 'Maria', 'Nathan', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Steven', 'Tara', 'Victor', 'Wendy', 'Xavier', 'Yuki'] as first_names,
 array['Anderson', 'Baker', 'Castillo', 'Dawson', 'Evans', 'Foster', 'Garcia', 'Hansen', 'Ibrahim', 'Jensen', 'Kim', 'Lindqvist', 'Mitchell', 'Nguyen', 'Olsen', 'Patel', 'Reed'] as last_names;

create temp table Equipment_models as
select * from (values
 (0, 'tractor', 'John Deere', '5075E', 72000),
 (1, 'harvester', 'Case IH', 'Axial-Flow 6150', 340000),
 (2, 'irrigation', 'Valley', '8120 Pivot', 92000),
 (3, 'trailer', 'Timpte', 'Super Hopper', 62000),
 (4, 'tractor', 'Massey Ferguson', '4710', 55000),
 (5, 'harvester', 'Claas', 'Lexion 6700', 480000),
 (6, 'irrigation', 'Reinke', 'Electrogator', 84000),
 (7, 'trailer', 'Big Tex', '70TV', 7800),
 (8, 'tractor', 'New Holland', 'T4.120', 68000),
 (9, 'harvester', 'John Deere', 'S660', 395000),
 (10, 'irrigation', 'Zimmatic', '9500P', 88000),
 (11, 'trailer', 'Neville', '3000 Series', 38000),
 (12, 'tractor', 'Kubota', 'M5-111', 61000),
 (13, 'harvester', 'New Holland', 'CR8.90', 450000),
 (14, 'irrigation', 'T-L Irrigation', 'Hydro Pivot', 81000),
 (15, 'trailer', 'Wilson', 'Pacesetter', 56000)
) as t(model_id, equipment_type, manufacturer, model, base_price);

create temp table Animal_breeds as
select * from (values
 (0, 'Cattle', 'Holstein', 'dairy', 'barn', 1400.00, 2200),
 (1, 'Cattle', 'Jersey', 'dairy', 'barn', 950.00, 2200),
 (2, 'Cattle', 'Angus', 'meat', 'barn', 1200.00, 900),
 (3, 'Cattle', 'Hereford', 'breeding', 'barn', 1700.00, 2500),
 (4, 'Chicken', 'Rhode Island Red', 'eggs', 'coop', 6.00, 500),
 (5, 'Chicken', 'Leghorn', 'eggs', 'coop', 4.50, 500),
 (6, 'Pig', 'Duroc', 'meat', 'barn', 240.00, 300),
 (7, 'Pig', 'Yorkshire', 'breeding', 'barn', 450.00, 1200),
 (8, 'Sheep', 'Suffolk', 'meat', 'barn', 150.00, 500),
 (9, 'Sheep', 'Dorset', 'breeding', 'barn', 160.00, 1500),
 (10, 'Goat', 'Nubian', 'dairy', 'barn', 135.00, 2000),
 (11, 'Goat', 'Boer', 'meat', 'barn', 170.00, 900)
) as t(breed_id, species, breed, purpose, home_type, base_weight, max_age_days);

insert into Farms (farm_id, farm_name, street_address, city, state, zip_code, total_acres, established_date, phone)
select
 i,
 name_stems[1 + i % cardinality(name_stems)] || ' ' || name_endings[1 + i % cardinality(name_endings)] || ' Farm',
 (100 + i * 37 % 8000)::text || ' ' || street_names[1 + i % cardinality(street_names)],
 city,
 state,
 zip_code,
 80 + i * 73 % 1900 + (i % 4) * 0.25,
 date '1955-01-01' + i * 397 % 24000,
 area_code || '-555-01' || lpad((i % 100)::text, 2, '0')
from generate_series(11, 100) as i
join Towns on town_id = i % 20
cross join Word_lists;

insert into Crops (crop_id, crop_name, variety, yield_unit)
select 10 + row_number() over (), crop_name, variety, yield_unit
from (values
 ('Corn', 'Silver Queen', 'bushels'), ('Corn', 'Peaches and Cream', 'bushels'), ('Corn', 'Bodacious', 'bushels'), ('Corn', 'Incredible', 'bushels'),
 ('Corn', 'Honey Select', 'bushels'), ('Corn', 'Kandy Korn', 'bushels'), ('Corn', 'Hickory King', 'bushels'), ('Corn', 'Bloody Butcher', 'bushels'),
 ('Soybeans', 'Hutcheson', 'bushels'), ('Soybeans', 'Essex', 'bushels'), ('Soybeans', 'Jack', 'bushels'), ('Soybeans', 'Harosoy', 'bushels'),
 ('Soybeans', 'Clark', 'bushels'), ('Soybeans', 'Forrest', 'bushels'), ('Soybeans', 'Bragg', 'bushels'), ('Soybeans', 'Amsoy', 'bushels'),
 ('Winter wheat', 'Turkey Red', 'bushels'), ('Winter wheat', 'Jagger', 'bushels'), ('Winter wheat', 'Karl', 'bushels'), ('Winter wheat', 'Everest', 'bushels'),
 ('Winter wheat', 'Overley', 'bushels'), ('Winter wheat', 'Fuller', 'bushels'), ('Winter wheat', 'TAM 111', 'bushels'), ('Winter wheat', 'Soft Red', 'bushels'),
 ('Oats', 'Ogle', 'bushels'), ('Oats', 'Jerry', 'bushels'), ('Oats', 'Rodeo', 'bushels'), ('Oats', 'Shelby', 'bushels'), ('Oats', 'Saber', 'bushels'),
 ('Barley', 'Conlon', 'bushels'), ('Barley', 'Tradition', 'bushels'), ('Barley', 'Legacy', 'bushels'), ('Barley', 'Robust', 'bushels'), ('Barley', 'Morex', 'bushels'),
 ('Alfalfa', 'Ranger', 'tons'), ('Alfalfa', 'Buffalo', 'tons'), ('Alfalfa', 'Apollo', 'tons'), ('Alfalfa', 'Saranac', 'tons'),
 ('Timothy', 'Climax', 'tons'), ('Timothy', 'Clair', 'tons'),
 ('Tomato', 'Cherokee Purple', 'lbs'), ('Tomato', 'Brandywine', 'lbs'), ('Tomato', 'Better Boy', 'lbs'), ('Tomato', 'Early Girl', 'lbs'),
 ('Tomato', 'Celebrity', 'lbs'), ('Tomato', 'Beefsteak', 'lbs'), ('Tomato', 'San Marzano', 'lbs'), ('Tomato', 'Amish Paste', 'lbs'),
 ('Potato', 'Russet Burbank', 'lbs'), ('Potato', 'Red Norland', 'lbs'), ('Potato', 'Kennebec', 'lbs'), ('Potato', 'Katahdin', 'lbs'), ('Potato', 'Superior', 'lbs'), ('Potato', 'Atlantic', 'lbs'),
 ('Sweet potato', 'Covington', 'lbs'), ('Sweet potato', 'Georgia Jet', 'lbs'), ('Sweet potato', 'Jewel', 'lbs'), ('Sweet potato', 'Centennial', 'lbs'), ('Sweet potato', 'Vardaman', 'lbs'),
 ('Winter squash', 'Acorn', 'lbs'), ('Winter squash', 'Spaghetti', 'lbs'), ('Winter squash', 'Delicata', 'lbs'), ('Winter squash', 'Hubbard', 'lbs'), ('Winter squash', 'Kabocha', 'lbs'), ('Winter squash', 'Buttercup', 'lbs'),
 ('Cabbage', 'Savoy', 'lbs'), ('Cabbage', 'Danish Ballhead', 'lbs'), ('Cabbage', 'Copenhagen Market', 'lbs'), ('Cabbage', 'Red Acre', 'lbs'), ('Cabbage', 'Napa', 'lbs'),
 ('Pepper', 'California Wonder', 'lbs'), ('Pepper', 'Jalapeno', 'lbs'), ('Pepper', 'Poblano', 'lbs'), ('Pepper', 'Cayenne', 'lbs'), ('Pepper', 'Banana', 'lbs'), ('Pepper', 'Serrano', 'lbs'),
 ('Onion', 'Yellow Granex', 'lbs'), ('Onion', 'Walla Walla', 'lbs'), ('Onion', 'Red Burgundy', 'lbs'), ('Onion', 'Candy', 'lbs'), ('Onion', 'Texas Sweet', 'lbs'),
 ('Carrot', 'Danvers', 'lbs'), ('Carrot', 'Nantes', 'lbs'), ('Carrot', 'Imperator', 'lbs'), ('Carrot', 'Chantenay', 'lbs'),
 ('Green bean', 'Blue Lake', 'lbs'), ('Green bean', 'Provider', 'lbs'), ('Green bean', 'Contender', 'lbs'), ('Green bean', 'Kentucky Wonder', 'lbs'), ('Green bean', 'Roma II', 'lbs')
) as t(crop_name, variety, yield_unit);

insert into Customers (customer_id, customer_name, customer_type, street_address, city, state, zip_code, phone, email)
select
 i,
 case customer_type
  when 'individual' then first_names[1 + i % cardinality(first_names)] || ' ' || last_names[1 + i % cardinality(last_names)]
  when 'restaurant' then name_stems[1 + i % cardinality(name_stems)] || (array[' Kitchen', ' Bistro', ' Table', ' Cafe'])[1 + i % 4]
  when 'grocer' then name_stems[1 + i % cardinality(name_stems)] || (array[' Market', ' Grocers', ' Foods'])[1 + i % 3]
  else name_stems[1 + i % cardinality(name_stems)] || ' Food Distributors'
 end,
 customer_type,
 case when customer_type = 'individual' and i % 8 = 0 then null
  else (100 + i * 53 % 9000)::text || ' ' || street_names[1 + i % cardinality(street_names)] end,
 city,
 state,
 zip_code,
 case when customer_type = 'individual' and i % 5 = 0 then null
  else area_code || '-555-01' || lpad((i * 3 % 100)::text, 2, '0') end,
 case when customer_type = 'individual' and i % 5 = 1 then null
  when customer_type = 'individual' then lower(first_names[1 + i % cardinality(first_names)] || '.' || last_names[1 + i % cardinality(last_names)]) || '@example.com'
  else 'orders' || i || '@example.com' end
from generate_series(11, 100) as i
cross join lateral (select (array['individual', 'restaurant', 'grocer', 'distributor'])[1 + i % 4] as customer_type) as types
join Towns on town_id = i * 3 % 20
cross join Word_lists;

insert into Vendors (vendor_id, vendor_name, street_address, city, state, zip_code, phone, email)
select
 i,
 name_stems[1 + i % cardinality(name_stems)] || (array[' Feed and Grain', ' Seed Co.', ' Electric Co-op', ' Ag Repair', ' Farm Supply'])[1 + i % 5],
 (200 + i * 61 % 7000)::text || ' ' || street_names[1 + i % cardinality(street_names)],
 city,
 state,
 zip_code,
 area_code || '-555-01' || lpad((i * 7 % 100)::text, 2, '0'),
 'office' || i || '@example.com'
from generate_series(11, 100) as i
join Towns on town_id = i * 7 % 20
cross join Word_lists;

insert into Products (product_id, product_name, product_category, unit_of_measure, list_price)
select 10 + row_number() over (), product_name, product_category, unit_of_measure, list_price
from (values
 ('Cherry tomatoes', 'produce', 'lb', 3.25), ('Heirloom tomatoes', 'produce', 'lb', 3.75), ('Russet potatoes', 'produce', 'lb', 0.80), ('Red potatoes', 'produce', 'lb', 0.95),
 ('Yukon Gold potatoes', 'produce', 'lb', 1.10), ('Acorn squash', 'produce', 'lb', 1.25), ('Spaghetti squash', 'produce', 'lb', 1.30), ('Delicata squash', 'produce', 'lb', 1.60),
 ('Green cabbage', 'produce', 'lb', 0.70), ('Red cabbage', 'produce', 'lb', 0.85), ('Napa cabbage', 'produce', 'lb', 1.15), ('Bell peppers', 'produce', 'lb', 2.25),
 ('Jalapeno peppers', 'produce', 'lb', 2.75), ('Poblano peppers', 'produce', 'lb', 2.60), ('Yellow onions', 'produce', 'lb', 0.90), ('Red onions', 'produce', 'lb', 1.05),
 ('Sweet onions', 'produce', 'lb', 1.20), ('Carrots', 'produce', 'lb', 1.00), ('Green beans', 'produce', 'lb', 2.40), ('Sweet corn', 'produce', 'dozen', 6.00),
 ('Cucumbers', 'produce', 'lb', 1.35), ('Zucchini', 'produce', 'lb', 1.45), ('Spinach', 'produce', 'lb', 3.50), ('Kale', 'produce', 'lb', 3.25),
 ('Lettuce', 'produce', 'head', 2.00), ('Broccoli', 'produce', 'lb', 2.10), ('Cauliflower', 'produce', 'lb', 2.20), ('Beets', 'produce', 'lb', 1.30),
 ('Radishes', 'produce', 'bunch', 1.75), ('Pumpkins', 'produce', 'lb', 0.65),
 ('Soft red wheat', 'grain', 'bushel', 6.40), ('Durum wheat', 'grain', 'bushel', 8.20), ('White corn', 'grain', 'bushel', 5.10), ('Soybeans', 'grain', 'bushel', 11.30),
 ('Oats', 'grain', 'bushel', 4.20), ('Barley', 'grain', 'bushel', 5.50), ('Rye', 'grain', 'bushel', 6.10), ('Sorghum', 'grain', 'bushel', 5.20),
 ('Alfalfa hay', 'grain', 'ton', 210.00), ('Timothy hay', 'grain', 'ton', 240.00), ('Wheat straw', 'grain', 'ton', 120.00), ('Sunflower seed', 'grain', 'bushel', 9.75),
 ('Cornmeal', 'grain', 'lb', 1.10), ('Whole wheat flour', 'grain', 'lb', 1.35), ('Rolled oats', 'grain', 'lb', 1.50),
 ('Two percent milk', 'dairy', 'gallon', 5.00), ('Skim milk', 'dairy', 'gallon', 4.75), ('Heavy cream', 'dairy', 'quart', 5.50), ('Unsalted butter', 'dairy', 'lb', 6.25),
 ('Salted butter', 'dairy', 'lb', 6.40), ('Plain yogurt', 'dairy', 'quart', 4.80), ('Cottage cheese', 'dairy', 'lb', 3.90), ('Mozzarella', 'dairy', 'lb', 7.75),
 ('Gouda', 'dairy', 'lb', 9.25), ('Swiss cheese', 'dairy', 'lb', 9.00), ('Goat milk', 'dairy', 'gallon', 9.50), ('Goat cheese', 'dairy', 'lb', 13.50),
 ('Ribeye steak', 'meat', 'lb', 16.50), ('Sirloin steak', 'meat', 'lb', 12.75), ('Chuck roast', 'meat', 'lb', 8.25), ('Brisket', 'meat', 'lb', 9.50),
 ('Pork chops', 'meat', 'lb', 6.90), ('Pork shoulder', 'meat', 'lb', 5.25), ('Bacon', 'meat', 'lb', 8.40), ('Pork sausage', 'meat', 'lb', 6.10),
 ('Ham', 'meat', 'lb', 6.80), ('Whole chicken', 'meat', 'lb', 3.95), ('Chicken breast', 'meat', 'lb', 6.20), ('Chicken thighs', 'meat', 'lb', 3.80),
 ('Lamb chops', 'meat', 'lb', 15.25), ('Ground lamb', 'meat', 'lb', 10.50), ('Goat meat', 'meat', 'lb', 10.75),
 ('White eggs', 'eggs', 'dozen', 3.90), ('Free range eggs', 'eggs', 'dozen', 5.50), ('Duck eggs', 'eggs', 'dozen', 8.00), ('Quail eggs', 'eggs', 'dozen', 7.25),
 ('Jumbo brown eggs', 'eggs', 'dozen', 5.25), ('Medium white eggs', 'eggs', 'dozen', 3.50),
 ('Dairy heifer', 'livestock', 'head', 2100.00), ('Angus heifer', 'livestock', 'head', 1900.00), ('Angus bull', 'livestock', 'head', 4800.00), ('Bottle calf', 'livestock', 'head', 350.00),
 ('Feeder pig', 'livestock', 'head', 120.00), ('Breeding sow', 'livestock', 'head', 450.00), ('Market lamb', 'livestock', 'head', 240.00), ('Breeding ewe', 'livestock', 'head', 320.00),
 ('Dairy goat', 'livestock', 'head', 380.00), ('Meat goat', 'livestock', 'head', 260.00), ('Laying hen', 'livestock', 'head', 22.00), ('Broiler chick', 'livestock', 'head', 3.50)
) as t(product_name, product_category, unit_of_measure, list_price);

insert into Buildings (building_id, building_name, building_type, square_feet, capacity, capacity_unit, year_built, condition_status, farm_id)
select
 i,
 case when i % 17 = 0 then null
  else (array['North', 'South', 'East', 'West', 'Upper', 'Lower'])[1 + i % 6] || ' ' || building_type end,
 building_type,
 case building_type when 'barn' then 6000 + i * 83 % 10000 when 'silo' then 800 + i * 11 % 700 when 'greenhouse' then 2000 + i * 29 % 4000 when 'storage shed' then 3000 + i * 47 % 4000 else 1200 + i * 19 % 1800 end,
 case building_type when 'barn' then 40 + i * 7 % 130 when 'silo' then 10000 + i * 211 % 20000 when 'greenhouse' then 20 + i % 40 when 'storage shed' then 4 + i % 8 else 150 + i * 13 % 500 end,
 case building_type when 'barn' then 'animals' when 'silo' then 'bushels' when 'greenhouse' then 'tons' when 'storage shed' then 'machines' else 'animals' end,
 1960 + i * 41 % 64,
 (array['good', 'good', 'fair', 'good', 'poor'])[1 + i * 3 % 5],
 1 + i % 37
from generate_series(13, 100) as i
cross join lateral (select (array['barn', 'silo', 'greenhouse', 'storage shed', 'coop'])[1 + i % 5] as building_type) as types;

insert into Equipment (equipment_id, equipment_name, equipment_type, manufacturer, model, serial_number, purchase_date, purchase_price, condition_status, last_service_date, farm_id, building_id)
select
 i,
 (array['Main', 'North field', 'South field', 'East field', 'West field', 'Backup'])[1 + i % 6] || ' ' || equipment_type,
 equipment_type,
 manufacturer,
 model,
 upper(left(replace(manufacturer, ' ', ''), 3)) || '-' || lpad((i * 911 % 100000)::text, 5, '0'),
 purchase_date,
 round(base_price * (0.90 + (i % 5) * 0.05), 2),
 condition_status,
 case when condition_status = 'retired' then purchase_date + 200
  when i % 13 = 0 then null
  else date '2026-10-31' - i * 29 % 300 end,
 farm_id,
 case when equipment_type = 'irrigation' then null
  else (select min(building_id) from Buildings as b where b.farm_id = dates.farm_id and b.capacity_unit = 'machines') end
from generate_series(13, 100) as i
join Equipment_models on model_id = i % 16
cross join lateral (
 select
  1 + i % 37 as farm_id,
  date '2008-01-01' + i * 311 % 6500 as purchase_date,
  case when i % 11 = 0 then 'retired' when i % 7 = 0 then 'in repair' else 'operational' end as condition_status
) as dates;

insert into Animals (animal_id, species, breed, sex, birth_date, weight_lbs, health_status, acquisition_date, purpose, farm_id, building_id, move_in_date)
select
 i,
 species,
 breed,
 case when purpose in ('eggs', 'dairy') or i % 2 = 0 then 'female' else 'male' end,
 birth_date,
 round(base_weight * (0.85 + (i % 7) * 0.05), 2),
 case when i % 17 = 0 then 'sick' when i % 19 = 0 then 'injured' when i % 23 = 0 then 'under treatment' else 'healthy' end,
 birth_date + i % 60,
 purpose,
 farm_id,
 building_id,
 case when building_id is null then null else birth_date + i % 60 + i % 14 end
from generate_series(13, 100) as i
join Animal_breeds on breed_id = i % 12
cross join lateral (
 select
  1 + i % 37 as farm_id,
  date '2026-09-01' - (120 + i * 37 % max_age_days) as birth_date,
  (select min(b.building_id) from Buildings as b where b.farm_id = 1 + i % 37 and b.building_type = home_type) as building_id
) as details;

insert into Plantings (planting_id, field_number, acres_planted, planting_date, expected_harvest_date, actual_harvest_date, yield_amount, growth_status, farm_id, crop_id)
select
 i,
 1 + i % 20,
 acres_planted,
 planting_date,
 expected_harvest_date,
 case when expected_harvest_date + 5 <= date '2026-10-31' then expected_harvest_date + i % 6 end,
 case when expected_harvest_date + 5 > date '2026-10-31' then null
  when yield_unit = 'bushels' then acres_planted * (40 + i % 130)
  when yield_unit = 'tons' then acres_planted * (2 + i % 4)
  else acres_planted * (8000 + i * 7 % 22000) end,
 case when expected_harvest_date + 5 <= date '2026-10-31' then 'harvested'
  when date '2026-10-31' - planting_date >= 14 and crop_name <> 'Winter wheat' then 'growing'
  else 'planted' end,
 1 + i % 61,
 crop_id
from generate_series(13, 100) as i
join Crops on crop_id = 1 + i % (select count(*) from Crops)
cross join lateral (
 select
  5 + i * 13 % 200 + (i % 4) * 0.25 as acres_planted,
  case when crop_name = 'Winter wheat' then make_date(2025 + i % 2, 9, 20) + i % 30
   else make_date(2025 + i % 2, 4, 1) + i * 23 % 120 end as planting_date
) as planting
cross join lateral (
 select planting_date + case when crop_name = 'Winter wheat' then 240 + i % 30 else 80 + i % 70 end as expected_harvest_date
) as harvest;

insert into Workers (worker_id, first_name, last_name, job_title, hire_date, hourly_wage, employment_type, phone, email, farm_id)
select
 i,
 first_names[1 + i * 5 % cardinality(first_names)],
 last_names[1 + i * 3 % cardinality(last_names)],
 job_title,
 case when employment_type = 'seasonal' then date '2026-04-01' + i % 60
  else date '2005-01-01' + i * 113 % 7700 end,
 case job_title when 'manager' then 28.00 when 'mechanic' then 25.00 when 'equipment operator' then 22.00 when 'livestock handler' then 19.00 else 16.00 end + (i % 8) * 0.50,
 employment_type,
 area_code || '-555-01' || lpad((i * 9 % 100)::text, 2, '0'),
 lower(first_names[1 + i * 5 % cardinality(first_names)] || '.' || last_names[1 + i * 3 % cardinality(last_names)]) || i || '@example.com',
 1 + i % 61
from generate_series(13, 100) as i
join Towns on town_id = i % 20
cross join Word_lists
cross join lateral (
 select
  (array['field hand', 'livestock handler', 'field hand', 'equipment operator', 'field hand', 'livestock handler', 'mechanic', 'manager'])[1 + i % 8] as job_title,
  (array['full time', 'full time', 'part time', 'seasonal'])[1 + i * 3 % 4] as employment_type
) as jobs;

insert into Orders (order_id, order_date, delivery_date, order_status, payment_status, customer_id, farm_id)
select
 i,
 date '2026-10-30' - age_days,
 case when order_status = 'delivered' then date '2026-10-30' - age_days + 1 + i % 5
  when order_status = 'shipped' then date '2026-10-31' + 1 + i % 6 end,
 order_status,
 case when order_status = 'delivered' and i % 7 <> 0 then 'paid'
  when order_status = 'shipped' and i % 2 = 0 then 'paid'
  when order_status = 'pending' and i % 3 = 0 then 'paid'
  else 'unpaid' end,
 1 + i * 7 % 100,
 1 + i % 61
from generate_series(13, 100) as i
cross join lateral (select i * 17 % 360 as age_days) as ages
cross join lateral (
 select case when i % 13 = 0 then 'cancelled' when age_days < 20 then 'pending' when age_days < 45 then 'shipped' else 'delivered' end as order_status
) as statuses;

insert into Bills (bill_id, bill_category, issue_date, due_date, amount_due, farm_id, vendor_id)
select
 i,
 (array['feed', 'seed', 'utilities', 'repairs', 'supplies'])[1 + i % 5],
 date '2026-10-25' - i * 19 % 420,
 date '2026-10-25' - i * 19 % 420 + 30,
 (array[3000, 2500, 900, 1200, 600])[1 + i % 5] + i * 67 % 3000 + (i % 4) * 0.25,
 1 + i % 61,
 11 + (i % 5 + 4) % 5 + 5 * (i % 18)
from generate_series(13, 100) as i;

insert into Payments (payment_id, payment_date, payment_amount, payment_method, bill_id)
select
 10 + row_number() over (order by bill_id, part),
 least(issue_date + day_offset, date '2026-10-31'),
 amount,
 (array['cash', 'check', 'card', 'transfer'])[1 + bill_id % 4],
 bill_id
from (
 select bill_id, issue_date, 1 as part, 12 + bill_id % 15 as day_offset,
  case when bill_id % 2 = 1 then round(amount_due * 0.6, 2) else amount_due end as amount
 from Bills
 where bill_id > 12 and bill_id % 6 <> 0
 union all
 select bill_id, issue_date, 2, 30 + bill_id % 8, amount_due - round(amount_due * 0.6, 2)
 from Bills
 where bill_id > 12 and bill_id % 6 <> 0 and bill_id % 2 = 1
) as parts;

insert into Stocks (farm_id, product_id, quantity_on_hand)
select farm_id, 1 + (farm_id * 7 + k * 13) % 100, 20 + (farm_id * 97 + k * 41) % 4000
from generate_series(1, 61) as farm_id
cross join generate_series(0, 2) as k
on conflict do nothing;

insert into Contains (order_id, product_id, quantity, unit_price)
select
 o.order_id,
 p.product_id,
 case when c.customer_type = 'individual' or p.product_category = 'livestock' or p.unit_of_measure = 'ton' then 1 + o.order_id * p.product_id % 6
  else 20 + o.order_id * p.product_id * 31 % 480 end,
 round(p.list_price * case when c.customer_type = 'individual' then 1.00 else 0.90 + (o.order_id % 3) * 0.05 end, 2)
from Orders as o
join Customers as c on c.customer_id = o.customer_id
cross join lateral (
 select st.product_id
 from Stocks as st
 where st.farm_id = o.farm_id
 order by (st.product_id + o.order_id) % 7, st.product_id
 limit 1 + o.order_id % 3
) as picked
join Products as p on p.product_id = picked.product_id
where o.order_id > 12;

drop table Towns, Word_lists, Equipment_models, Animal_breeds;
