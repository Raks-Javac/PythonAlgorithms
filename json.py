import json
json_output = '{"email":"rufaikudus@gmail.com","password": "*****"}'


#converts json to python dictionary
py_output = json.loads(json_output)
print(py_output)

#converts python dictionary to json
py_output = {
    "email":"rufaikudus@gmail.com","password": "*****"
}
json_output = json.dumps(py_output)
print(json_output)