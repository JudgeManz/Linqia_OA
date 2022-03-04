# Sponsor API 

Features include:
- Return the vocabulary of sponsorship keywords
- Add a new keyword to the vocabulary
- Predict if the given text is sponsored or not
- Bonus: Store the vocabulary in a databse
- Bonus: Provide a dockerfile to run the code

# Tech Stack 
- Django 3.1.2
- Python 3.8.5
- SQLite3
- Docker

# Running the Application

<h2> Option A: Running on Docker </h2> 

1. Open terminal and run docker-compose file to build and run the application:
    ```
    docker-compose up --build
    ```
    Note: During the first run, build may take up to 5 minutes to finish

<h2> Option B: Running Locally </h2>

1. Open terminal and create the environment:
    ```
    conda env create -f env-windows.yml
    ```
2. Acitvate conda environment:
    ```
    conda activate linqia_oa
    ```
3. Run the Django application:
    ```
    python manage.py runserver
    ```

# Usage

<h2> Postman Requests </h2>

1. File -> Import -> Upload Files
2. Select postman_requests.json

(GET) Vocabulary <br>
- Description: Return the vocabulary of sponsorship keywords
- Endpoint: /api/vocab

(POST) Vocabulary <br>
- Description: Add a new keyword to the vocabulary
- Endpoint: /api/vocab

(POST) Prediction <br>
- Description: Predict if the given text is sponsored or not
- Endpoint: /api/prediction