from faker import Faker
import pandas as pd
import random
import os

fake = Faker()
number_of_rows = 100000

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

printProgressBar(0, 10, prefix = 'Progress:', suffix = 'Complete', length = 50)

#customer demographics
customers = pd.DataFrame([[fake.first_name(), fake.last_name(), fake.address(), random.choice(["C", "I"]),random.choice(["Owner", "Manager", "Employee"]),fake.email(),fake.phone_number()] for _ in range(number_of_rows)], columns=['first_name', 'last_name', 'address', 'company_or_individual', 'role_in_company', 'email', 'phone'])
customers.index = [fake.uuid4() for _ in range(customers.shape[0])] 
customers.index.name = 'customer_id'

#products
products = pd.DataFrame([], columns=['name', 'description', 'type', 'available_quantity'])
products["name"] = ["gold ore", "gold bar", "copper ore", "copper conentrate", "iron ore", "iron pellets", "coal"]
products["description"] = ["Natural rock or sediment containing economically valuable concentrations of gold.", 
                           "Refined and solidified form of gold, often used as a store of value or for investment purposes.", 
                           "Rock or mineral from which copper can be extracted, typically containing various copper compounds.", 
                           "Product of the ore processing stage where copper is concentrated and separated from other minerals.", 
                           "Natural rock or mineral from which iron can be extracted and processed into iron and steel products.", 
                           " Small spheres or pellets of iron ore used in steelmaking processes for improved efficiency and handling.", 
                           " Combustible black or brownish-black sedimentary rock composed mostly of carbon, used as a fuel in power generation and industrial processes."]
products["type"] = ["raw material", "finished product", "raw material", "processed material", "raw material", "finished product", "raw material"]
products["available_quantity"] = [random.randint(1000, 100000) for _ in range(products.shape[0])]
products.index = [fake.uuid4() for _ in range(products.shape[0])] 
products.index.name = 'product_id'

#equipment
equipment = pd.DataFrame([], columns=['name',"description", 'type', 'quantity_owned', 'quantity_available'])
equipment["name"] = ["excavator", "dump truck", "dozer", "drill", "shovel", "crusher", "loader"]
equipment["description"] = ["Large, heavy-duty equipment used in mining to remove overburden or ore.",
                            "Large, heavy-duty truck used in mining to transport ore or waste material.",
                            "Large, heavy-duty equipment used in mining to push or remove overburden or ore.",
                            "Large, heavy-duty equipment used in mining to drill holes in the ground for blasting or exploration.",
                            "Large, heavy-duty equipment used in mining to remove overburden or ore.",
                            "Large, heavy-duty equipment used in mining to crush or break down large rocks into smaller pieces.",
                            "Large, heavy-duty equipment used in mining to load ore or waste material into trucks or conveyors."]
equipment["type"] = ["heavy equipment", "heavy equipment", "heavy equipment", "heavy equipment", "heavy equipment", "heavy equipment", "heavy equipment"]
equipment["quantity_owned"] = [random.randint(1, 10) for _ in range(equipment.shape[0])]
equipment["quantity_available"] = [random.randint(1, 10) for _ in range(equipment.shape[0])]
equipment.index = [fake.uuid4() for _ in range(equipment.shape[0])] 
equipment.index.name = 'equipment_id'

