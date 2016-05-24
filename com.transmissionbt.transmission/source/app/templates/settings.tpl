<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Transmission setup</title>
  </head>
  <body>
    <h1>Transmission setup</h1>
    <form action="save" method="post">
      <h2>Download destination path</h2>
      <select name="dest_path">
        {{ path_list }}
      </select>
      <input class="btn" value="Save" type="submit" />
    </form>
  </body>
</html>
