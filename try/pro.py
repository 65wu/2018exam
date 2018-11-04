from flask import Flask, render_template, request
import math,time
app=Flask(__name__)

@app.route('/')
def start():
    return render_template('primenum.html')

@app.route('/answer')
def end():
    return render_template('answer.html')

@app.route('/func', methods=['POST'])
def getPrime():
    Num=request.form['Num']
    Num=int(Num)
    primeList = []
    if Num > 2:
        for x in range(2, Num+1):
            x_sqrt = math.sqrt(x)
            for prime in primeList:
                if prime > x_sqrt:
                    primeList.append(x)
                    break
                if x % prime == 0:
                    break
            else:
                primeList.append(x)
        return render_template('answer.html', ans=primeList)
    else:
        return render_template('error.html')



if __name__ == "__main__":
    app.run(debug=True)



