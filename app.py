from pickle import TRUE
from flask import Flask,jsonify,render_template,request
app = Flask(__name__)
@app.route("/")
def welcome():
    print(" gaurav")
    return " hellow flask"
################################################
@app.route("/test")
def  test_api():
    print('2nd api')
    return ({"massage":"send early morning"})
################################################################


@app.route('/predict_charges')
def get_insurance_charges():
     age=56
     sex='male'
     bmi=27.9
     children= 4
     smoker='yes'
     region='northeast'
     med_ins=MedicalInsurance(age, sex, bmi, children, smoker,region)
     med_ins.get_predicted_charges()
     return jsonify({'msg':"success"})
 
if __name__ == "__main__":
    app.run(port= 5005, debug=True)

    
