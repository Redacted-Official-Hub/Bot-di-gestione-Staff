import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio
import json

# Configura il bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Carica dati dello staff
def load_staff():
    try:
        with open("staff.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Salva dati dello staff
def save_staff(data):
    with open("staff.json", "w") as f:
        json.dump(data, f, indent=4)

staff_data = load_staff()

# Sincronizza i comandi slash
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} è online!")

# Comando per aggiungere staff
@bot.tree.command(name="add_staff", description="Aggiungi un membro dello staff")
@app_commands.describe(user="Utente da aggiungere", role="Ruolo dello staff")
async def add_staff(interaction: discord.Interaction, user: discord.Member, role: str):
    staff_data[str(user.id)] = {"name": user.name, "role": role}
    save_staff(staff_data)
    embed = discord.Embed(title="✅ Staff Aggiunto", description=f"{user.mention} è stato aggiunto come **{role}**", color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

# Comando per rimuovere staff
@bot.tree.command(name="remove_staff", description="Rimuovi un membro dello staff")
@app_commands.describe(user="Utente da rimuovere")
async def remove_staff(interaction: discord.Interaction, user: discord.Member):
    if str(user.id) in staff_data:
        del staff_data[str(user.id)]
        save_staff(staff_data)
        embed = discord.Embed(title="❌ Staff Rimosso", description=f"{user.mention} è stato rimosso dallo staff!", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Questo utente non è nello staff!", ephemeral=True)

# Comando per vedere lo staff
@bot.tree.command(name="staff_list", description="Mostra la lista dello staff")
async def staff_list(interaction: discord.Interaction):
    if not staff_data:
        await interaction.response.send_message("Nessun membro dello staff registrato!", ephemeral=True)
    else:
        embed = discord.Embed(title="📋 Lista dello Staff", color=discord.Color.blue())
        for data in staff_data.values():
            embed.add_field(name=data['name'], value=f"Ruolo: **{data['role']}**", inline=False)
        await interaction.response.send_message(embed=embed)

# Comando per modificare il ruolo di un membro dello staff
@bot.tree.command(name="update_role", description="Aggiorna il ruolo di un membro dello staff")
@app_commands.describe(user="Utente", new_role="Nuovo ruolo")
async def update_role(interaction: discord.Interaction, user: discord.Member, new_role: str):
    if str(user.id) in staff_data:
        staff_data[str(user.id)]["role"] = new_role
        save_staff(staff_data)
        embed = discord.Embed(title="🔄 Ruolo Aggiornato", description=f"Ruolo di {user.mention} aggiornato a **{new_role}**!", color=discord.Color.orange())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Questo utente non è nello staff!", ephemeral=True)

# Comando per inviare un annuncio allo staff
@bot.tree.command(name="announce", description="Invia un annuncio allo staff")
@app_commands.describe(message="Messaggio da inviare")
async def announce(interaction: discord.Interaction, message: str):
    for member_id in staff_data.keys():
        member = interaction.guild.get_member(int(member_id))
        if member:
            try:
                await member.send(f"📢 Annuncio dallo staff: {message}")
            except:
                await interaction.response.send_message(f"Impossibile inviare il messaggio a {member.name}", ephemeral=True)
    embed = discord.Embed(title="📢 Annuncio Staff", description=message, color=discord.Color.purple())
    await interaction.response.send_message(embed=embed)

# Comando per impostare un promemoria
@bot.tree.command(name="remind", description="Imposta un promemoria")
@app_commands.describe(time="Tempo in secondi", message="Messaggio del promemoria")
async def remind(interaction: discord.Interaction, time: int, message: str):
    embed = discord.Embed(title="⏳ Promemoria Impostato", description=f"Il promemoria verrà inviato tra **{time}** secondi!", color=discord.Color.gold())
    await interaction.response.send_message(embed=embed)
    await asyncio.sleep(time)
    await interaction.followup.send(f"🔔 **Promemoria:** {message}")

# Comando di aiuto
@bot.tree.command(name="help_staff", description="Mostra i comandi disponibili per lo staff")
async def help_staff(interaction: discord.Interaction):
    embed = discord.Embed(title="📜 Comandi Disponibili", color=discord.Color.blue())
    embed.add_field(name="/add_staff @utente ruolo", value="Aggiunge un membro dello staff", inline=False)
    embed.add_field(name="/remove_staff @utente", value="Rimuove un membro dello staff", inline=False)
    embed.add_field(name="/staff_list", value="Mostra la lista dello staff", inline=False)
    embed.add_field(name="/update_role @utente nuovo_ruolo", value="Modifica il ruolo di un membro", inline=False)
    embed.add_field(name="/announce messaggio", value="Invia un messaggio privato a tutto lo staff", inline=False)
    embed.add_field(name="/remind tempo messaggio", value="Imposta un promemoria", inline=False)
    embed.add_field(name="/help_staff", value="Mostra questo messaggio di aiuto", inline=False)
    await interaction.response.send_message(embed=embed)

# Avvia il bot
TOKEN = "MTM1MzMxOTMwMzc4ODg4ODE1NA.GWAD_C.ioDWQHRCVT_1D0PdwYWOvjwMipEnpJ_G2ElMg4"
bot.run(TOKEN)