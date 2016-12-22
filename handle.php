<html>
<body>
<a href="index.html">back</a><br><br>
Results:
<?php
  $output = array();
  $a = "python main.py " . $_POST["question"];
  exec($a, $output);
  echo '<table border="1">';
  foreach($output as $item) {
    echo "<tr>";
    $subRow = explode(',', $item);
    foreach($subRow as $subItem) {
      echo "<td>".$subItem."</td>";
    }
    echo "</tr>";
  }
  echo "</table>";
?><br>


</body>
</html>
