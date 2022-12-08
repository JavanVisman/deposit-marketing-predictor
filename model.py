import pickle

# global variable
global model, scaler

def load():
    global model, scaler
    model = pickle.load(open('model/pickle/rf_bm_model.pkl', 'rb'))
    scaler = pickle.load(open('model/pickle/scaler.pkl', 'rb'))

def model_predict(data):
    data = scaler.transform(data)
    prediction = int(model.predict(data))
    pred_score = model.predict_proba(data).flatten()
    pred_score = max(pred_score) * 100
    print(pred_score)
    pred_score = round(pred_score)

    if prediction == 1:
        pred_result = "berpotensi"
    else:
        pred_result = "tidak berpotensi"
    return pred_result, pred_score