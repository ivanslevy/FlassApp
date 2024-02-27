# Flask modules
from flask   import render_template, request, jsonify
from flask import send_from_directory
import jsonify
from jinja2  import TemplateNotFound

import pandas as pd
# App modules
from app import app

# Charger les données du fichier metrics_df.py et définir les variables
exec(open('C:/Users/gilbe/OneDrive/Bureau/MDSMS 2/Data Science sous Python et R/jinja-star-admin-master/app/metrics_df.py').read())

# Définir les variables que vous souhaitez transmettre au template
acc = df.Metrics[0]
pre = df.Metrics[1]
rec = df.Metrics[2]
f1 = df.Metrics[3]
auc = df.Metrics[4]

df = df
df2 = df2
df_sl = df_sl.to_dict()
df_sw = df_sw.to_dict()
df_pl = df_pl.to_dict()
df_pw = df_pw.to_dict()

rf_model = rf_model


dist = df2.groupby('nature').count().target
labels = dist.index

chart_data3 = pd.DataFrame(df2.iloc[:,:4].describe().drop(['std','count'])).to_dict()

chart_data2 = {
    'Names': dist.tolist(),
    'Counts': labels.tolist()
}

chart_data = {
    'Names': df.Names.tolist(),
    'Metrics': df.Metrics[:-1].tolist()
}

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')

def index(path):

    try:
        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + path, segment=segment, acc=acc, pre=pre, rec=rec, f1=f1, auc=auc, chart_data=chart_data,
                                chart_data2=chart_data2,chart_data3=chart_data3,df_sl=df_sl,df_sw=df_sw,df_pl=df_pl,df_pw=df_pw,
                                table=df2.to_html(classes='table'))
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404


@app.route('/predict', methods=['POST'])
def predict():

    # Récupérer les données du formulaire
    input1 = float(request.form['value1'])
    input2 = float(request.form['value2'])
    input3 = float(request.form['value3'])
    input4 = float(request.form['value4'])

    prediction = rf_model.predict([[input1, input2, input3, input4]])
    prediction = prediction[0]

    dict = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }
    nature = dict[prediction]

    # Effectuer des prédictions avec les données reçues

    # Renvoyer les prédictions dans le template sans recharger la page
    return str(nature)

def get_segment( request ): 

    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  

