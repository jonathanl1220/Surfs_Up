from flask import Flask,redirect, render_template, jsonify, request
import pandas as pd
import numpy as np
from datetime import date, datetime
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

link = pd.read_pickle('img_link.pkl')

surf = pd.read_csv('/Users/victorialendof/Desktop/Jonathan/Galvanize/Capstones/Capstone3/app/surf_01_13_21pm.csv')

features = ['crowds',
            'difficulty',
            'surf height ft',
            'tide height ft',
            'wind kts',
            'water temp f',
            'temp f'    
]

X = surf[features].values

ss = StandardScaler()

X = ss.fit_transform(X)

def diff(x):
    if x <= 2:
        return 'Beginner'
    if x >2 and x < 4:
        return 'Intermediate'
    else:
        return 'Advanced'

def crowd(x):
    if x <= 3:
        return 'Not Crowded'
    else:
        return 'Crowded'
class_surf = surf
class_surf['difficulty'] = class_surf['difficulty'].apply(diff)
class_surf['crowds'] = class_surf['crowds'].apply(crowd)

def cos_sim_recommendations(index, n=5, region=None):
    spots = X[index].reshape(1,-1)
    cs = cosine_similarity(spots, X)
    rec_index = np.argsort(cs)[0][::-1]
    ordered_df = surf.loc[rec_index]
    ordered_df = ordered_df.drop(index)
    if region:
        ordered_df = ordered_df[ordered_df['region'] == region]
    rec_df = ordered_df.head(n)
    orig_row = surf.loc[[index]].rename(lambda x: 'original')
    total = pd.concat((orig_row,rec_df))

    return total

@app.route('/', methods=['GET','POST'])
def home():
        return render_template('index.html', content = 'Testing')

@app.route('/main_rec', methods=['GET','POST'])
def main_rec():
        return render_template('main_rec.html',surf = surf, content = 'Testing' )

@app.route('/sec_rec', methods=['GET','POST'])
def sec_rec():
    return render_template('sec_rec.html', class_surf = class_surf, content = 'Testing' )

@app.route('/about_me', methods=['GET','POST'])
def about_me():
        return render_template('about_me.html',surf = surf, content = 'Testing' )

@app.route('/recommendations', methods=['GET','POST'])
def recommendations():
    surfspot = request.form['surfspot']
    if surfspot != '':
        index = int(surfspot)
        rec_df = cos_sim_recommendations(index)
    b = surf['surfspot'].loc[index]
    return render_template('recommendations.html', b = b, rec_df = rec_df, content = 'Testing')

@app.route('/recommendations2', methods=['GET','POST'])
def recommendations2():
    region = request.form['region']
    experience = request.form['experience']
    crowd = request.form['crowd']
    class_surf['links']  = link
    rec2_df = class_surf[class_surf['region'] == region]
    rec2_df = rec2_df[rec2_df['difficulty'] == experience]
    rec2_df = rec2_df[rec2_df['crowds'] == crowd]
    rec2_df = rec2_df.drop(columns=['links'])
    rec2_df = rec2_df.head()
    a = list(rec2_df.region.unique()).pop(0)
    return render_template('recommendations2.html', a= a, link = link, rec2_df = rec2_df, content = 'Testing')

@app.route('/get_surfspot')
def get_surfspot():
    region = request.args.get('region')
    if region:
        sub_df = surf[surf['region'] == region]
        sub_df.sort_values(by='surfspot',inplace=True)
        id_name = [("","Select a surfspot...")] + list(zip(list(sub_df.index),list(sub_df['surfspot'])))
        data = [{"id": str(x[0]),"name": x[1]} for x in id_name]
    return jsonify(data)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)