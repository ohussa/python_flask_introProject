from flask import Flask, render_template
app=Flask(__name__,static_url_path='/static')
#static url, is address for static files, as we said webpages can change
#but not png,js and other files
#below code means when go to homepage,run the below function
#the @ is called a decorator
@app.route('/')
def index():
    #means serve client this html page
    return render_template('welcome.html')

#start the server, host 0.0.0.0 is allow connections from anywhere
#port 8080 means what port of computer should people use to connect
# to my computer(server)
app.run(host='0.0.0.0',port=8080)

