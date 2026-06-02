# Cegid Revo - Technical Test

Aquest repositori conté la resolució de la prova tècnica per a la posició d'iOS/Swift Developer.

S'ha optat per utilitzar **Python** per a la resolució de tots els exercicis amb l'objectiu de prioritzar la claredat, la lògica de negoci i l'arquitectura de programari per demostrar els fonaments de l'enginyeria.

## Estructura i decisions tècniques:

* **Exercici 1 (Collections 1):** Ús de funcions d'ordre superior (`map`) per evitar bucles tradicionals, aplicant el principi Open/Closed per a l'extensibilitat i una aproximació TDD. Inclou integració amb l'API real de GitHub.
* **Exercici 2 (Collections 2):** Ús combinat de `filter` i `map` amb funcions anònimes per processar dades JSON anidades, mantenint la puresa funcional i la prevenció d'errors.
* **Exercici 3 (Refactor & Testing):**
   - **Video Store Refactor:** Desacoblament de la lògica de la classe `Customer` implementant el patró de disseny **Strategy**. Això permet afegir nous tipus de preus i formats de sortida (HTML/XML) de manera escalable, complint estrictament el principi de Responsabilitat Única (SRP) i Obert/Tancat (OCP).
   - **Primes TDD:** Resolució de l'algorisme de nombres primers aplicant el cicle Red-Green-Refactor mitjançant la llibreria `unittest`.