### Aim
This Project is aimed at building a predictive model for predicting used-car prices in Nigeria. 

#### Properties Considered
The Poperties Being considered are:
    1. Make
    2. Year
    3. Model
    4. Mileage
    5. Transmission
    6. Color
    7. Location
    8. History
    9. Car-Rating
    
    
### Files
##### data_scrap_c45.ipynb
This file scraps data from the cars45 website. copy the webpage of the car, you want to scrap into cell 3.
Keep copying the link and run only cell 3 and 4. Be careful not to run cell 2, this will re-initialize the dataframe.

##### data_scrap_cheki.ipynb
This file scraps data from the cheki website. copy the webpage of the car, you want to scrap into cell 3.
Keep copying the link and run only cell 3 and 4. Be careful not to run cell 2, this will re-initialize the dataframe.
Happy Scraping. 

##### data_cars45.ipynb
This file scraps data from car from autochek which is also redirecting the datas from Cheki.com.ng. 
In this file We scraped 14,195 rows of cars and saved into a CSV file afterwards. 

##### model_2.ipynb
For model development - Here I compared the performance of different models. (Linear Regression, k-Nearest Neigbours, Random Forest and Gradient Boosted Trees) with missing rating set to 2.0


##### model_2.ipynb-gridsearchcv
For model development - Here I used GridSearchCV to find the best parameters for the Gradient Boosted Trees and K-Nearest Neigbhours.
(The 2 best performing models from model_2.ipynb)

##### model_3.ipynb
For model development - Here I compared the performance of different models. (Linear Regression, k-Nearest Neigbours, Random Forest and Gradient Boosted Trees) with missing rating set to 3.0
