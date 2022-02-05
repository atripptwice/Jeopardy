# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
response = requests.get('https://jservice.io/api/random')
x = response.json()

print("The category is: " + x[0]['category']['title'])
print("Question value is: " + str(x[0]['value']))
print("Question: " + x[0]['question'])
print("Scroll down for the answer!")
for i in range(20):
    print()
print("Answer: " + x[0]['answer'])
