from flask import Flask, render_template, request
import random
import cgi

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

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/thanks')
def thanks():
    person = "Bob"
    action = "dancing"
    return render_template("tynote.html", name = person, verb = action)

@app.route('/results', methods=["POST"])
def results():
   color_choice = request.form['color']
   return 'Favorite color: ' + cgi.escape(color) #protects user input from hacking
   luck_num = request.form['luck_num']
   fav_class = request.form['fav_class']
   best_pix = request.form['best_pix'].lower().strip()

   films = ["toy story","a bug's life","toy story 2","monsters, inc.",
      "finding nemo", "the incredibles","cars","ratatouille","wall-e","up",
      "toy story 3","cars 2", "brave","monsters university","inside out",
      "the good dinosaur","finding dory", "cars 3","coco","incredibles 2",
      "toy story 4","onward","soul"]

   if best_pix not in films:
      best_pix = "Sorry, '{0}' isn't a Pixar film.".format(best_pix.title())
   else:
      best_pix = best_pix.title()

# sets cookies in flask to save data for users
# http_response = make_response(render_template('form_results.html', color = color_choice, luck_num = luck_num, fav_class = fav_class, best_pix = best_pix))
# http_response.set_cookie(cookie_name, cookie_value)
# return http_response

   return render_template('form_results.html', color = color_choice, luck_num = luck_num, fav_class = fav_class, best_pix = best_pix)

if __name__ == '__main__':
   app.run()