<html>
<body>
<a href="index.html">back</a><br><br>
Results:
<?php
  $output = array();
  $a = "python main.py " . $_POST["question"];
  exec($a, $output);
  echo var_dump($output);
?><br>


</body>
</html>
