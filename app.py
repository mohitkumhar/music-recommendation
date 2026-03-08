from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

df = pickle.load(open('df.pkl', 'rb'))
similarity =pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)


def recommandation(song):
    if song not in df['song'].values:
        return f"Song '{song}' not found in the dataset."
    
    idx = df[df['song'] == song].index[0]
    
    distances = [(i, sim) for i, sim in enumerate(similarity[idx].flatten()) if i != idx]
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    
    songs = [df.iloc[i[0]]['song'] for i in distances[:20]]
    
    return songs



@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('index.html', name=names)


@app.route('/recom', methods=['POST'])
def mysong():
    user_song = request.form['names']
    songs = recommandation(user_song)
    
    return render_template('index.html', songs=songs)


if __name__ == "__main__":
    app.run(debug=False)