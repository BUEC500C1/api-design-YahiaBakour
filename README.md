# Yahia Bakour Api Design

HW2 for EC500.

By: Yahia Bakour

Email: yehia234@bu.edu

BUID: U37575373

## Getting Started

#### To setup server

```
python3 -m flask run --host=0.0.0.0 --port=8000
```

#### To get data from server

```
curl http://0.0.0.0:8000/user\?twittername\=Reuters
```


### Prerequisites

You will need to setup your config source/config.py file as shown

```
TWITTER_API_KEY = XXXXXXXXX
TWITTER_API_SECRET_KEY = XXXXXXXXXXXXXXXXXX
TWITTER_ACCESS_TOKEN = XXXXXXXXX
TWITTER_ACCESS_TOKEN_SECRET = XXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Twitter Keys:

[Setup a Twitter API Key](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/) - Twitter API Key how to

Google Cloud Api Service Accounts:

[Setup a Google Cloud Vision Service Account](https://cloud.google.com/vision) - Google Cloud Vision Api Service Account How To


### Installing

Install requirements
```
pip3 install -r requirements.txt
```

## Running the tests

```
export GOOGLE_APPLICATION_CREDENTIALS="google_application_credentials.json"
python3 tests/unitTests.py
```

## Results

running

```
curl http://0.0.0.0:8000/user\?twittername\=Reuters
```

Produces

```
[{"name": "Reuters", "text": "Man shot by police in London was under surveillance: Sky News https://t.co/HQaiFsklDa https://t.co/2NDGVIHUDI", "images": [{"objects": [{"name": "Bus", "score": 0.9217402935028076}, {"name": "Person", "score": 0.908085823059082}, {"name": "Car", "score": 0.8587362766265869}, {"name": "Bus", "score": 0.7822839617729187}, {"name": "Bus", "score": 0.6747764945030212}, {"name": "Bus", "score": 0.6524977684020996}]}]}, {"name": "Reuters", "text": "OPEC+ technical panel to meet Feb 4-5 to discuss coronavirus impact: sources https://t.co/Q2WqPSrfAO https://t.co/rS8nGrjQFw", "images": [{"objects": []}]}, {"name": "Reuters", "text": "ICYMI: British swimmer Lewis Gordon Pugh swam in icy Antarctic waters to raise awareness about climate change https://t.co/wwBPbHi4cY", "images": [{"objects": [{"name": "Animal", "score": 0.6502722501754761}, {"name": "Person", "score": 0.5106813907623291}]}]}, {"name": "Reuters", "text": "North Korea says it is free of new virus amid travel restrictions https://t.co/B1zcal9m2i https://t.co/zYDd1QKRK4", "images": [{"objects": [{"name": "Flag", "score": 0.7180966734886169}]}]}, {"name": "Reuters", "text": "Protesters marched in Baghdad and southern cities in Iraq against the appointment of the country's new prime minist\u2026 https://t.co/9sDZj6xEva", "images": []}, {"name": "Reuters", "text": "Head of Sudan's sovereign council invited to visit Washington https://t.co/omn1Eaftzh https://t.co/6mOKo7KAA5", "images": [{"objects": [{"name": "Hat", "score": 0.8886822462081909}, {"name": "Person", "score": 0.8514617085456848}, {"name": "Man", "score": 0.794467568397522}, {"name": "Person", "score": 0.7843323945999146}, {"name": "Man", "score": 0.7004446983337402}, {"name": "Packaged goods", "score": 0.6256531476974487}, {"name": "Luggage & bags", "score": 0.588623046875}, {"name": "Person", "score": 0.550233006477356}, {"name": "Person", "score": 0.5226520299911499}]}]}, {"name": "Reuters", "text": "ICYMI: Fighting against odds, model Ana Gabriela Molina was born without arms and she is seeking the crown in a sta\u2026 https://t.co/QiX5akClUk", "images": []}, {"name": "Reuters", "text": "On the campaign trail: Big crowds, Super Bowl watch parties cap Democrats' final Iowa push https://t.co/7Wr46Y6lwZ https://t.co/pIHY0zBbij", "images": [{"objects": [{"name": "Glove", "score": 0.6011140942573547}]}]}, {"name": "Reuters", "text": "Factbox: List of Australian Open men's singles champions https://t.co/qLh63fFxNR https://t.co/LHUSPYzhmY", "images": [{"objects": [{"name": "Man", "score": 0.8542057275772095}, {"name": "Top", "score": 0.7174635529518127}, {"name": "Bracelet", "score": 0.6085463762283325}]}]}, {"name": "Reuters", "text": "Box Office: 'Rhythm Section' Flops as 'Bad Boys' Takes Another Victory Lap https://t.co/s2J3AYN7vs https://t.co/C5qYNtsdQM", "images": [{"objects": [{"name": "Glasses", "score": 0.9519599676132202}, {"name": "Man", "score": 0.8706254959106445}, {"name": "Person", "score": 0.8536853790283203}, {"name": "Man", "score": 0.7661489248275757}, {"name": "Outerwear", "score": 0.6755449175834656}, {"name": "Hat", "score": 0.5604291558265686}]}]}, {"name": "Reuters", "text": "'Punxsutawney Phil' the Groundhog delivered the desired verdict to the cheers of his followers braving the early mo\u2026 https://t.co/RgJsVcqvhP", "images": []}, {"name": "Reuters", "text": "Djokovic targets Grand Slam record in two seasons https://t.co/8Y3ox062Uv https://t.co/d2Nnn1ntVo", "images": [{"objects": [{"name": "Man", "score": 0.8804200291633606}, {"name": "Top", "score": 0.7648512721061707}, {"name": "Person", "score": 0.6909412145614624}]}]}, {"name": "Reuters", "text": "Three-times unlucky but Thiem edges closer to slam breakthrough https://t.co/KidBMJCSkF https://t.co/K3uCXk3GZU", "images": [{"objects": [{"name": "Man", "score": 0.9002090096473694}, {"name": "Person", "score": 0.8777777552604675}, {"name": "Outerwear", "score": 0.646940290927887}, {"name": "Luggage & bags", "score": 0.6137917637825012}]}]}, {"name": "Reuters", "text": "ICYMI: 'It forms a large part of our identities': Nigerian English appears for the first time in Oxford English Dic\u2026 https://t.co/BiLfsFESwC", "images": []}, {"name": "Reuters", "text": "Activists occupy German coal plant site Datteln 4 in green protest https://t.co/xR5hY707mJ https://t.co/qTrsWcgCtC", "images": [{"objects": []}]}, {"name": "Reuters", "text": "Ahead of crucial vote, anxious Iowa Democrats grapple with tough choices https://t.co/a3ZBdJilRH https://t.co/kJVoAV8Etu", "images": [{"objects": [{"name": "Person", "score": 0.6872423887252808}, {"name": "Flag", "score": 0.6152145862579346}]}]}, {"name": "Reuters", "text": "Sovereignty comes first: Britain lays out tough stance for EU trade talks https://t.co/kflzqV9bvt https://t.co/54RSJLlbTC", "images": [{"objects": [{"name": "Flag", "score": 0.7819514870643616}, {"name": "Person", "score": 0.7814802527427673}]}]}, {"name": "Reuters", "text": "Djokovic edges Thiem in thriller to clinch eighth Australian Open https://t.co/QuSKJI1wdo https://t.co/HEVIWpC4TQ", "images": [{"objects": [{"name": "Tennis racket", "score": 0.9635822772979736}, {"name": "Person", "score": 0.9132473468780518}, {"name": "Man", "score": 0.8846760392189026}, {"name": "Top", "score": 0.8201693296432495}]}]}, {"name": "Reuters", "text": "Factbox: Latest on the coronavirus spreading in China and beyond https://t.co/nPUOSqbAuj https://t.co/OpTTORqKBx", "images": [{"objects": [{"name": "Person", "score": 0.9121265411376953}, {"name": "Person", "score": 0.904628574848175}, {"name": "Person", "score": 0.8956074714660645}, {"name": "Person", "score": 0.8892576098442078}, {"name": "Person", "score": 0.8857775926589966}, {"name": "Person", "score": 0.8808212280273438}, {"name": "Person", "score": 0.8583121299743652}, {"name": "Person", "score": 0.8539234399795532}, {"name": "Person", "score": 0.8339678645133972}, {"name": "Airplane", "score": 0.7917851209640503}]}]}, {"name": "Reuters", "text": "ICYMI: Prince Harry and Meghan have moved to a place with many hallmarks of home. A town on Canada's Vancouver Isla\u2026 https://t.co/Lzqdqx0wiX", "images": []}]
```


## Built With

* [Google Vision](https://cloud.google.com/vision) - Google Vision Api
* [Tweepy](http://docs.tweepy.org/en/latest/api.html) - Tweepy API
* [Flask Restful](https://flask-restful.readthedocs.io/en/latest/) - Flask Restful


## Authors

* **Yahia Bakour** - [Website](https://yahiabakour.com/)
