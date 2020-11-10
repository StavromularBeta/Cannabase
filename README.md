# Cannabase

Cannabase is a TKinter window to a sqlite database. This database can be used to keep track of submitted jobs to an analytical laboratory.

The following is tracked for each work order:
* Job ID
* Customer Name
* Type of Testing Required
* Recieve Date
* Complete Date
    * Both of the overall job, and the individual tests in the job.
* Job Status (Complete or Incomplete)
* Job Notes
    * Can be added to throughout the analytical process.
* Photos of the sample being analyzed
* Analytical data
    * View basic, text based potency reports at the job page level
    * Links to scanned bench sheet pdf's, which open in your default PDF viewer
    * Links to scanned report good copies, which open in your default PDF viewer

Work orders are placed into an "active jobs" table. When they have been marked as complete, they are archived. Both active and archived jobs 
can be searched independently.
    * You can search by Customer Name or Jobnumber. Additionally, there are a series of filters for the various tests - can select whatever tests 
    you want, and then hit (ONLY/OR/AND) to search. 

Customers are tracked by the database - you can search through all customers, and view all of a customer's jobs on a given "customer page".
You can click on the individual jobs to go to their "job pages", and can click on the customer name on the "job page" to go back to the 
"customer page".






[Home](http://StavromularBeta.github.io)