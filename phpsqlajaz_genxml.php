<?php error_reporting(-1); ?>
<?php ini_set('display_errors', true); ?>
<?php

// Start XML file, create parent node
$dom = new DOMDocument("1.0");
$node = $dom->createElement("gps_data");
$parnode = $dom->appendChild($node);

// Opens a connection to a mySQL server
$connection=@mysql_connect ("127.0.0.1", "root", "shrikanth");
if (!$connection) {
  die("Not connected : " . mysql_error());
}

// Set the active mySQL database
$db_selected = mysql_select_db("GPSDB", $connection);
if (!$db_selected) {
  die ("Can\'t use db : " . mysql_error());
}

// Search the rows in the markers table
$query = "SELECT * FROM GPS WHERE 1";
$result = mysql_query($query);

$result = mysql_query($query);
if (!$result) {
  die("Invalid query: " . mysql_error());
}

header("Content-type: text/xml");

// Iterate through the rows, adding XML nodes for each
while ($row = @mysql_fetch_assoc($result)){
  $node = $dom->createElement("gps_data");
  $newnode = $parnode->appendChild($node);
  $newnode->setAttribute("device", $row['device']);
  $newnode->setAttribute("lat", $row['lat']);
  $newnode->setAttribute("lng", $row['lng']);
}

echo $dom->saveXML();
?>

