# LogisticsFlow – Development Plan

## Etap 1. Przygotowanie projektu

- Utworzenie struktury katalogów.
- Konfiguracja środowiska Python.
- Instalacja bibliotek.
- Inicjalizacja Git.

## Etap 2. Dokumentacja

- Wymagania projektu.
- Projekt bazy danych.
- Diagram ERD.
- Plan rozwoju.

## Etap 3. Konfiguracja aplikacji

- Uruchomienie FastAPI.
- Konfiguracja PostgreSQL.
- Konfiguracja SQLAlchemy.
- Konfiguracja Alembic.

## Etap 4. Modele i baza danych

- Model Customer.
- Migracje bazy danych.
- Kolejne modele zgodnie z projektem ERD.

## Etap 5. Klienci

- Dodawanie klientów.
- Pobieranie klientów.
- Aktualizacja klientów.
- Usuwanie klientów.
- Testy funkcjonalności.

## Etap 6. Zlecenia transportowe

- Tworzenie zleceń.
- Pobieranie zleceń.
- Aktualizacja i anulowanie.
- Obsługa statusów.
- Testy.

## Etap 7. Punkty transportowe i trasy

- Punkty załadunku i rozładunku.
- Lokalizacje.
- Odległości i odcinki tras.
- Testy.

## Etap 8. Kierowcy i pojazdy

- Modele kierowców i pojazdów.
- Przypisywanie zasobów do zleceń.
- Obsługa maksymalnie dwóch kierowców.
- Testy.

## Etap 9. Zdarzenia i logowanie

- Historia zdarzeń transportowych.
- Wzorzec Decorator.
- Logowanie rozpoczęcia, zakończenia i błędów operacji.
- Testy.

## Etap 10. Dalszy rozwój

- Uwierzytelnianie.
- CI/CD.
- Przygotowanie do wdrożenia.

## Zasada realizacji

Funkcjonalności implementujemy stopniowo. Każdy etap kończymy testami i commitem Git.
