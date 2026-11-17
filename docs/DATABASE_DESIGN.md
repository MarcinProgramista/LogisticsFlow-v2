# LogisticsFlow – Database Design

## 1. CUSTOMERS

Dane klientów korzystających z usług transportowych.

Relacja:

- Jeden klient może posiadać wiele zleceń transportowych (1:N).

## 2. TRANSPORT_ORDERS

Główna tabela zleceń transportowych.

Przechowuje:

- identyfikator klienta (`customer_id`),
- dane zlecenia,
- status,
- informacje o ładunku.

Relacja:

- Każde zlecenie należy do jednego klienta.
- Jedno zlecenie może mieć wiele punktów transportowych.

## 3. LOCATIONS

Słownik lokalizacji.

Przechowuje:

- miasto,
- kod pocztowy.

Kombinacja miasta i kodu pocztowego jest unikalna.

Lokalizacje są wykorzystywane w punktach transportowych i trasach.

## 4. ORDER_STOPS

Punkty załadunku i rozładunku.

Przechowuje:

- `transport_order_id`,
- typ punktu: `PICKUP` lub `DELIVERY`,
- lokalizację,
- kolejność realizacji,
- planowaną datę,
- dane kontaktowe.

Relacja:

- Jedno zlecenie może mieć wiele punktów transportowych (1:N).

## 5. ROUTE_DISTANCES

Tabela przechowująca odległości między lokalizacjami.

Przechowuje:

- lokalizację początkową,
- lokalizację docelową,
- odległość w kilometrach.

Trasy są kierunkowe:

- A → B i B → A są osobnymi rekordami.
- Kombinacja lokalizacji początkowej i docelowej jest unikalna.
- Odległość jest wprowadzana ręcznie.

## 6. ORDER_ROUTE_SEGMENTS

Tabela łącząca zlecenia z odcinkami tras.

Przechowuje:

- `transport_order_id`,
- `from_stop_id`,
- `to_stop_id`,
- `route_distance_id`,
- `distance_km`.

`distance_km` jest kopią historycznej odległości. Zmiana domyślnej odległości w `ROUTE_DISTANCES` nie zmienia historii istniejącego zlecenia.

Całkowity dystans wielopunktowego transportu jest sumą odcinków.

## 7. VEHICLES

Dane pojazdów wykorzystywanych w transporcie.

## 8. DRIVERS

Dane kierowców realizujących transporty.

## 9. ORDER_ASSIGNMENTS

Tabela pośrednicząca między zleceniami transportowymi i pojazdami.

Relacja:

- Zlecenia i pojazdy tworzą relację wiele do wielu (N:M).

## 10. ASSIGNMENT_DRIVERS

Tabela przypisująca kierowców do konkretnego przydziału pojazdu i zlecenia.

Zasada:

- Do jednego przydziału można przypisać maksymalnie dwóch kierowców.

## 11. ORDER_EVENTS

Historia zdarzeń dotyczących zlecenia.

Przechowuje:

- typ zdarzenia,
- opis,
- datę i czas zdarzenia.

Relacja:

- Jedno zlecenie może mieć wiele zdarzeń (1:N).

## 12. Podsumowanie relacji

- CUSTOMERS 1:N TRANSPORT_ORDERS
- TRANSPORT_ORDERS 1:N ORDER_STOPS
- LOCATIONS 1:N ORDER_STOPS
- TRANSPORT_ORDERS N:M VEHICLES (przez ORDER_ASSIGNMENTS)
- ORDER_ASSIGNMENTS 1:N ASSIGNMENT_DRIVERS
- DRIVERS 1:N ASSIGNMENT_DRIVERS
- TRANSPORT_ORDERS 1:N ORDER_EVENTS
- TRANSPORT_ORDERS 1:N ORDER_ROUTE_SEGMENTS
- ROUTE_DISTANCES 1:N ORDER_ROUTE_SEGMENTS
