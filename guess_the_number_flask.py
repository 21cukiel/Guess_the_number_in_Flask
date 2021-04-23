from flask import Flask, request

app = Flask(__name__)



HTML_START = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<center>
<h1>Think a number from 1 to 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</center>
</body>
</html>
"""

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<center>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="to big">
    <input type="submit" name="user_answer" value="to small">
    <input type="submit" name="user_answer" value="you win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</center>
</body>
</html>
"""

HTML_WIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<center>
<h1>Your number is {guess}</h1>
</center>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """Function ask us about number, we answer is it to small or to big"""
    if request.method == "GET":
        return HTML_START.format(0, 1000)
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "to big":
            max = guess
        elif user_answer == "to small":
            min = guess
        elif user_answer == "you win":
            return HTML_WIN.format(guess=guess)

        guess = (max - min) // 2 + min

        return HTML.format(guess=guess, min=min, max=max)


if __name__ == '__main__':
    app.run()
