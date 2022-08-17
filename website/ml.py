from flask import Flask, render_template, request
import pickle 
app = Flask(__name__)
import sklearn as sk
import numpy as np
import pandas as pd




# model = pickle.load(open('svc_model.pkl','rb')) 
# aircraft_type = pickle.load(open('aircraft.pkl','rb')) 
# bay_number = pickle.load(open('bayno.pkl','rb')) 
# model = pickle.load(open('log.pkl','rb'))
# dfcols = pickle.load(open('dfcol.pkl','rb')) 
# data = pickle.load(open('test.csv','rb'))[:10]



@app.route("/ml")
def ml():
    return render_template("ml.html")

    # myData = list(data.values)
    # return render_template('ml.html',bay_number = bay_number,aircraft_type=aircraft_type,myData = myData)

# todo 
# make it into single function 
# load result into seperate table above csv
# call function from main file


# @app.route('/', methods=['GET', 'POST'])
# def ml():
#     if request.method == 'GET':
#         return render_template('ml.html',bay_number = bay_number,aircraft_type=aircraft_type )
#     elif request.method == 'POST':
#         time = int(request.form["time"])
#         count = int(request.form["count"])
        
        
#         aircraft_type = 'aircraft_type_' + str(request.form["aircraft_type"])
#         bay_number = 'bay_number_' + str(request.form["bay_number"])

#         p = pd.DataFrame(columns =dfcols)
#         p = p.append(pd.Series(0, index=dfcols), ignore_index=True)
#         p.at[0,'time']=time
#         p.at[0,'count']=count
#         p.at[0,bay_number] = 1
#         p.at[0,aircraft_type] = 1
#         #get prediction
        
#         pred = model.predict(p)
#         # pred = p[0]
#         return render_template("index.html",bay_number = bay_number,aircraft_type=aircraft_type, prediction_text='pred: {}'.format(pred[0]))

    

# @app.route("/predict", methods=['GET','POST'])
# def predict():
#     if request.method == 'POST':
    
#         time = int(request.form["time"])
#         count = int(request.form["count"])
        
        
#         aircraft_type = 'aircraft_type_' + str(request.form["aircraft_type"])
#         bay_number = 'bay_number_' + str(request.form["bay_number"])

#         p = pd.DataFrame(columns =dfcols)
#         p = p.append(pd.Series(0, index=dfcols), ignore_index=True)
#         p.at[0,'time']=time
#         p.at[0,'count']=count
#         p.at[0,bay_number] = 1
#         p.at[0,aircraft_type] = 1
#         #get prediction
        
#         pred = model.predict(p)
#         # pred = p[0]
        
#         return render_template("ml.html", prediction_text='pred: {}'.format(pred),bay_number = bay_number,aircraft_type=aircraft_type,myData = myData)

if __name__ == "__main__":
    app.run(debug=True)