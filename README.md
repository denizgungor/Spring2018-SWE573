# Spring2018-SWE573
This repository contains applications &amp; documentation developed for Boğaziçi University Software engineering practice class.

Project Plan

Tomsplanner has been used for project plan.
Please find it in here: 

https://www.tomsplanner.com/public/denizswe573   

## Installing Instructions    

```
git clone https://github.com/denizgungor/Spring2018-SWE573.git  
cd Spring2018-SWE573   
pip install -r requirements.txt   
cd swe573
python manage.py runserver
```   

If you see  "RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly."    
Please run the command below:    
```conda install matplotlib```    
and run again:    
```python manage.py runserver```    


If you see "module 'preprocessor' has no attribute 'set_options'" error   
Go to url: https://pypi.org/project/tweet-preprocessor/#files   
Download the tweet-proprocessor manually   
Extract the files and execute the command below:      
``` 
cd tweet-preprocessor-0.5.0  
pip install . 
```
Then go to project folder again and start the app: 
```
cd Spring2018-SWE573\swe573     
python manage.py runserver   
```
