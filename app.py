from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
med_df = pd.read_pickle("medicine_data_with_images.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/medicines')
def medicines():
    medicines = med_df.to_dict(orient='records')
    return render_template("product_list.html", medicines=medicines)

@app.route('/medicine/<int:medicine_id>')
def medicine_detail(medicine_id):
    med = med_df[med_df['id'] == medicine_id].to_dict(orient='records')
    if med:
        return render_template("product_detail.html", medicine=med[0])
    return "Medicine not found", 404

if __name__ == '__main__':
    app.run(debug=True)
