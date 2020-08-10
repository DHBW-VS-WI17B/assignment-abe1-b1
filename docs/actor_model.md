# Aktorenmodell

Das Aktorenmodell stellt eine Alternative zur Thread-Programmierung dar.
Die nebenläufige Programmierungen kann u. U. zu unerwünschten Effekten wie bspw. Race Conditions führen.

> Synchronisation gewährleistet Atomizität und Sichtbarkeit.

Aber auch die Synchronisation kann aufgrund von `Shared mutablity` zu Problemen wie bspw. Deadlocks führen. 
Aus diesem Grund besitzt das Aktorenmodell sogenannte `Aktoren`, die vollständig voneinander isoliert sind und keine gemeinsamen Speicherbereiche nutzen.

Ein Aktor ist die primitive Einheit der Berechnung und besitzt einen bestimmten Zustand.

Aktoren kommen immer in Systemen. 
Jeder Aktor besitzt eine Adresse, an die ein anderer Aktor eine Botschaft senden kann.
Botschaften sind unveränderliche Nachrichten.

Aktoren verarbeiten eingehende Nachrichten sequenziell (`FIFO-Verfahren`).
Aus diesem Grund warten eingehende Nachrichten in der sogenannten `Mailbox` eines Aktors.
Damit mehrere Nachrichten gleichzeitig verarbeitet werden können, muss jede Nachricht an einen anderen Aktor gesendet werden.

Aktoren können mit den folgenden drei Tätigkeiten auf Nachrichten reagieren:  
1. Nachrichten an sich oder andere Aktoren senden
2. Neue Aktoren erzeugen
3. Verhalten oder Zustand ändern

-----------
Quelle 1: `Aktoren.pdf` von Prof. Dr. Wolfgang Funk.  
Quelle 2: https://www.youtube.com/watch?v=7erJ1DV_Tlo
