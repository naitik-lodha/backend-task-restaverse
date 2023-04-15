# Python Swiggy Data Extractor

This Python code flattens and normalizes the response received from Swiggy API. The API returns a JSON object containing the menu items of a restaurant. The code first sends a GET request to the API with the restaurant ID as input. It then parses the response body as JSON and extracts the required JSON object from the parsed response.

The extracted JSON object is flattened using a recursive function that separates nested key-value pairs by appending their keys together with an underscore. For instance, {"menu": {"item": "burger"}} becomes {"menu_item": "burger"}. Finally, the flattened JSON object is normalized using the pandas library's json_normalize() function.


## How to use the app

1.Install the required libraries using pip install -r requirements.txt.
2.Enter the restaurant ID in the restaurant_id variable.
3.Run the script and the normalized data will be saved in a CSV file named data.csv

## Libraries Used

-requests
-pandas

## Acknowledgments

This project was built as a task for Restaverse FullStack Development Intern Selection Process
