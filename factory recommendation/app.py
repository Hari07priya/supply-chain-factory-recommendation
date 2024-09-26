from flask import Flask, request, render_template
from model import data, model, recommend_factory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_country = request.form['country']
    user_rating = int(request.form['rating'])
    user_delivery = int(request.form['delivery'])
    user_communication = int(request.form['communication'])
    user_price = int(request.form['price'])

    # Get the best factory recommendation, factory name, and reason
    best_supplier_id, best_factory_name, reason = recommend_factory(user_country, user_rating, user_delivery, user_communication, user_price, data, model)

    if best_supplier_id:
        return render_template('index.html', supplier_id=best_supplier_id, factory_name=best_factory_name, reason=reason)
    else:
        return render_template('index.html', error="No data available for the specified country.")

if __name__ == '__main__':
    app.run(debug=True)
