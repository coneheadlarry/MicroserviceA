# CSV to JSON Microservice


## Overview

This service converts uploaded CSV files to JSON format. It is implemented using Flask and provides a simple API to handle file uploads and receive JSON data.


## HTTP communcation 
To request data from the service, you need to POST a CSV file path to the /convert endpoint. The server will return a JSON file. It is up to the user to decide what to do with the response.

```
POST URL/convert -F "file path"
```


## Example Request 
This example creates a request function that gets the JSON file from the service then saves it in a specifed location.

```
import requests

def make_request_CSV_to_JSON(file_path, save_path):
    url = "http://localhost:4000/convert"
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Request successful! JSON file saved as '{save_path}'.")
    elif response.status_code == 400:
        print("Error:", response.json()['error'])
    else:
        print("An error occurred:", response.status_code, response.text)

make_request_CSV_to_JSON("CSVs/trainees.csv", "JSONS/trainees.json")
```
### or 

```
curl -X POST http://localhost:4000/convert \ -F "file=@/path/to/your/file.csv"
```

## Receiving Data from the Microservice

Appon successful processing, the service returns the JSON representation of the CSV data. If you use example code for a request the JSON will be saved in the specified path.

### Example Response 
```
[
    {
    "header1": "value1", 
    "header2": "value2"
    },
    {
    "header1": "value3", 
    "header2": "value4"
    }
]
```

# UML Diagram

![UML diagram](imgs/image.png)

### Quick Start Guide
Create a function that has service URL file path, and save path. You can then call the function when you need to convert a CSV to a JSON file.
```
import requests

def make_request_CSV_to_JSON(file_path, save_path):
    url = "http://localhost:4000/convert"
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Request successful! JSON file saved as '{save_path}'.")
    elif response.status_code == 400:
        print("Error:", response.json()['error'])
    else:
        print("An error occurred:", response.status_code, response.text)

make_request_CSV_to_JSON("CSVs/trainees.csv", "JSONS/trainees.json")
```
