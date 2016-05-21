import socket
import MySQLdb

db = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 15000)
print('starting up on %s port %s' % server_address)

sock.bind(server_address)
sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(100)
            print('received "%s"' % data)
            if data:
                bin_data = []
                data_str = data
                data_str = data_str.split(" ")
                data_d = map(float, data_str)
                if len(data_d) == 3: 
                   if (data_d[0] in db) == False:
                      #insert new entry..
                      print("opening sqldb\n")
                      sqldb = MySQLdb.connect("localhost","root","shrikanth","GPSDB")
                      sql = "INSERT INTO GPS (`device`, `lat`, `lng`) VALUES('%d', '%f', '%f')" % (data_d[0], data_d[1], data_d[2])
                      try: 
                         print("inserting new value")
                         cursor = sqldb.cursor()
                         cursor.execute(sql)
                         sqldb.commit()
                      except:
                         print("error while inserting to sqldb\n")
                         
                         sqldb.rollback()
                      sqldb.close()
                   else: 
                      sgldb = MySQLdb.connect("localhost", "root", "shrikanth", "GPSDB")
                      sql = "UPDATE GPS SET lat=%f, lng=%f" % (data_d[1], data_d[2]) + " WHERE device=%d" % data_d[0]
                      print(sql)
                      try:
                         print("Updating exisitng entry\n")
                         cursor = sqldb.cursor()
                         cursor.execute(sql)
                         sqldb.commit()
                      except:
                         print("error while updating")
                         sqldb = MySQLdb.connect("localhost","root","shrikanth","GPSDB")
                         sqldb.rollback()
                      sqldb.close()       

                   db[data_d[0]] = (data_d[1], data_d[2]) 
                
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
    print(db)


