# Ask the user for the price of a meal at a restaurant. Then calculate the tip for the meal at 15%,18% and 20%. Output the results using the print().

# Ask the user for the price of the meal
mealPrice = float(input("What is the price of the meal? "))

# Calculate the tip for 15%
tip15 = mealPrice * 0.15

# Calculate the tip for 18%
tip18 = mealPrice * 0.18

# Calculate the tip for 20%
tip20 = mealPrice * 0.20

# Output the results
print("A 15% tip would be: ", tip15)
print("A 18% tip would be: ", tip18)
print("A 20% tip would be: ", tip20)

# Output the results using 2 decimal places and round the decimal places,
print("A 15% tip would be: ", round(tip15, 2))
print("A 18% tip would be: ", round(tip18, 2))
print("A 20% tip would be: ", round(tip20, 2))

# Output a nice message to the waitress in the style of Edgard Allen Poe.
print("Thank you for your service, your tip is: ", round(tip20, 2), "dollars.")

# Output a nice message to the waitress in the style of Ice T.
print("Yo, thanks for your service, your tip is: ", round(tip20, 2), "dollars.")

# Output a nice message to the waitress in the style of a pirate.
print("A tip of ", round(tip20, 2), "dollars, for your service, me hearty.")

# Output a nice message to the waitress in the style of a Mr. T.
message = "I pity the fool who doesn't give a tip of ", round(tip20, 2), "dollars."

# Output a nice message to the waitress in the style of a Taylor Swift.
print("I knew you were trouble when you walked in, so here's a tip of ", round(tip20, 2), "dollars.")

# Output the results using 2 decimal places and format for 2 decimal places.
print("A 15% tip would be: ", format(tip15, '.2f'))
print("A 18% tip would be: ", format(tip18, '.2f'))
print("A 20% tip would be: ", format(tip20, '.2f'))

# Output the results to a web browser, using flask
from flask import Flask

app = Flask(__name__)

@app.route('/')

# create the html for the web page
def index():
    return """
    <html>
    <body>
    <h1>Tip Calculator</h1>
    <p>A 15% tip would be: """ + str(round(tip15, 2)) + """</p>
    <p>A 18% tip would be: """ + str(round(tip18, 2)) + """</p>
    <p>A 20% tip would be: """ + str(round(tip20, 2)) + """</p>
    <h2>Mr. T says:</h2>
    <p>""" + str(message) + """</p>
    </body>
    </html>
    """

# run the web page
app.run(debug=True)

# Path: copilotWebVersion.py