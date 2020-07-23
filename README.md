# Scraping E-Mail adresses from LinkedIn

Python selenium project whicih logins to the LinkedIn website and goes directly to the profile page of the given user. Then scrapes the e-mail address and saves it to the email_address.txt file.

This is a small prototyp. Below actions will be taken in the production phase:

* Reading users from given input file
* removing sleep() codes
* Converting in to functions
* Login credentials will be read from a config file
* Automatically direct contact details page with reading given input file. whicih removes the hardcoded broswer destinations.

# Running
This script is written with Python3 and Selenium.

install requirements via below command:

```shell
 pip install -r requirements.txt
```

Update username and password in the scrapper.py file.

Then run below command to execute the script.
```shell
 python scrapper.py
```
