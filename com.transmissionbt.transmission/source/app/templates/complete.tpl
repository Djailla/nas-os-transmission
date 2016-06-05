<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Transmission setup</title>
    <script type="text/JavaScript">
      var request = new XMLHttpRequest();
      request.onreadystatechange = function() {
          if (request.readyState === 4) {
              if (request.status === 200) {
                  document.body.className = 'ok';
                  console.log(request.responseText);
              } else {
                  document.body.className = 'error';
              }
          }
      };
      request.open("GET", "restart" , true);
      request.send(null);

      function timeRefresh(timeoutPeriod)
      {
        setTimeout("window.location.href = \"web\";", timeoutPeriod);
      }
    </script>
  </head>
  <body onload="JavaScript:timeRefresh(5000);">
    <h1>Transmission setup complete</h1>
    <h2>Page will reload automatically in 5 seconds</h2>
  </body>
</html>
