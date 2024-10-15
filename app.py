# from flask import Flask,render_template

# app = Flask(_name_)

# data = dict()

# reviews =['good product','bad product']
# positive=1
# negative=1

# @app.route("/")
# def index():
#     data['reviews']=reviews
#     data['positive']= positive
#     data['negative']=negative
#     return render_template('index.html',data=data)


# if_name_=="_main_":
# app.run()

from flask import Flask, render_template

app = Flask(__name__)

# Replace hardcoded reviews with data from a database or other source
reviews = [
    {"product": "Product A", "review": "This product is great!", "rating": 5},
    {"product": "Product B", "review": "Not impressed with this one.", "rating": 2},
    # ... more reviews
]

def get_reviews():
    # Implement logic to fetch reviews from a database or other source
    return reviews

@app.route('/')
def index():
    reviews_data = get_reviews()
    positive_reviews = sum(1 for review in reviews_data if review["rating"] >= 3)
    negative_reviews = sum(1 for review in reviews_data if review["rating"] < 3)

    return render_template('index.html', reviews=reviews_data, positive=positive_reviews, negative=negative_reviews)

if __name__ == '__main__':
    app.run()