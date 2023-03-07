# EventWave

## Vision
The purpose of this document is to specify the necessary features for a virtual event ticketing platform. This platform will facilitate the recording of event and customer information, as well as ticket management. Users will be able to add and edit details about events and customers, as well as manage ticket orders. The platform will provide a user-friendly experience, enabling organizers can manage the ticketing process with ease.

**Application should provide:**
- Storing ticket orders, customers and event details in a database;
- Display list of ticket orders;
- Updating the list of orders (adding, editing, removing);
- Display list of customers;
- Updating the list of customers (adding, editing, removing);
- Display list of events;
- Updating the list of events (adding, editing, removing);
- Filtering by ticket order date;
- Filtering by date for events.
   
## 1. Ticket orders
   
### 1.1. Display list of ticket orders.

The mode has been created to enable the viewing and editing of the order list and, if feasible, to exhibit the number of orders during a designated period.

***Main scenario:***
- User selects item “Ticket orders”; 
- Application displays list of ticket orders.
    
![](https://lh3.googleusercontent.com/mTH7aM9DJXtsU0RDO0TG5Ptc6mFFoaF0hIsciBYLJAPNVCWeJJ4MLOICxcI0Cy5OKMHAH53_NfBq7ntslMkP5Ga2lx3HiXNjhU3kVLh1SOQoapuFrx-_HZoBh0i7awd-9eNgZPgOUpu7SNXddi6ckHU)

*Pic. 1.1. Order list view.*

***The list displays the following columns:***
- Name and date – unique name and date of the event; 
- Cost – cost per ticket;
- Quantity – quantity of tickets purchased;
- Total cost – total cost, calculated by multiplying the cost per ticket by the quantity purchased; 
- Order date – the date on which the ticket/tickets were ordered; 
- Customer’s e-mail – customer’s unique e-mail address.
    
***Filterin by date:***
- The user selects a date filter and then clicks the "refresh list" button located to the right of the date entry field while in the list view mode; 
- A form will be presented by the application, showing the updated data of the order list for viewing.
    
***The following restrictions apply:***
- The start date must be earlier than the end date;
- If the start date is not provided, filtering will be based only on the end date;
- If the end date is not provided, filtering will be based only on the start date;
- To update data based on the filtering conditions, the user must click the "Refresh" button.
    
### 1.2. Add a new order.

***Main scenario:***
- To add a new order, the user have to click the "Add order" button in the ticket orders list view mode;
- The application will then display a form that allows the user to enter the required order data;    
- After entering the data, the user have to press the "Save" button;    
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;   
- If the entered data is valid, the application will add the new order record to the database;   
- If an error occurs during the addition of the new record, the application will display an error message;   
- If the new order record is successfully added to the database, the list of orders, including the newly added record, will be displayed to the user.
    
***Cancel operation scenario:***
- To add a new order, the user have to click the "Add order" button in the ticket orders list view mode;    
- The application will then display a form that allows the user to enter the required order data;    
- If the user enters order data but clicks the "Cancel" button, the data is not saved in the database;    
- The application displays the list of order records to the user;    
- If the user selects either the "List of customers" or "List of events" page when adding a new order, the corresponding data form will open without being saved new data to the database.
    
![](https://lh6.googleusercontent.com/80zFE2C0V8UkGlSU32S75_-JtohCyjj_SPYoYGWAZQwHKRhl3Clq1vNMHJm8uRTkl_3QmJJrZa0oQoLwfiE3OYnWWFv_Zktm65kX5VTsITckdDg6v8sPnyIY0_ckDsp_BpjTXPaqeR1gRMI7l2MwlfA)

*Pic. 1.2. View of the window for adding a new order.*

***When adding an order, the following details are entered:***
- Choose date – the date of the event;
- Choose event – the name of the event;    
- Quantity of tickets – quantity of tickets purchased;    
- Cost of ticket – cost per ticket;    
- Order date – the date on which the ticket/tickets were ordered;    
- E-mail – customer’s unique e-mail address.
    
***Constraints for data validation:***
- Choose date –should not be left blank and should be in the format "dd/mm/yyyy";    
- Choose event – the user should select an event from a predetermined list of options. The format should match the pre-defined event names;    
- Quantity of tickets – should not be left blank and should be represented by a whole number. No decimal values or negative numbers are allowed. The maximum order quantity is 20 tickets;    
- Cost of ticket – should not be left blank and should be represented as a decimal number with two decimal places. For example, "15.99";    
- Order date – should not be left blank andshould be in the format "dd/mm/yyyy";    
- E-mail – should not be left blank and should follow the standard e-mail format, with a valid username, followed by the "@" symbol, and then the domain name. For example, "example123@gmail.com". The allowable length of input is between 6 to 50 characters.
    
### 1.3. Edit the order.

***Main scenario:***
- To edit the order, the user have to click the "Edit" button in the ticket orders list view mode;    
- The application will then display a form that allows the user to change the order data;    
- After entering the data, the user have to press the "Save" button;    
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;    
- If the entered data is valid, the application will add the edited order record to the database;    
- If an error occurs while trying to change a record, the program will issue an error message;    
- If the modified order record is successfully added to the database, the user will be shown a list of orders including the newly edited record.
    
***Cancel operation scenario:***
- To edit the order, the user have to click the "Edit" button in the ticket orders list view mode;    
- The application will then display a form that allows the user to change order data;    
- If the user enters order data but clicks the "Cancel" button, the changed data is not saved in the database;    
- The application displays the list of order records to the user;    
- When the user selects either the "List of customers" or "List of events" page when editing the order , the corresponding data form will open without being saved edited data to the database.
    
![](https://lh3.googleusercontent.com/ZinnWBf60T5ks-9iTFzkXMY73NdphHwo-WjierZJiPhBLEjDnOGfDcKJv7bhLUJ74qT2vonM_87i8sxdrWXgcs6vBZIhvPS6o5JIROJdEk-YEIuKEW2Tx163cBQPlbD_vl-mbQffhU6h_NFSMDta11g)

*Pic. 1.3. View of the order editing window.*

***When editing the order, the following details may be changed:***
- Quantity of tickets – quantity of tickets purchased;   
- Cost of ticket – cost per ticket;  
- Order date – the date on which the ticket/tickets were ordered;   
- E-mail – customer’s unique e-mail address.
The “Choose date” and “Choose event” fields are disabled for editing.

***The  validation process*** for adding a new order is also applied to all active fields when editing the order.

### 1.4. Remove order.

***Main scenario:***
- When the user is viewing the list of orders, they can select a specific order and click the "Delete" button;    
- If the order can be deleted, a confirmation dialog will appear;    
- The user can confirm the removal;    
- After confirmation, the record is deleted from the database;    
- If an error occurs during the deletion process, an error message is displayed;    
- If the order is successfully deleted, the list of orders is refreshed and displayed without the deleted record.
    
***Cancel operation scenario:***
- When the user is viewing the list of orders, they can click the "Delete" button to delete the order;    
- If the user decides not to delete the order, they can click the "Cancel" button in the confirmation dialog or click the cross in the upper right corner of the dialog box;    
- After clicking "Cancel," the list of orders is refreshed and displayed without any changes.
    
![](https://lh6.googleusercontent.com/M4AGxN7r_l8T3HqwwrkAhlozX4fwq9jtKMeYu1FbAubN2WDFaRZPJky01v73QatCMgHh2bp9-ADbO6CnQBHu3DISsk5Jo2feczD7oPByS7ld5mQaeVdy0Q7d-aqlWp7UUyB669BInHrMawjcztxlLzc)

*Pic. 1.4. Remove order dialog.*

## 2. Event details
    
### 2.1. Display list of event details.

This mode has been developed to display and modify the list of events and, where possible, to show the number of events within a specified time frame.

**Main scenario:**
- User selects item “List of events”;    
- Application displays list of events.
    
![](https://lh4.googleusercontent.com/Eru1pkx-IHgqFB-rUGhxixyybyylug2cDVab2mUCW1o1YyryGJwnoYuoBBziEW6zU4OrSdQMrApif8DQ-1MRWDaMURkFQCtYrrM5gCefd-9_Fc4Mux84slEPkMllTEXSTmH5F-3Axqo62C-0mlhrwog)

*Pic. 2.1. Event list view.*

**The list displays the following columns:**
- Name – name of the event;    
- Date – the date on which the event will take place;    
- Time – the time at which the event will start;    
- City – the city where the event will take place;    
- Location – the specific location where the event will take place;    
- Availability – the number of seats or spaces that are available for the event.
    
**Filterin by date:**
-   The user selects a date filter and then clicks the "refresh list" button located to the right of the date entry field while in the list view mode;   
-   A form will be presented by the application, showing the updated data of the list of events for viewing.

**The following restrictions apply:**
- The start date must be earlier than the end date;   
- If the start date is not provided, filtering will be based only on the end date;    
- If the end date is not provided, filtering will be based only on the start date;   
- To update data based on the filtering conditions, the user must click the "Refresh" button.
    
### 2.2. Add new event.

**Main scenario:**
- To add a new event, the user have to click the "Add event" button in the list of events view mode;    
- The application will then display a form that allows the user to enter the required event data;  
- After entering the data, the user have to press the "Save" button;   
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;  
- If the entered data is valid, the application will add the new event record to the database;    
- If an error occurs during the addition of the new record, the application will display an error message;   
- If the new event record is successfully added to the database, the list of events, including the newly added record, will be displayed to the user.
    
**Cancel operation scenario:**
- To add a new event, the user have to click the "Add event" button in the list of events view mode;   
- The application will then display a form that allows the user to enter the required event data;   
- If the user enters event data but clicks the "Cancel" button, the data is not saved in the database;   
- The application displays the list of event records to the user;  
- When the user selects either the "List of customers" or "Ticket orders" page when adding the event , the corresponding data form will open without being saved a new data to the database.
    
![](https://lh6.googleusercontent.com/HNiJ3hKfmocu3TT1EHCmygmSmtx_G13IhE1OENpyCz9NpwgzMzFSoYRnDQSWMLV2QpvEdZElTR6SElaD1wfLLDNfQS3Bp2J6yOCeshM60s24txuBl-coRYAqzDEGSEdSqK--6gSWfWpxlGHM9H_P0Bs)

*Pic. 2.2. View of the window for adding a new event.*

**When adding an event, the following details are entered:**
- Name – name of the event;    
- Date – the date on which the event will take place;    
- Time – the time at which the event will start;    
- City – the city where the event will take place;   
- Location – the specific location where the event will take place;   
- Availability – the number of seats or spaces that are available for the event.
    
**Constraints for data validation:**
- Name – should not be left blank and should be between 3 to 50 characters long; 
- Date – should not be left blank and should be in the format "dd/mm/yyyy";   
- Time – cannot be left blank and should be in a valid time format “hh:mm”;    
- City – should not be left blank and should be between 3 to 50 characters long;    
- Location – should not be left blank and should be between 3 to 50 characters long;    
- Availability – should be a numeric value that indicates the number of seats or spaces available for the event, should not be left blank and should not contain any special characters.
    
### 2.3. Edit the event.

**Main scenario:**
- To edit the event, the user have to click the "Edit" button in the list of events view mode;    
- The application will then display a form that allows the user to change the event data;    
- After entering the data, the user have to press the "Save" button;    
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;    
- If the entered data is valid, the application will add the edited event record to the database;    
- If an error occurs while trying to change a record, the program will issue an error message;    
- If the modified event record is successfully added to the database, the user will be shown a list of events including the newly edited record.
    
**Cancel operation scenario:**
- To edit the event, the user have to click the "Edit" button in the list of events view mode;    
- The application will then display a form that allows the user to change event data;    
- If the user enters event data but clicks the "Cancel" button, the changed data is not saved in the database;    
- The application displays the list of event records to the user;    
- When the user selects either the "List of customers" or "Ticket orders" page when editing the event , the corresponding data form will open without being saved edited data to the database.
    
![](https://lh6.googleusercontent.com/6FLjy_6FMoZ3mIOZvsLqIVC2RfeAnF7hUeuv-iDzWCJdLwo0koxmwaygMpTCJ2z-sBmatdpNw0E5j_7XW9xCYferQMvggTrSJkeba2hR2cf1XzAFVW1cztgdFKM2L1S8BFPgz6qBo5Puc7HTF9hP_nw)

*Pic 2.3. View of the event editing window.*

**When editing the event, the following details may be changed:**
- Name – name of the event;    
- Date – the date on which the event will take place;    
- Time – the time at which the event will start;    
- City – the city where the event will take place;    
- Location – the specific location where the event will take place;    
- Availability – the number of seats or spaces that are available for the event.
    
**The validation process** for adding the event is also applied to all fields when editing the event. 

### 2.4. Remove event.

**Main scenario:**
- When the user is viewing the list of events, they can select a specific event and click the "Delete" button;    
- If the event can be deleted, a confirmation dialog will appear;    
- The user can confirm the removal;    
- After confirmation, the record is deleted from the database;    
- If an error occurs during the deletion process, an error message is displayed;  
- If the event is successfully deleted, the list of eventss is refreshed and displayed without the deleted record.
    
**Cancel operation scenario:**
- When the user is viewing the list of events, they can click the "Delete" button to delete the event;    
- If the user decides not to delete the event, they can click the "Cancel" button in the confirmation dialog or click the cross in the upper right corner of the dialog box;    
- After clicking "Cancel," the list of events is refreshed and displayed without any changes.
    
![](https://lh5.googleusercontent.com/s1WOEDJMEVOmHv0i-kVn6UcWkiSzJOBUPW-1fjyYONWIocWVWqXeGjE_LT9Hqb9GV33Eo98zYZxucms4Jd1kPrKv6nHpVrb5D2AsLx0NJy1m74G9A3sB1sGRfOYU6ZWsT-_5HIZmnyn6Iq1wubERFqc)

*Pic. 2.4 Remove event dialog.*

## 3. Customers
    
### 3.1. Display list of customers.

This mode has been developed to display and modify the list of customers.

**Main scenario:**
- User selects item “List of customers”;   
- Application displays list of customers.
    
![](https://lh3.googleusercontent.com/IdPL0ET4iesBv-0gj0rrXROlOAajk1Mh3PyhGdlsB-AcqfhpImUwT9sfYqGJ5J5OsN4NDuSWJcb5wH8BgioHwSfA-Ysla_gokIZfCg_I3BhXGPahio7AW9SD6Ic8BqTWUFndI4WnccgeFJvcPwwEI2c)

*Pic. 3.1. Customers list view.*

**The list displays the following columns:**
- Name – name of the customer;    
- Phone number – the customer's unique phone number;    
- E-mail – the customer’s unique e-mail address.
    
### 3.2. Add new customer.

**Main scenario:**
- To add a new customer, the user have to click the "Add customer" button in the list of customers view mode;    
- The application will then display a form that allows the user to enter the required customer data;    
- After entering the data, the user have to press the "Save" button;    
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;    
- If the entered data is valid, the application will add the new customer record to the database;    
- If an error occurs during the addition of the new record, the application will display an error message;    
- If the new customer record is successfully added to the database, the list of customers, including the newly added record, will be displayed to the user.
    
**Cancel operation scenario:**
-   To add a new customer, the user have to click the "Add customer" button in the list of customers view mode;    
-   The application will then display a form that allows the user to enter the required customer data;    
-   If the user enters required customer data but clicks the "Cancel" button, the data is not saved in the database;    
-   The application displays the list of customer records to the user;    
-   When the user selects either the "List of events" or "Ticket orders" page when adding the customer , the corresponding data form will open without being saved a new data to the database.
    
![](https://lh4.googleusercontent.com/PeVUkp6P0B3Cig5J6xoVCI19RAG4f8dav3x6XQdCi4mnlKNMZF9Z6ZaG8w4hCLp_nX_1EV49_V42mSVMBxwrg_zQ_8v40NNFMY5zD-TVvaA4l2uNqQRilUQh-Ij13o9-WABUvLPsNjn09cAWkIHYOAM)

*Pic. 3.2. View of the window for adding a new customer.*

**When adding an order, the following details are entered:**
- Name – the customer’s name;    
- E-mail – the customer’s unique e-mail address;    
- Phone number – customer’s unique phone number.
    
**Constraints for data validation:**
- Name – should not be left blank and should be between 3 to 50 characters long;    
- E-mail – should not be left blank and should follow the standard e-mail format, with a valid username, followed by the "@" symbol, and then the domain name. For example, <example123@gmail.com>. The allowable length of input is between 3 to 50 characters; 
- Phone number - this field must not be left blank and must contain a valid phone number format. Input data can only contain numbers and the "+" symbol, with no spaces. The acceptable input length is from 10 to 12 characters.
    
### 3.3. Edit the customer.

**Main scenario:**
- To edit the customer, the user have to click the "Edit" button in the list of customers view mode;    
- The application will then display a form that allows the user to change the customer data;    
- After entering the data, the user have to press the "Save" button;    
- If any data is entered incorrectly, the application will display an error message indicating the incorrect data;    
- If the entered data is valid, the application will add the edited customer record to the database;    
- If an error occurs while trying to change a record, the program will issue an error message;    
- If the modified customer record is successfully added to the database, the user will be shown a list of customers including the newly edited record.
    
**Cancel operation scenario:**
- To edit the customer, the user have to click the "Edit" button in the list of customers view mode;    
- The application will then display a form that allows the user to change customer data;    
- If the user enters customer data but clicks the "Cancel" button, the changed data is not saved in the database;   
- The application displays the list of customer records to the user;    
- When the user selects either the "List of events" or "Ticket orders" page when editing the customer, the corresponding data form will open without being saved edited data to the database.
    
![](https://lh4.googleusercontent.com/DqpnJPpICUeb_gaCvo5-eNqnY-cpCTSlv_IQ2a36YH8Mk42NTm6xC403kAe7dMjz66ppc9HdUGvAEgC_R4v2RMIlTtRyBj4DGJVZEY8TK-1pu7SfopgPedgitNEFx4ly-PArvODx3-VSpHld0YsoQ8Y)

*Pic. 3.3. View of the customer editing window.*

**When editing the customer, the following details may be changed:**
- Name – the customer’s name;    
- E-mail – the customer’s unique e-mail address;    
- Phone number – customer’s unique phone number.
    
**The validation process** for adding the event is also applied to all fields when editing the event.

### 3.4. Remove customer.

**Main scenario:**
- When the user is viewing the list of customers, they can select a specific customer and click the "Delete" button;   
- If the event can be deleted, a confirmation dialog will appear;    
- The user can confirm the removal;    
- After confirmation, the record is deleted from the database;    
- If an error occurs during the deletion process, an error message is displayed;    
- If the event is successfully deleted, the list of eventss is refreshed and displayed without the deleted record.
    
**Cancel operation scenario:**
-   When the user is viewing the list of customers, they can click the "Delete" button to delete the customer;    
- If the user decides not to delete the customer, they can click the "Cancel" button in the confirmation dialog or click the cross in the upper right corner of the dialog box;   
- After clicking "Cancel," the list of customers is refreshed and displayed without any changes.
    
![](https://lh3.googleusercontent.com/zjFt_03MbPOlrhGa2SB11MMcWGdq5VXvFMwZDRd3AP2e6mk1pgJ-8dH-jBlZQo6-Py0y2AXzM82qm9Hd3BPf2gazE1RuMicrshMDo6HS73x-RsXiwceLMdxBf9Byyh25yXLL5zwOPwFbGyVvbiZtcWg)

*Pic. 3.4. Remove customer dialog.*
