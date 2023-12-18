AirBnB clone - Web framework

## Learning Objectives

In this folder, you will find the following topics:

# Flask Web Application

This repository contains a Flask web application with various routes and templates. The application is structured to display information about states and cities.


### General

* What is a Web Framework : A web framework (WF) or web application framework (WAF) is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs. Web frameworks provide a standard way to build and deploy web applications on the World Wide Web. Web frameworks aim to automate the overhead associated with common activities performed in web development. For example, many web frameworks provide libraries for database access, templating frameworks, and session management, and they often promote code reuse.
* How to build a web framework with Flask (AirBnB clone): Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

### More Info

When running your server.py script, you must use port 5000 - 
    example: `app.run(host="0.0.0.0", port=5000)`

#### Install Flask

```bash
$ pip3 install Flask
```

#### Install Jinja

```bash
$ pip3 install Jinja2
```

#### Install pep8

```bash
$ pip3 install pep8
```

## On this Folder

### 0. Hello Flask! : This script starts a Flask web application and display Hello HBNB!

### 1. HBNB : This script starts a Flask web application and make it display a page with HBNB

### 2. C is fun! : This script starts a Flask web application and make it display a page with C is fun!



### 3. Python is cool! : This script starts a Flask web application and make it display a page with Python is cool!



### 4. Is it a number? : This script starts a Flask web application and it display a page with a number only if n is an integer


### 5. Number template : This script starts a Flask web application and the page display a HTML page only if n is an integer that is the number is in the route /number_template/<n>

### 6. Odd or even? : This script starts a Flask web application and the page display a HTML page only if n is an integer that is the number is in the route /number_odd_or_even/<n>

### 7. Improve engines : This script starts a Flask web application and improve the file storage engine to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

### 8. List of states : This script starts a Flask web application and have a HTML page that display a list of states from storage engine (FileStorage or DBStorage) listed in alphabetical order

### 9. Cities by states : This script starts a Flask web application and have a HTML page that display a list of cities from storage engine (FileStorage or DBStorage) listed in alphabetical order

### 10. States and State : This script starts a Flask web application and make it display a HTML page that display a list of states from storage engine (FileStorage or DBStorage) listed in alphabetical order


### Python Scripts

1. **1-hbnb_route.py**
   - Description: Simple Flask script to start a web application.
   - Usage: `curl 0.0.0.0:5000/hbnb`

2. **2-c_route.py**
   - Description: Flask script to start a web application with multiple routes.
   - Usage: `curl 0.0.0.0:5000/c ; curl 0.0.0.0:5000/python ; curl 0.0.0.0:5000/text`

3. **3-python_route.py**
   - Description: Flask script to start a web application with a dynamic route.
   - Usage: `curl 0.0.0.0:5000/python/(any text)`

4. **4-number_route.py**
   - Description: Flask script to start a web application with a dynamic route that accepts only integers.
   - Usage: `curl 0.0.0.0:5000/n/(any integer)`

5. **5-number_template.py**
   - Description: Flask script to start a web application with a dynamic route that accepts only integers. Renders an HTML page with the integer.
   - Usage: `curl 0.0.0.0:5000/n/(any integer)`

6. **6-number_odd_or_even.py**
   - Description: Flask script to start a web application with a dynamic route that accepts only integers. Renders an HTML page with information about whether the integer is odd or even.
   - Usage: `curl 0.0.0.0:5000/n/(any integer)`

7. **7-states_list.py**
   - Description: Flask script to start a web application that displays a list of states retrieved from the storage engine.
   - Usage: `curl 0.0.0.0:5000/states`

8. **8-cities_by_states.py**
   - Description: Flask script to start a web application that displays a list of states and their cities retrieved from the storage engine.
   - Usage: `curl 0.0.0.0:5000/cities_by_states`

9. **9-states.py**
   - Description: Flask script to start a web application that displays a list of states and their cities, with dynamic routes for individual states.
   - Usage: `curl 0.0.0.0:5000/states` and `curl 0.0.0.0:5000/states/(state_id)`

10. **10-hbnb_filters.py**
    - Description: Flask script to start a web application that displays an HTML page with HBNB filters.
    - Usage: `curl 0.0.0.0:5000/hbnb_filters`

### HTML Templates

1. **5-number.html**
   - Description: HTML template for the 5-number_template.py script.

2. **6-number_odd_or_even.html**
   - Description: HTML template for the 6-number_odd_or_even.py script.

3. **9-states.html**
   - Description: HTML template for the 9-states.py script.

4. **10-hbnb_filters.html**
   - Description: HTML template for the 10-hbnb_filters.py script.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the repository:

    ```bash
    cd <repository-name>
    ```

3. Run a Flask script (choose any of the Python scripts mentioned above):

    ```bash
    python <script-name.py>
    ```

4. Open a browser and visit `http://0.0.0.0:5000/` to interact with the web application.

## Bugs

No known bugs at this time.

## Authors

Sweety Castro 