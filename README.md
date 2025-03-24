# 🤖 Discord Staff Manager Bot

Un bot per Discord che gestisce lo staff del server con comandi **Slash**! 🚀  
Permette di **aggiungere, rimuovere e aggiornare i membri dello staff**, inviare **annunci**, impostare **promemoria** e molto altro.

## ✨ Funzionalità
- ✅ **Aggiunta e rimozione staff** con ruoli personalizzabili  
- 🔄 **Aggiornamento del ruolo dello staff**  
- 📋 **Visualizzazione della lista dello staff**  
- 📢 **Invio di annunci privati ai membri dello staff**  
- ⏳ **Impostazione di promemoria temporizzati**  
- 🔒 **Permessi personalizzabili**: Solo utenti con un determinato ruolo (o superiore) possono eseguire i comandi  

## 🎯 Requisiti
- Python 3.8+  
- Libreria `discord.py` (`pip install discord`)  

## 🚀 Installazione e Configurazione
1. **Clona il repository**  
   ```bash
   git clone https://github.com/TUO-NOME/discord-staff-bot.git
   cd discord-staff-bot
   ```

2. **Installa le dipendenze**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura il token del bot**  
   Sostituisci `IL_TUO_TOKEN_DISCORD` nel codice con il token del tuo bot.

4. **Esegui il bot**  
   ```bash
   python bot.py
   ```

## 🛠️ Comandi disponibili
| Comando        | Descrizione |
|---------------|------------|
| `/add_staff @utente ruolo` | Aggiunge un utente allo staff |
| `/remove_staff @utente` | Rimuove un membro dallo staff |
| `/staff_list` | Mostra la lista dello staff |
| `/update_role @utente nuovo_ruolo` | Modifica il ruolo di un membro dello staff |
| `/announce messaggio` | Invia un annuncio privato allo staff |
| `/remind tempo messaggio` | Imposta un promemoria dopo X secondi |

## 🛡️ Autorizzazioni richieste
Il bot richiede le seguenti autorizzazioni per funzionare correttamente:
- **Gestione ruoli** (se deve assegnare ruoli automaticamente)
- **Inviare messaggi privati**
- **Utilizzare comandi slash**

## 📜 Licenza
Questo progetto è distribuito sotto licenza MIT.
