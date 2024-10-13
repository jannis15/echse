# Echse
 
Ein Fullstack-Projekt zum Tracken der Zeit diverser Windows-Programme (.exe).

- Frontend: Flutter (Dart)
- Backend: FastAPI (Python)

Das Backend fragt jede Minute über die win32-API die aktuell laufenden Prozessdaten ab und speichert diese in einer SQLite-Datenbank.

Das Frontend kann über die REST-Schnittstelle Programme sortiert nach laufender Dauer abfragen und anzeigen.

![305243448-67dbf41e-4b39-43a5-b8d0-16bc855ceb4b](https://github.com/user-attachments/assets/40ef3808-c072-4117-be45-00fffdf67188)
