# tech_engage_smart_bins

Instruction to run:

1. tinyGPS++.cpp, tinyGPS.h file implement GPS library routines. copy them to the same place as gps.ino file. and upload them to an Arduino Uno Board. Open Serial Monitor to see the GPS Info. 
2. server.py and client.py files implement web socket in python. they are used to send info to server from bins
3. you need to create a mysgl database named "GPSDB" and need to run create_mysql_table.py file before starting web sockets..
4. start apache2 server on localhost.
5. open localhost/phpsqlajax_map_v3.html in browser
