# **Task-09 Report**

### **Overview**

In this task, I structured my project into multiple levels to improve modular programming, testing practices, and API integration. Each level introduced a new concept—from writing and testing basic functions to implementing APIs and mapping tools.

---

## **LEVEL 01 – Function Testing with Assert**

I started by creating a **`functions.py`** file that contained several utility functions.
To ensure correctness, I wrote another file named **`test_functions.py`**. This file used **assert statements** to verify that each function returned the expected output.
If a test passed, it confirmed the function’s accuracy; if it failed, it helped identify logical or coding errors.

---

## **LEVEL 02 – School Bounty Debugging**

Next, I developed **`schoolBounty.py`**, which included a set of functions for the school bounty logic.
To validate and debug these functions, I created **`test_schoolBounty.py`**, where I used **pytest** along with **assert** statements to test each part of the code.
Through this process, I successfully detected and fixed bugs, ensuring all tests passed without issues.

---

## **LEVEL 03 – Location Mapping**

In this stage, I built two files:

* **`location_map.py`** – Contains functions that fetch the user’s location through their IP address using an API, returning data such as **latitude**, **longitude**, **city**, **region**, and **country**.
* **`test_geo_map.py`** – Tests the accuracy of the functions.

Additionally, I used the **Folium** library to generate an interactive map from the coordinates and saved it as an **HTML** file, which could be opened in a browser for visualization.

---

### **Outcome**

This task strengthened my understanding of:

* Writing modular and testable Python code
* Using **assert** and **pytest** for unit testing
* Debugging efficiently
* Integrating external APIs and libraries (like **Folium** and **OpenWeatherMap**)
* Building reliable, data-driven Python applications.
