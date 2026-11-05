# Naming: <page file or helpers.py function>_<variable the result is assigned to>.
# Queries with {where} are filled in with where_clause(conditions).


# helpers.py: farm_labels()

farm_labels_farms = """
    select farm_id, farm_name
    from Farms
    order by farm_name
"""


# helpers.py: building_labels()

building_labels_buildings = """
    select building_id, coalesce(building_name, building_type) as label
    from Buildings
    where farm_id = %s
    order by label
"""


# helpers.py: distinct_values()
# {column} and {table} are filled in by distinct_values(column, table).

distinct_values_values = """
    select distinct {column}
    from {table}
    order by {column}
"""


# helpers.py: crop_varieties()

crop_varieties_varieties = """
    select distinct variety
    from Crops
    where crop_name = %s
    order by variety
"""


# pages/overview.py

overview_bills = """
    select coalesce(sum(b.amount_due - coalesce(p.paid, 0)), 0) as owed,
           count(*) filter (where b.due_date < current_date) as past_due
    from Bills b
    left join (select bill_id, sum(payment_amount) as paid from Payments group by bill_id) p
        on p.bill_id = b.bill_id
    where b.amount_due > coalesce(p.paid, 0)
"""

overview_orders_to_ship = """
    select count(*) as total
    from Orders
    where order_status = 'pending'
"""

overview_fields_to_harvest = """
    select count(*) as total
    from Plantings
    where growth_status <> 'harvested'
        and expected_harvest_date >= current_date
        and expected_harvest_date <= current_date + 14
"""

overview_animals_needing_care = """
    select count(*) as total
    from Animals
    where health_status <> 'healthy'
"""

overview_harvests = """
    select f.farm_name as "Farm",
           p.field_number as "Field",
           c.crop_name || ', ' || c.variety as "Crop",
           p.acres_planted as "Acres",
           p.expected_harvest_date as "Harvest date"
    from Plantings p
    join Farms f on f.farm_id = p.farm_id
    join Crops c on c.crop_id = p.crop_id
    where p.growth_status <> 'harvested'
        and p.expected_harvest_date >= current_date
        and p.expected_harvest_date <= current_date + 14
    order by p.expected_harvest_date
"""

overview_sales = """
    select cu.customer_type as "Customer type",
           sum(c.quantity * c.unit_price) as "Total sales"
    from Orders o
    join Customers cu on cu.customer_id = o.customer_id
    join Contains c on c.order_id = o.order_id
    where o.order_status = 'delivered'
    group by cu.customer_type
"""


# pages/fields.py

fields_plantings = """
    select f.farm_name as "Farm",
           p.field_number as "Field",
           c.crop_name || ', ' || c.variety as "Crop",
           p.acres_planted as "Acres",
           p.planting_date as "Planted",
           p.expected_harvest_date as "Harvest date",
           p.growth_status as "Status"
    from Plantings p
    join Farms f on f.farm_id = p.farm_id
    join Crops c on c.crop_id = p.crop_id
    {where}
    order by f.farm_name, p.field_number
"""

fields_crops = """
    select crop_id, crop_name || ', ' || variety as label
    from Crops
    order by label
"""

fields_inserted = """
    insert into Plantings (planting_id, field_number, acres_planted, planting_date,
                           expected_harvest_date, growth_status, farm_id, crop_id)
    select coalesce(max(planting_id), 0) + 1, %s, %s, %s, %s, 'planted', %s, %s
    from Plantings
"""


# pages/crops.py

crops_acres = """
    select f.farm_name as "Farm",
           c.crop_name as "Crop",
           c.variety as "Variety",
           sum(p.acres_planted) as "Acres"
    from Plantings p
    join Farms f on f.farm_id = p.farm_id
    join Crops c on c.crop_id = p.crop_id
    {where}
    group by f.farm_name, c.crop_name, c.variety
    order by f.farm_name, c.crop_name, c.variety
"""


# pages/livestock.py

livestock_animals = """
    select f.farm_name as "Farm",
           a.species as "Species",
           a.breed as "Breed",
           count(*) as "Animals"
    from Animals a
    join Farms f on f.farm_id = a.farm_id
    {where}
    group by f.farm_name, a.species, a.breed
    order by f.farm_name, a.species, a.breed
"""

livestock_inserted = """
    insert into Animals (animal_id, species, breed, sex, birth_date, weight_lbs, health_status,
                         acquisition_date, purpose, farm_id, building_id, move_in_date)
    select coalesce(max(animal_id), 0) + 1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    from Animals
"""


# pages/equipment.py

equipment_equipment_rows = """
    select f.farm_name as "Farm",
           e.equipment_id as "ID",
           e.equipment_name as "Equipment",
           e.equipment_type as "Type",
           e.manufacturer as "Manufacturer",
           e.model as "Model",
           e.serial_number as "Serial number",
           e.purchase_date as "Purchased",
           e.purchase_price as "Price",
           e.condition_status as "Condition",
           e.last_service_date as "Last service"
    from Equipment e
    join Farms f on f.farm_id = e.farm_id
    {where}
    order by f.farm_name, e.equipment_id
"""

equipment_inserted = """
    insert into Equipment (equipment_id, equipment_name, equipment_type, manufacturer, model,
                           serial_number, purchase_date, purchase_price, condition_status,
                           last_service_date, farm_id, building_id)
    select coalesce(max(equipment_id), 0) + 1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    from Equipment
"""


# pages/workers.py

workers_worker_names = """
    select worker_id, first_name || ' ' || last_name as label
    from Workers
    order by label
"""

workers_worker_rows = """
    select f.farm_name as "Farm",
           w.worker_id as "ID",
           w.first_name as "First name",
           w.last_name as "Last name",
           w.job_title as "Job title",
           w.hire_date as "Hired",
           w.hourly_wage as "Hourly wage",
           w.employment_type as "Employment type",
           w.phone as "Phone",
           w.email as "Email"
    from Workers w
    join Farms f on f.farm_id = w.farm_id
    {where}
    order by f.farm_name, w.worker_id
"""

workers_inserted = """
    insert into Workers (worker_id, first_name, last_name, job_title, hire_date, hourly_wage,
                         employment_type, phone, email, farm_id)
    select coalesce(max(worker_id), 0) + 1, %s, %s, %s, %s, %s, %s, %s, %s, %s
    from Workers
"""


# pages/sales.py

sales_sales_rows = """
    select f.farm_name as "Farm",
           cu.customer_type as "Customer type",
           count(distinct o.order_id) as "Orders",
           sum(c.quantity * c.unit_price) / count(distinct o.order_id) as "Average order",
           sum(c.quantity * c.unit_price) as "Total sales"
    from Orders o
    join Farms f on f.farm_id = o.farm_id
    join Customers cu on cu.customer_id = o.customer_id
    join Contains c on c.order_id = o.order_id
    join Products p on p.product_id = c.product_id
    {where}
    group by f.farm_name, cu.customer_type
    order by "Total sales" desc
"""


# pages/products.py

products_stock_rows = """
    select f.farm_name as "Farm",
           p.product_name as "Product",
           p.product_category as "Category",
           p.unit_of_measure as "Unit",
           p.list_price as "List price",
           s.quantity_on_hand as "On hand"
    from Stocks s
    join Farms f on f.farm_id = s.farm_id
    join Products p on p.product_id = s.product_id
    {where}
    order by f.farm_name, p.product_name
"""
