from flask import Flask, url_for, render_template, request
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/rank")
def render_rank():
    names = get_names()
    return render_template('rank.html', names = names)
    
@app.route("/data")
def render_data():
    names = get_names()
    return render_template('data.html', names = names)
def get_names():
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    names=list(set([c["name"] for c in info]))
    
    return names
@app.route("/response")
def render_response():
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    choice = request.args["billionaire"]
    
    for i in info:
        if i['name'] == choice:
            response1 = choice + " is rank " + str(i['rank']) + " in the list of billioniares from 1994 to 2014"
            response2 = choice + " is rank " + str(i['rank']) + " in the list of billioniares from 1994 to 2014"
        




    return render_template('rank.html', response = response1)
@app.route("/response1")
def render_response1():
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    choice = request.args["billionaire"]
    
    for i in info:
        if i['name'] == choice:
            print((i['company']['founded']))
            reply2 = choice + " is rank " + str(i['rank']) + " in the list of billioniares from 1994 to 2014. Their data was collected in " + str(i['year']) + "."
            reply3 = "This wealth came from the company " + i['company']['name'] + ", which was founded in " + str(i['company']['founded']) + "."
            if i['company']['relationship'] == 'relation': #ask how to do an or statement for empty ""
                i['company']['relationship'] = ' an important member'
            else: i['company']['relationship'] = "the " + i['company']['relationship']
            if i['demographics']['gender'] == 'male':
                reply4 = "He is " + str(i['demographics']['age']) + " years old and is " + i['company']['relationship'] + " of the company."
            elif i['demographics']['gender'] == 'female':
                reply4 = "She is " + str(i['demographics']['age']) + " years old and is " + i['company']['relationship'] + " of the company."
            else:
                reply4 = "They are " + str(i['demographics']['age']) + " years old and is " + i['company']['relationship'] + " of the company."
            

    return render_template('data.html', response = reply2, response1 = reply3, response2 = reply4)
if __name__=="__main__":
    app.run(debug=False)