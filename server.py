import flask as f

app = f.Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return f"""Человечество вырастает из детства.<br>
<br>
Человечеству мала одна планета.<br>
<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
<br>
И начнем с Марса!<br>
<br>
Присоединяйся!"""

@app.route('/image_mars')
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h2>Жди нас, Марс!</h2>
    <img src='https://foni.papik.pro/uploads/posts/2024-09/foni-papik-pro-b9s6-p-kartinki-mars-na-prozrachnom-fone-6.png' height=300px>
    <p>Вот она какая, красная планета.</p>
</body>
</html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Колонизация</title>
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" href="{f.url_for('static', filename='css/style.css')}">
</head>
<body>
    <h2>Жди нас, Марс!</h2>
    <img src='{f.url_for('static', filename='img/Mars.png')}' height=300px>
    <div class="alert-dark">Человечество вырастает из детства.</div>
<div class="alert-success">Человечеству мала одна планета.</div>
<div class="alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
<div class="alert-warning">И начнем с Марса!</div>
<div class="alert-danger">Присоединяйся!</div>
</body>
</html>"""


@app.route("/astronaut_selection")
def astronaut_selection():
    return f'''<!doctype html>
<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{f.url_for('static', filename='css/style.css')}" />
    <title>Отбор астронафтов</title>
    </head>
    <body>
    <h1>Анкета претендента</h1>
    <h3>на участие в миссии</h3>
    <div>
        <form class="login_form" method="post">
            <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="suname">
            <input type="text" class="form-control" id="text" placeholder="Введите имя" name="name">
            <br>
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
            <div class="form-group">
                <label for="classSelect">Какое у Вас образование?</label>
                <select class="form-control" id="classSelect" name="class">
                    <option>Начальное</option>
                    <option>Основное</option>
                    <option>Среднее</option>
                    <option>Среднее профессиональное</option>
                    <option>Высшее</option>
                </select>
                </div>
            <br>
            <div class="form-group">
                Какие у вас есть профессии?
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Индженер-иследователь</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Индженер-строитель</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Пилот</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Метеоролог</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Индженер по жизниобеспечению</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Индженер по радиоционной защите</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Врач</label>
                <br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                
            </div>
            <br>
            <div class="form-group">
                <label for="form-check">Укажите пол</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                    <label class="form-check-label" for="male">
                    Мужской
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">
                    Женский
                    </label>
                </div>
            </div>
            <br>
            <div class="form-group">
                <label for="about">Почему вы хотите принять участие в миссии?</label>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </div>
            <br>
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <br>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
    </body>
</html>'''

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Варианты выбора</title>
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" href="{f.url_for('static', filename='css/style.css')}">
</head>
<body>
    <h1 id='y'>Моё преложение: {planet_name}</h1>
    <h2>Эта планета близка к Земле;</h2>
<div class="alert-success">На ней много необходимых ресурсов;</div>
<div class="alert-secondary">На ней есть вода и атмосфера;</div>
<div class="alert-warning">На ней есть небольшое магнитное поле;</div>
<div class="alert-danger">Наконец, она просто красива!</div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Варианты выбора</title>
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" href="{f.url_for('static', filename='css/style.css')}">
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}</h2>
<div class="alert-success">Поздравляем ваш рейтинг после {level} этапа отбора</div>
<div>состовляет {rating}!</div>
<div class="alert-warning">Желаем удачи!</div>
</body>
</html>
    """

@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if f.request.method == 'GET':
        return f"""<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{f.url_for('static', filename='css/style.css')}" />
    <title>Отбор астронафтов</title>
    </head>
    <body>
    <h1>Загрузка фотографии</h1>
    <h3>для участия в миссии</h3>
    <div>
        <form enctype="multipart/form-data" class="login_form" method="post">
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
    </body>
</html>"""
    elif f.request.method == 'POST':
        img = f.request.files['file']
        with open(r'static/img/icon.png', 'wb') as i:
            i.write(img.read())
        return f"""<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{f.url_for('static', filename='css/style.css')}" />
    <title>Отбор астронафтов</title>
    </head>
    <body>
    <h1>Загрузка фотографии</h1>
    <h3>для участия в миссии</h3>
    <div>
        <form enctype="multipart/form-data" class="login_form" method="post">
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <br>
            <img src='{f.url_for('static', filename='img/icon.png')}' width=200px>
            <br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
    </body>
</html>"""
    
@app.route('/carousel')
def carousel():
    return f"""<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="{f.url_for('static', filename='css/style.css')}">
    <title>Пейзажи Марса</title>
    </head>
    <body>
        <h1>Пейзажи Марса</h1>
        <div id="carouselExampleIndicators" class="carousel slide">
            <div class="carousel-indicators">
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active u" aria-current="true" aria-label="Slide 1"></button>
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" class="u" aria-label="Slide 2"></button>
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" class="u" aria-label="Slide 3"></button>
            </div>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img src="{f.url_for('static', filename='img/mars1.jpg')}" style="height: 400px; width: 80px;" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="{f.url_for('static', filename='img/mars2.jpg')}" style="height: 400px; width: 80px;" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="{f.url_for('static', filename='img/mars3.jpg')}" style="height: 400px; width: 80px;" class="d-block w-100" alt="...">
              </div>
            </div>
            
          </div>
    </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
