<html>
<body>
<a href="index.html">back</a><br>
Results:
<?php
  $output = array();
  $a = "python main.py " . $_POST["question"];
  exec($a, $output);
  echo $output[0];
?><br>


</body>
</html>
