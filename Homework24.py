from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

books = []
next_id = 1

base_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            background:#f4f4f4;
            margin:0;
        }

        nav{
            background:#2c3e50;
            padding:15px;
            text-align:center;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin:0 15px;
            font-weight:bold;
        }

        .container{
            width:90%;
            max-width:1200px;
            margin:20px auto;
        }

        form{
            background:white;
            padding:15px;
            border-radius:10px;
            margin-bottom:20px;
        }

        input, textarea{
            width:100%;
            padding:10px;
            margin:5px 0;
        }

        button{
            padding:10px;
            border:none;
            cursor:pointer;
            color:white;
        }

        .add-btn{
            background:green;
        }

        .delete-btn{
            background:red;
        }

        .books{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:15px;
        }

        .card{
            background:white;
            padding:15px;
            border-radius:10px;
        }

        footer{
            text-align:center;
            background:#2c3e50;
            color:white;
            padding:15px;
            margin-top:20px;
        }
    </style>
</head>
<body>

<nav>
    <a href="/">Головна</a>
    <a href="/about-me">Про себе</a>
    <a href="/about-library">Про бібліотеку</a>
</nav>

<div class="container">
{{ content|safe }}
</div>

<footer>
    © 2026 Моя бібліотека
</footer>

</body>
</html>
"""


@app.route("/")
def index():
    books_html = ""

    for book in books:
        books_html += f"""
        <div class="card">
            <h3>{book['title']}</h3>
            <p><b>Автор:</b> {book['author']}</p>
            <p><b>Рік:</b> {book['year']}</p>
            <p><b>Жанр:</b> {book['genre']}</p>
            <p>{book['description']}</p>

            <form action="/delete/{book['id']}" method="POST">
                <button class="delete-btn">
                    Видалити
                </button>
            </form>
        </div>
        """

    content = f"""
    <h1>Каталог книг</h1>

    <form action="/add" method="POST">

        <input type="text"
               name="title"
               placeholder="Назва книги"
               required>

        <input type="text"
               name="author"
               placeholder="Автор"
               required>

        <input type="number"
               name="year"
               placeholder="Рік видання">

        <input type="text"
               name="genre"
               placeholder="Жанр">

        <textarea name="description"
                  placeholder="Опис"></textarea>

        <button class="add-btn" type="submit">
            Додати книгу
        </button>

    </form>

    <div class="books">
        {books_html}
    </div>
    """

    return render_template_string(
        base_template,
        title="Бібліотека",
        content=content
    )


@app.route("/add", methods=["POST"])
def add_book():
    global next_id

    title = request.form["title"].strip()
    author = request.form["author"].strip()

    if title and author:
        books.append({
            "id": next_id,
            "title": title,
            "author": author,
            "year": request.form.get("year", ""),
            "genre": request.form.get("genre", ""),
            "description": request.form.get("description", "")
        })

        next_id += 1

    return redirect(url_for("index"))


@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book():
    global books

    books[:] = [book for book in books if book["id"] != book_id]

    return redirect(url_for("index"))


@app.route("/about-me")
def about_me():
    content = """
    <h1>Про себе</h1>

    <img src="https://via.placeholder.com/200">

    <p>
        Мене звати Іван.
        Я вивчаю Python та Flask.
    </p>

    <p>Email: ivan@example.com</p>
    """

    return render_template_string(
        base_template,
        title="Про себе",
        content=content
    )


@app.route("/about-library")
def about_library():
    content = """
    <h1>Про бібліотеку</h1>

    <p>
        Навчальний Flask-проєкт для
        зберігання книг.
    </p>

    <h3>Місія</h3>

    <p>
        Допомогти користувачам
        вести власний каталог книг.
    </p>

    <p>
        Адреса: вул. Книжкова, 10
    </p>

    <p>
        Графік роботи: 09:00 - 18:00
    </p>
    """

    return render_template_string(
        base_template,
        title="Про бібліотеку",
        content=content
    )


if __name__ == "__main__":
    app.run(debug=True)
