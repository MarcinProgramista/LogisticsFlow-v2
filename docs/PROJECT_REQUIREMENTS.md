# LogisticsFlow – Project Requirements

## 1. Cel projektu

LogisticsFlow to aplikacja backendowa wspierająca zarządzanie procesami logistycznymi i transportowymi.

System będzie obsługiwał transporty FTL (Full Truck Load) oraz LTL (Less Than Truckload).

Głównym celem MVP jest zarządzanie zleceniami transportowymi i monitorowanie ich realizacji.

## 2. Główne funkcjonalności

### 2.1. Klienci

- Dodawanie klientów.
- Pobieranie listy klientów i szczegółów klienta.
- Aktualizacja danych klienta.
- Usuwanie klientów.

### 2.2. Zlecenia transportowe

- Tworzenie zleceń transportowych.
- Pobieranie zleceń i szczegółów zlecenia.
- Aktualizacja zleceń.
- Anulowanie zleceń.
- Przypisanie zlecenia do klienta.

### 2.3. Ładunki

Każde zlecenie może zawierać informacje o:

- rodzaju ładunku,
- wadze,
- liczbie palet,
- wymiarach,
- wymaganiach specjalnych.

### 2.4. Punkty załadunku i rozładunku

- Obsługa wielu punktów na jednym zleceniu.
- Rozróżnienie punktów PICKUP i DELIVERY.
- Adres, planowana data, osoba kontaktowa.
- Kolejność realizacji punktów.

### 2.5. Kierowcy i pojazdy

- Zarządzanie kierowcami.
- Zarządzanie pojazdami.
- Przypisywanie pojazdów do zleceń.
- Możliwość przypisania jednego lub dwóch kierowców do transportu.

### 2.6. Monitorowanie transportu

- Aktualizacja statusu zlecenia.
- Rejestrowanie zdarzeń transportowych.
- Zapisywanie opóźnień i awarii.
- Historia zdarzeń dla każdego zlecenia.

## 3. Statusy zleceń

System będzie obsługiwał następujące statusy:

- `NEW` – nowe zlecenie.
- `PLANNED` – zlecenie zaplanowane.
- `IN_PROGRESS` – transport w trakcie realizacji.
- `COMPLETED` – transport zakończony.
- `CANCELLED` – zlecenie anulowane.

Nowe zlecenie otrzymuje status `NEW`.

Zmiany statusów muszą uwzględniać dozwolone przejścia pomiędzy statusami.

## 4. Wymagania techniczne

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Pytest

## 5. Architektura

Projekt będzie podzielony na warstwy:

- `routers` – obsługa endpointów API.
- `schemas` – walidacja danych i schematy Pydantic.
- `models` – modele bazy danych.
- `services` – logika biznesowa.
- `database` – konfiguracja połączenia z bazą danych.

## 6. Wzorce projektowe

W projekcie zostanie zastosowany wzorzec **Decorator**.

Jego zadaniem będzie logowanie:

- rozpoczęcia operacji biznesowej,
- poprawnego zakończenia operacji,
- wystąpienia błędu.

## 7. Testowanie

Testy będą tworzone równolegle z implementacją funkcjonalności.

Wykorzystamy Pytest do testowania:

- logiki biznesowej,
- operacji na danych,
- endpointów API,
- obsługi błędów.

## 8. Zakres MVP

Pierwsza wersja projektu będzie koncentrować się na:

1. Zarządzaniu klientami.
2. Zarządzaniu zleceniami transportowymi.
3. Obsłudze punktów załadunku i rozładunku.
4. Zarządzaniu kierowcami i pojazdami.
5. Przypisywaniu zasobów do transportów.
6. Statusach i historii zdarzeń.

Dalsze funkcjonalności będą rozwijane etapami.