#contracts
contracts = pd.DataFrame([], columns=['customer_id', "product_or_equipment", "product_or_equipment_id", 'supply_fee', 'start_date', 'supply_period'])
contracts["customer_id"] = [random.choice(customers.index) for _ in range(number_of_rows//100)]
contracts["product_or_equipment"] = [random.choice(["P", "E"]) for _ in range(number_of_rows//100)]
contracts["product_or_equipment_id"] = [random.choice([random.choice(products.index),random.choice(equipment.index)]) for _ in range(number_of_rows//100)]
contracts["supply_fee"] = [random.randint(1000, 10000) for _ in range(number_of_rows//100)]
contracts["start_date"] = [fake.date_this_decade() for _ in range(number_of_rows//100)]
contracts["supply_period"] = [random.randint(1, 12) for _ in range(number_of_rows//100)]
contracts.index = [fake.uuid4() for _ in range(contracts.shape[0])] 
contracts.index.name = 'contract_id'

#sales
sales = pd.DataFrame([], columns=['customer_id', 'product_id', 'quantity', 'price_per_ounce', 'contract_details'])
sales["customer_id"] = [random.choice(customers.index) for _ in range(number_of_rows//100)]
sales["product_id"] = [random.choice(products.index) for _ in range(number_of_rows//100)]
sales["quantity"] = [random.randint(1, 100) for _ in range(number_of_rows//100)]
sales["price_per_ounce"] = [random.randint(1000, 10000) for _ in range(number_of_rows//100)]
sales["contract_details"] = [random.randint(1, contracts.shape[0]) for _ in range(number_of_rows//100)]
sales.index = [fake.uuid4() for _ in range(sales.shape[0])] 
sales.index.name = 'sale_id'

#leases
leases = pd.DataFrame([], columns=['customer_id', 'equipment_id', 'rental_fee_per_month', 'start_date', 'end_date', 'equipment_returned', 'contract_details'])
leases["customer_id"] = [random.choice(customers.index) for _ in range(number_of_rows//100)]
leases["equipment_id"] = [random.choice(equipment.index) for _ in range(number_of_rows//100)]
leases["rental_fee_per_month"] = [random.randint(1000, 10000) for _ in range(number_of_rows//100)]
leases["start_date"] = [fake.date_this_decade() for _ in range(number_of_rows//100)]
leases["end_date"] = [fake.date_this_decade() for _ in range(number_of_rows//100)]
leases["equipment_returned"] = [random.choice([True, False]) for _ in range(number_of_rows//100)]
leases["contract_details"] = [random.randint(1, contracts.shape[0]) for _ in range(number_of_rows//100)]
leases.index = [fake.uuid4() for _ in range(leases.shape[0])] 
leases.index.name = 'lease_id'

#consultations
consultations = pd.DataFrame([], columns=['customer_id', 'type', 'consultation_fee', 'operation_fee', 'consultation_completed', 'contract_details'])
consultations["customer_id"] = [random.choice(customers.index) for _ in range(number_of_rows//100)]
consultations["type"] = [random.choice(["geological surveys", "mine planning", "feasibility studies", "operational optimization", "safety training", "risk management assessments"]) for _ in range(number_of_rows//100)]
consultations["consultation_fee"] = [random.randint(1000, 10000) for _ in range(number_of_rows//100)]
consultations["operation_fee"] = [random.randint(1000, 10000) for _ in range(number_of_rows//100)]
consultations["consultation_completed"] = [random.choice([True, False]) for _ in range(number_of_rows//100)]
consultations["contract_details"] = [random.randint(1, contracts.shape[0]) for _ in range(number_of_rows//100)]
consultations.index = [fake.uuid4() for _ in range(consultations.shape[0])] 
consultations.index.name = 'consultation_id'

#communication channels
communication_channels = pd.DataFrame([], columns=['customer_id', 'email', 'text_messages', 'phone_calls', 'in_person_meetings', 'video_meetings'])
communication_channels["customer_id"] = [i for i in customers.index]
communication_channels["email"] = [random.choice([True, False]) for _ in range(number_of_rows)]
communication_channels["text_messages"] = [random.choice([True, False]) for _ in range(number_of_rows)]
communication_channels["phone_calls"] = [random.choice([True, False]) for _ in range(number_of_rows)]
communication_channels["in_person_meetings"] = [random.choice([True, False]) for _ in range(number_of_rows)]
communication_channels["video_meetings"] = [random.choice([True, False]) for _ in range(number_of_rows)]
communication_channels.index = [fake.uuid4() for _ in range(communication_channels.shape[0])]
communication_channels.index.name = 'communication_channel_id'

#billing plan
billing_plan = pd.DataFrame([], columns=['customer_id', 'invoice_frequency', 'payment_method'])
billing_plan["customer_id"] = [i for i in customers.index]
billing_plan["invoice_frequency"] = [random.choice(["monthly", "quarterly", "annually"]) for _ in range(number_of_rows)]
billing_plan["payment_method"] = [random.choice(["credit card", "ACH", "check"]) for _ in range(number_of_rows)]
billing_plan.index = [fake.uuid4() for _ in range(billing_plan.shape[0])] 
billing_plan.index.name = 'billing_plan_id'

#supply logistics
supply_logistics = pd.DataFrame([], columns=['customer_id', 'priority_level', 'shipping_method'])
supply_logistics["customer_id"] = [i for i in customers.index]
supply_logistics["priority_level"] = [random.choice(["high", "medium", "low"]) for _ in range(number_of_rows)]
supply_logistics["shipping_method"] = [random.choice(["self-pickup", "express shipping", "freight forwarding", "3rd party logistics"]) for _ in range(number_of_rows)]
supply_logistics.index = [fake.uuid4() for _ in range(supply_logistics.shape[0])] 
supply_logistics.index.name = 'supply_logistics_id'

#save data to csv files
os.makedirs("../data/abosso_goldfields_limited", exist_ok=True)

list_of_dataframes = [customers, products, equipment, contracts, sales, leases, consultations, communication_channels, billing_plan, supply_logistics]

for i, item in enumerate(list_of_dataframes):
    item.to_csv(f"../data/abosso_goldfields_limited/{item.index.name[:-3]}.csv")
    printProgressBar(i + 1, len(list_of_dataframes), prefix = 'Progress:', suffix = 'Complete', length = 50)

# customers.to_csv("data/abosso_goldfields_limited/customers.csv")
# products.to_csv("data/abosso_goldfields_limited/products.csv")
# equipment.to_csv("data/abosso_goldfields_limited/equipment.csv")
# contracts.to_csv("data/abosso_goldfields_limited/contracts.csv")
# sales.to_csv("data/abosso_goldfields_limited/sales.csv")
# leases.to_csv("data/abosso_goldfields_limited/leases.csv")
# consultations.to_csv("data/abosso_goldfields_limited/consultations.csv")
# communication_channels.to_csv("data/abosso_goldfields_limited/communication_channels.csv")
# billing_plan.to_csv("data/abosso_goldfields_limited/billing_plan.csv")
# supply_logistics.to_csv("data/abosso_goldfields_limited/supply_logistics.csv")
print("Data generated successfully!")
