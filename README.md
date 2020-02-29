# Stock Price Accumulator
This is a Python Script to accumulate stock prices of multiple companies by minutes.

<b>Problem Statement:</b>
I was trying to build a sequence model to predict stock price of a company, when I began searching for data I realized that the online APIs such as Yahoo Finance & Google Finance allow for only upto 30 days previous minute level data at a maximum. Therefore if I were to use one of these APIs my data would be only constrained to 30 days and this was a very small amount of data to build a sequence model and the resulting model would be far from robust. Alternative was to manually update the datase daily or weekly atleast which was a very tedious task.

<b>Solution:</b>
Inorder to tackle the above issue I wrote a python script which would automatically collect the data daily for the listed companies after end of each trading day, process it and save it to the local.

<b>Challenges:</b>
The major challenge was the pivot table we would get from Yahoo Finance API. I unpivoted the table and rectified the column names. Another challenge was at given point you can only request for 7 days of data, so this had to be managed approriately by dynamically making calls as required.

<b>Scope:</b>
Right now I return only the Close & the Volume column but one can easily add columns if they want by modifying the code. Further I have restricted last update to previous day so that we have full clean data upto that particular day instead of live update. If one contines to accumulate data for next 30 working days he/she would have added 11700 rows to the original dataset. Although the process of collecting data may seem slower for someone who wants to start working instantly on the dataset, but the alternative is he/she has to work on either 30 days of data or bets that someone is accumulating minute level data for their preferred company.

<b>Potential Issues</b>
Scalability - Right now up to 10 companies data can be easily collected & maintained, it is possible that it may work  for more than 10 companies also but over a period of time I am not sure if it'll work smoothly. Further if the number of companies are large may be we can call the program twice separately for each list of companies.

<b>How to use:</b>
1. Download or copy create both py files and make sure they're in the same directory.
2. In the Accumulate Stock Price file add the name of the companies for which you want to accumulate data.
3. In the Accumulate Stock Price file add the local path where you want to save your excel file.
4. Create a daily task and execute the script using the windows task scheduler.

<b>Future Work:</b>
1. Broaden the scope i.e. include for more intervals rather than just minute level data
2. Alllow user to choose their own columns instead of returning "Close" & "Volume" by default.

<b>Citations:</b>
1. This code was developed using Spyder IDE
2. Publicly available <a href="https://github.com/ranaroussi/yfinance">Yahoo Finance API</a> is used to accumulate the data.
