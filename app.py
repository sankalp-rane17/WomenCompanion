from flask import Flask,request,jsonify
import pickle
import numpy as nm

model = pickle.load(open('model.pkl','rb'))

app=Flask(__name__)



@app.route('/predict',methods=['POST'])
def predict():
                                                  Funny=request.form.get('Funny')
                                                  Blame=request.form.get('Blame')
                                                  Panicky=request.form.get('Panicky')
                                                  Anxious=request.form.get('Anxious')
                                                  topofme=request.form.get('topofme')
                                                  miserable=request.form.get('miserable')
                                                  unhappy=request.form.get('unhappy')
                                                  Depression=request.form.get('Depression')
                                                  crying=request.form.get('crying')
                                                  Enjoyment=request.form.get('Enjoyment')
                                                  harming=request.form.get('harming')
                                                  
                                                  input_query = nm.array([[Funny,Blame,Panicky,Anxious,topofme,miserable,unhappy,Depression,crying,Enjoyment,harming]])
                                                  result=model.predict(input_query)[0]
                                                  return jsonify({'depression':str(result)})
if __name__=='__main__':
                                                  app.run(debug=True)
                                                  