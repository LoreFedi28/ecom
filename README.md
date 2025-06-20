# Sito E-Commerce – Progetto Django

## Descrizione

Questo progetto è un sito e-commerce sviluppato con Django. Permette agli utenti di registrarsi, navigare tra i prodotti, aggiungerli al carrello e completare un ordine tramite checkout. È stato distribuito online tramite Railway.

---

## Funzionalità principali

- **Registrazione e login utenti**
  - Gli utenti possono registrarsi, accedere, aggiornare il proprio profilo e cambiare password.
  - Esistono due gruppi con permessi distinti: **clienti** e **store manager**.

- **Navigazione tra i prodotti**
  - I prodotti sono organizzati in **categorie**.
  - Ogni prodotto ha una pagina di dettaglio.
  - È possibile cercare e filtrare i prodotti.

- **Carrello**
  - Il carrello è basato su sessione e si aggiorna in modo dinamico.
  - È possibile aggiungere, rimuovere prodotti e vedere il totale.

- **Checkout e ordini**
  - L’utente può inserire le informazioni di fatturazione e concludere l’acquisto.
  - Gli ordini vengono salvati e possono avere stato “spedito” o “non spedito”.
  - Gli store manager possono vedere tutti gli ordini, gestirli e aggiornarne lo stato.

- **Profilo utente**
  - La classe `User` di Django è estesa con un modello personalizzato (`Profile`) per salvare informazioni aggiuntive.

- **Permessi e gruppi**
  - I clienti possono solo vedere e modificare il proprio profilo.
  - Gli store manager hanno accesso a dashboard di gestione ordini.

---

## Come usare il sito

### Link al sito online

👉 [https://ecom-production-14d9.up.railway.app/](https://ecom-production-14d9.up.railway.app/)

### Passaggi principali

1. **Registrati** come nuovo utente oppure **accedi** se hai già un account.
2. **Naviga** tra i prodotti e le categorie.
3. **Aggiungi** al carrello i prodotti desiderati.
4. Vai al **checkout**, inserisci le informazioni e conferma l’ordine.
5. Se sei uno **store manager**, accedi alla sezione di gestione ordini per spuntare quelli spediti.

---

## Struttura del progetto

- `store/` – gestione prodotti, categorie, utenti e profili
- `cart/` – logica del carrello (basata su sessione)
- `payment/` – gestione ordini, checkout, dashboard amministrazione
- `ecom/` – configurazioni globali del progetto

---

## Tecnologie utilizzate

- **Backend**: Django 4.x
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (sviluppo) / PostgreSQL (produzione)
- **Deploy**: Railway (Procfile + Gunicorn)

---

## Avvio in locale

1. Clonare il progetto
2. Installare le dipendenze:
   ```bash
   pip install -r requirements.txt

	3.	Creare il file .env con le variabili d’ambiente necessarie
	4.	Applicare le migrazioni:

python manage.py migrate


	5.	Creare un superuser:

python manage.py createsuperuser


	6.	Avviare il server:

python manage.py runserver



⸻

Autore

Lorenzo Fedi
Studente di Ingegneria Informatica – A.A. 2025
