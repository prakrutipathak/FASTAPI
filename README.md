
# Implementation of FastAPI

This is a simple application that uses FastAPI for classifying the iris flower species based on its features. The application uses a trained logistic regression model to make predictions.





## Installation

1. Clone this repository:

```bash
git clone https://github.com/prakrutipathak/FASTAPI.git
```
2. Navigate to the project directory:

```bash
cd FASTAPI
```
3. Create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```
4. Install the required libraries:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the server by running the following command:
 ```bash
uvicorn main:app --reload
```
This command starts the server and reloads it automatically when you make changes to the code.

2. Open a browser and navigate to http://localhost:8000/. You should see a welcome message.

3. To Test the api run the test.py
```bash
python test.py
```
Where you can view the predicted output

## Development
- main.py: This file defines the FastAPI application and the prediction route.

- requirements.txt: This file lists the required libraries for the application.
- iris_model.pkl: This is a trained logistic regression model that is used to make predictions.
- test.py: This file contains code to test the api.



 
    
