# phillycourtdockets
Code for scraping and analyzing Philadelphia court docket data.

There are a bunch of court dockets at this website:
https://ujsportal.pacourts.us/DocketSheets/CP.aspx

For example:
https://ujsportal.pacourts.us/DocketSheets/CPReport.ashx?docketNumber=CP-51-CR-0000862-2013

Ryan Briggs, Philadelphia journalist, is particularly interested in the ~15k dockets with the numbers
CP-51-CR-######-2015

He's interested in searching through these for all kinds of potential articles, so getting the text into a database with some metadata seems like it would be really helpful and then one could do all kinds of things.

Has a friend who wrote some similar code:
http://pastebin.com/C7M96KUN


## TODO
* create an AWS server with a MySQL database
* read ~5 dockets into the MySQL database... docket number and raw text from "Charges" section.

