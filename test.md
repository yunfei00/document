## AT command for produce

* GET SOFEWARE VERSION : `printf "AT+VERSION\r\n" | nc localhost 6777`
* TURN ON DEPTH : `printf "AT+DEPTH=ON\r\n" | nc localhost 6777`
* TURN OFF DEPTH : `printf "AT+DEPTH=OFF\r\n" | nc localhost 6777`
* TURN ON IR : `printf "AT+IR=ON\r\n" | nc localhost 6777`
* TURN OFF IR : `printf "AT+IR=OFF\r\n" | nc localhost 6777`
* TURN ON FISHEYE : `printf "AT+FISHEYE=ON\r\n" | nc localhost 6777`
* TURN OFF FISHEYE : `printf "AT+FISHEYE=OFF\r\n" | nc localhost 6777`
* TURN ON POSE DETECT : `printf "AT+POSE=ON\r\n" | nc localhost 6777`
* TURN OFF POSE DETECT : `printf "AT+POSE=OFF\r\n" | nc localhost 6777`
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA3MjgxNjgxN119
-->