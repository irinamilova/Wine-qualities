import pandas as pd
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notebook')
def notebook():
    return render_template('nb.html')

@app.route('/streamlit')
def streamlit():
    return render_template('sreamlit.html')


def get_df():
    df = pd.read_csv("wines_SPA.csv")
    df = df.drop(columns=['winery', 'wine', 'year', 'rating', 'num_reviews', 'country', 'region', 'price', 'type', 'body', 'acidity'])
    #df["year"] = df["year"].replace("N.V.", np.NaN)
    df = df.dropna()
    return df

app.config["JSON_SORT_KEYS"] = False
df = get_df()


@app.route('/interactive')
def interactive():
    return render_template('interactive.html')


@app.route('/interactive', methods=['GET', 'POST'])
def feature():
    if request.method == 'POST':
        date = request.form.get('date')
        #
        #
        #
        result = {'result': wine }
        return redirect('/interactive', data=result)
    else:
        return render_template('interactive.html')


if __name__ == '__main__':
    app.run(debug=True, port=8500)

