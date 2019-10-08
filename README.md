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

There is a view for the jobs currently being worked on that is connected to a working jobs table in the Cannabase, and a system to archive those jobs to long term archive tables.


[Home](http://StavromularBeta.github.io)