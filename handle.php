<html>
<body>
<a href="index.html">back</a><br><br>
Results:
<?php
  $output = array();
  $a = "python main.py " . $_POST["question"];
  exec($a, $output);
  foreach($output as $item) {
    echo "<li>".$item."</li>";
  }

?><br>


</body>
</html>
