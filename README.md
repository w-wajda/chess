# REST Chess solver

Aplikacja REST wspomagająca grę w szachy.

# Instalacja

`pipenv install`

# Uruchomienie aplikacji

Aktywujemy środowisko wirtualne:

`pipenv shell`

Uruchamiamy serwer:

`./run.sh`

# Przykładowe zapytania

#### [GET] `/api/v1/{chess-figure}/{current-field}` (wyświetla listę możliwych ruchów)

Przykładowe zapytanie:
`curl http://localhost:5000/api/v1/rook/h2`

Przykładowa odpowiedź:

```json
{
  "availableMoves": [
    "A2", 
    "B2", 
    "C2", 
    "D2", 
    "E2", 
    "F2", 
    "G2", 
    "H1", 
    "H3", 
    "H4", 
    "H5", 
    "H6", 
    "H7", 
    "H8"
  ], 
  "currentField": "H2", 
  "error": null, 
  "figure": "rook"
}
```

Przykładowe zapytanie:
`curl http://localhost:5000/api/v1/rook/h15`

Przykładowa odpowiedź:

```json
{
  "availableMoves": [], 
  "currentField": "H15", 
  "error": "Field does not exist.", 
  "figure": "rook"
}
```

####  [GET] `/api/v1/{chess-figure}/{current-field}/{dest-field}` (waliduje czy ruch na wskazane pole jest poprawny)

Przykładowe zapytanie:
`curl http://localhost:5000/api/v1/rook/h2/h3`

Przykładowa odpowiedź:

```json
{
  "currentField": "H2", 
  "destField": "H3", 
  "error": null, 
  "figure": "rook", 
  "move": "valid"
}
```

Przykładowe zapytanie:
`curl http://localhost:5000/api/v1/rook/h2/h1`

Przykładowa odpowiedź:

```json
{
  "currentField": "H2", 
  "destField": "H1", 
  "error": null, 
  "figure": "rook", 
  "move": "valid"
}
```