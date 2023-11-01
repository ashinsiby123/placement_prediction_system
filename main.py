import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
#data= pd.read_csv('cleaned_dataset.csv')
pipe = pickle.load(open("gb_model.pkl","rb"))

@app.route('/')
def index():

    #locations = sorted(data['location'].unique())
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    ip = request.form.get('ip')
    pr = request.form.get('pr')
    wc = request.form.get('wc')
    ass = request.form.get('ass')
    sst = request.form.get('sst')
    sscm = request.form.get('sscm')
    hscm = request.form.get('hscm')
    exa = request.form.get('exa')
    pt = request.form.get('pt')

    print(cgpa, ip, pr, wc, ass, sst, exa, pt, sscm, hscm)
    input = pd.DataFrame([[cgpa, ip, pr, wc, ass, sst, exa, pt, sscm, hscm]],columns=['CGPA', 'Internships', 'Projects', 'Workshops/Certifications', 'AptitudeTestScore', 'SoftSkillsRating', 'ExtracurricularActivities', 'PlacementTraining', 'SSC_Marks', 'HSC_Marks'])
    prediction = pipe.predict(input)[0]
    return render_template("popup.html", prediction_text = "Chance for placement : {}".format(prediction))
    #return render_template("popup.html", prediction_text = "Chance for placement : {}".format(np.round(prediction,0)))


if __name__=="__main__":
    app.run(debug=True)