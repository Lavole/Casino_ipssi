import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Bonjour ! </h1>
    <p> bla bla bla </p>
</body>
</html>
"""

print(html)