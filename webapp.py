from flask import Flask, url_for, render_template, request
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html',a=liam(76,100), b=amount(1,25))
    
@app.route("/rank")
def render_rank():
    names = get_names()
    return render_template('rank.html', names = names)
    
@app.route("/data")
def render_data():
    names = get_names()
    return render_template('data.html', names = names)
    
@app.route("/graph")
def render_graph():
    names = get_names()
    return render_template('graph.html', names = names)
    
@app.route("/graph2")
def render_graph2():
    names = get_names()
    return render_template('graph2.html', names = names)
    
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
    count = 0
    names = []
    highest = []
    years = []
    for i in info:
        if i["name"] not in names:
            names.append(i["name"])
            highest.append(i["rank"])
            years.append(i["year"])
        else:
            x = names.index(i["name"])
            if highest[x] < i["rank"]:
                highest[x] = i["rank"]
                years[x] = i["year"]
    
    if choice not in names:
        return render_template('rank.html', response = "Please enter a valid name")
        
    for n in names:
        if n == choice:
            response1 = choice + " was highest ranked  at rank " + str(highest[names.index(n)]) + " in the year " + str(years[names.index(n)]) + "."
    
        




    return render_template('rank.html', response = response1)

@app.route("/response1")
def render_response1():
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    choice = request.args["billionaire"]
    
    for i in info:
        if i['name'] == choice:
            print((i['company']['founded']))
            emerging = ""
            reply3 = "This wealth came from the company " + i['company']['name'] + ", which was founded in " + str(i['company']['founded']) + "."
            
            
            if i['wealth']['how']['from emerging'] == True:
                emerging = ", is from an emerging market, meaning that it's coming from a fast growing economy"
            else: emerging = ", is not from an emerging market."
            reply2 = choice + " 's company, " + i['company']['name'] + emerging + "."
            relationship = ""
            if i['company']['relationship'] == 'relation' or i['company']['relationship'] == '': 
                relationship = ' an important member'
            else: relationship = "the " + i['company']['relationship']
            age = ""
            if i['demographics']['age'] == 0: 
                age = 'has an unknown age'
            else: age = "is " + str(i['demographics']['age']) + " years old" 
            
            if i['demographics']['gender'] == 'male':
                reply4 = "He " + age + " and is " + relationship + " of the company."
            elif i['demographics']['gender'] == 'female':
                reply4 = "She " + age + " and is " + relationship + " of the company."
            else:
                reply4 = "They " + age + " and is " + relationship + " of the company."
            

    return render_template('data.html', response = reply2, response1 = reply3, response2 = reply4)
    
    
    
    
def liam(min,max):
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    money = 0
    count = 0
    for i in info:
        if i["demographics"]["age"] > min and i["demographics"]["age"] <= max:
            money += i["wealth"]["worth in billions"]
            count+=1
            
    return money/count
def amount(min,max):
    with open('billionaires.json') as billionaires_data:
        info = json.load(billionaires_data)
    
    count = ""
    for i in info:
        if i["demographics"]["age"] > min and i["demographics"]["age"] <= max:
            
            count+= " " + i['name'] + " " 
            
    return count
     
    



if __name__=="__main__":
    app.run(debug=False)