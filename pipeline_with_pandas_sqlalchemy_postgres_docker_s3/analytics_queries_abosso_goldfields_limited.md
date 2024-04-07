### 10 analytics questions about the company data, along with SQL queries that can answer them:

1. **Customer Demographics:**

   - Question: How many customers are there in each company role category?

   ```sql
   SELECT role_in_company, COUNT(*) AS count_customers
   FROM customers
   GROUP BY role_in_company;
   ```

2. **Products:**

   - Question: What is the total available quantity for each product type?

   ```sql
   SELECT type, SUM(available_quantity) AS total_available_quantity
   FROM products
   GROUP BY type;
   ```

3. **Equipment:**

   - Question: How many units of each type of equipment do we own and have available?

   ```sql
   SELECT type, SUM(quantity_owned) AS total_owned, SUM(quantity_available) AS total_available
   FROM equipment
   GROUP BY type;
   ```

4. **Contracts:**

   - Question: What is the average supply fee per contract type (product or equipment)?

   ```sql
   SELECT product_or_equipment, AVG(supply_fee) AS average_supply_fee
   FROM contracts
   GROUP BY product_or_equipment;
   ```

5. **Sales:**

   - Question: What is the total revenue generated from product sales for each customer?

   ```sql
   SELECT s.customer_id, c.first_name, c.last_name, SUM(s.quantity * s.price_per_ounce) AS total_revenue
   FROM sales s
   JOIN customers c ON s.customer_id = c.customer_id
   GROUP BY s.customer_id, c.first_name, c.last_name;
   ```

6. **Leases:**

   - Question: How many leases are active and how many have been returned for each type of equipment?

   ```sql
   SELECT e.type,
          SUM(CASE WHEN l.equipment_returned = FALSE THEN 1 ELSE 0 END) AS active_leases,
          SUM(CASE WHEN l.equipment_returned = TRUE THEN 1 ELSE 0 END) AS returned_leases
   FROM leases l
   JOIN equipment e ON l.equipment_id = e.equipment_id
   GROUP BY e.type;
   ```

7. **Consultations:**

   - Question: What is the total fee earned from completed consultations for each consultation type?

   ```sql
   SELECT type, SUM(consultation_fee + operation_fee) AS total_fee_earned
   FROM consultations
   WHERE consultation_completed = TRUE
   GROUP BY type;
   ```

8. **Communication Channels:**

   - Question: How many customers prefer each communication channel?

   ```sql
   SELECT
       SUM(CASE WHEN email = TRUE THEN 1 ELSE 0 END) AS email_preference,
       SUM(CASE WHEN text_messages = TRUE THEN 1 ELSE 0 END) AS text_messages_preference,
       SUM(CASE WHEN phone_calls = TRUE THEN 1 ELSE 0 END) AS phone_calls_preference,
       SUM(CASE WHEN in_person_meetings = TRUE THEN 1 ELSE 0 END) AS in_person_meetings_preference,
       SUM(CASE WHEN video_meetings = TRUE THEN 1 ELSE 0 END) AS video_meetings_preference
   FROM communication_channels;
   ```

9. **Billing Plan:**

   - Question: What is the distribution of payment methods among customers?

   ```sql
   SELECT payment_method, COUNT(*) AS count_customers
   FROM billing_plan
   GROUP BY payment_method;
   ```

10. **Supply Logistics:**
    - Question: How many customers prefer each shipping method?
    ```sql
    SELECT shipping_method, COUNT(*) AS count_customers
    FROM supply_logistics
    GROUP BY shipping_method;
    ```

These queries should provide insightful analytics into various aspects of your data related to customers, products, contracts, sales, equipment, consultations, communication channels, billing plans, and supply logistics.
