from flask import Flask
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello')
def hello():
   message = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)   # Select a random integer from 1 - 25.
   return message.format(num)

@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message

@app.route('/third_page')
def third_page():
    message = "<h2>A third page too!</h2>"
    return message


if __name__ == '__main__':
   app.run()