from flask import Flask
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask import jsonify

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/CathayDB"
mongo = PyMongo(app)
app.config['JSON_AS_ASCII'] = False


@app.route('/api/find', methods=['GET'])
def find_all():
    renter = mongo.db.Cathay_591_data
    output = []
    for s in renter.find():
        output.append({'renter':s['renter'], 'title':s['title'], 'city':s['city']})
    return jsonify({'result' : output})

@app.route('/api/find/gender/<gender>/city/<city>', methods=['GET'])
def search_gender_city(gender, city):
    renter = mongo.db.Cathay_591_data
    s = renter.find({'$or':[{'gender':gender},{'gender':'男女生皆可'},{'gender':None}], 'city':city})
    if s:
        output = []
        for i in s:
            output.append({'gender':i['gender'], 'title':i['title'], 'city':i['city']})

    return jsonify({'result' : output})

@app.route('/api/find/phone/<phone>', methods=['GET'])
def search_phone(phone):
    renter = mongo.db.Cathay_591_data
    s = renter.find({'phone':phone})
    if s:
        output = []
        for i in s:
            output.append({'gender':i['gender'], 'renter':i['renter'], 'title':i['title'], 'city':i['city'], 'phone':i['phone']})
    
    return jsonify({'result' : output})

@app.route('/api/find/is_identity/<identity>', methods=['GET'])
def search_is_identity(identity):
    renter = mongo.db.Cathay_591_data
    s = renter.find({'identity':identity})
    if s:
        output = []
        for i in s:
            output.append({'gender':i['gender'], 'renter':i['renter'], 'identity':i['identity'],
                           'title':i['title'], 'city':i['city'], 'phone':i['phone']})
    
    return jsonify({'result' : output})

@app.route('/api/find/not_identity/<identity>', methods=['GET'])
def search_not_identity(identity):
    renter = mongo.db.Cathay_591_data
    s = renter.find({'identity':{'$ne':identity}})
    if s:
        output = []
        for i in s:
            output.append({'gender':i['gender'], 'renter':i['renter'], 'identity':i['identity'],
                           'title':i['title'], 'city':i['city'], 'phone':i['phone']})
    
    return jsonify({'result' : output})

@app.route('/api/find/renter/<renter_name>/renter_gender/<renter_gender>/city/<city>', methods=['GET'])
def get_search(renter_name, renter_gender, city):
    renter = mongo.db.Cathay_591_data
    if renter_gender == 'man':
        s = renter.find({'$or':[{'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '哥'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '弟'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '先生'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '爸'}}]}], 'city':city})
    elif renter_gender == 'women':
        s = renter.find({'$or':[{'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '姊'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '姐'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '妹'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '小姐'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '太太'}}]},
                                {'$and':[{'renter':{'$regex': renter_name}}, {'renter':{'$regex': '媽'}}]}], 'city':city})
        
    if s:
        output = []
        for i in s:
            output.append({'renter' : i['renter'], 'title' : i['title'], 'city':i['city']})
        
    return jsonify({'result' : output})
