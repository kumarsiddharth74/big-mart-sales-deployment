import flask
import pandas as pd
#from joblib import dump, load
import pickle

#with open(f'bigmart_final.pkl', 'rb') as f:
#    model = load(f)
model = pickle.load(open('bigmart_final.pkl', 'rb'))

app1 = flask.Flask(__name__, template_folder='templates')


@app1.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        Item_Weight=flask.request.form['Item_Weight']

        Item_Fat_Content=flask.request.form['Item_Fat_Content']
        Item_Visibility=flask.request.form['Item_Visibility']
        Item_Type=flask.request.form['Item_Type']
        Item_MRP=flask.request.form['Item_MRP']
        Outlet_Establishment_Year=flask.request.form['Outlet_Establishment_Year']
        Outlet_Type=flask.request.form['Outlet_Type']
        Outlet_Size=flask.request.form['Outlet_Size']
        Outlet_Location_Type=flask.request.form['Outlet_Location_Type']
        pred_args=pd.DataFrame([[Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                   Item_MRP,Outlet_Establishment_Year,Outlet_Type,Outlet_Size,Outlet_Location_Type
                   ]],columns=[Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                              Item_MRP,Outlet_Establishment_Year,Outlet_Type,Outlet_Size,Outlet_Location_Type
                              ],dtype='float',index=['input'])

        predictions = model.predict(pred_args)[0]
        print(predictions)

        return flask.render_template('main.html',result=predictions)


if __name__ == '__main__':
    app1.run()
