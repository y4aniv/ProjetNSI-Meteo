# > Importer les modules nécessaires
import random
import os
from datetime import datetime, timedelta

# > Définir les fonctions
def clearConsole():
    """
    Nettoie la console

    Entrée: Aucune
    Sortie: Aucune
    """
    # Si le système d'exploitation est Windows, utiliser la commande 'cls' sinon utiliser 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def randomWeather():
    """
    Retourne une météo aléatoire avec une chance de 2/3 d'avoir du soleil et 1/3 d'avoir de la pluie

    Entrée: Aucune
    Sortie: 'rainy' ou 'sunny' (string)
    """
    return random.choice(['rainy', 'sunny', 'sunny'])

def randomTemperature(weather):
    """
    Retourne une température aléatoire en fonction de la météo

    Entrée: weather (string)
    Sortie: temperature (int)
    """
    if weather == 'rainy':
        return random.randint(10, 20)
    else:
        return random.randint(20, 30)

def randomExpense():
    """
    Retourne un prix aléatoire dépensé par les retraités

    Entrée: Aucune
    Sortie: price (int)
    """
    return random.randint(20, 40)

def parseHistoryWeather(historyWeather):
    """
    Retourne l'historique de la météo sous forme d'émoticônes

    Entrée: historyWeather (list)
    Sortie: historyWeatherText (string)
    """
    # Définir les variables
    historyWeatherText = ''

    # Parcourir la liste historyWeather
    for weather in historyWeather:
        # Ajouter un émoticône en fonction de la météo
        if weather == 'rainy':
            historyWeatherText += '🌧️ '
        else:
            historyWeatherText += '☀️ '

    # Retourner l'historique de la météo
    return historyWeatherText

def parseHistoryTemperature(historyTemperature):
    """
    Retourne l'historique de la température sous forme de graphique avec des flèches

    Entrée: historyTemperature (list)
    Sortie: historyTemperatureText (string)
    """
    # Définir les variables
    historyTemperatureText = ''
    
    # Parcourir la liste historyTemperature
    for i in range(len(historyTemperature)):
        temperature = historyTemperature[i]
        historyTemperatureText += str(temperature) + '°C'
        
        # Vérifier s'il y a une température suivante dans la liste
        if i < len(historyTemperature) - 1:
            next_temperature = historyTemperature[i + 1]
            
            # Ajouter ↗️ si la température est inférieure à la température suivante
            if temperature < next_temperature:
                historyTemperatureText += ' ↗️ '
            # Ajouter ↘️ si la température est supérieure à la température suivante
            elif temperature > next_temperature:
                historyTemperatureText += ' ↘️ '
            # Ajouter ↔️ si la température est égale à la température suivante
            else:
                historyTemperatureText += ' ↔️ '

    # Retourner l'historique de la température
    return historyTemperatureText

def parseHistoryExpense(historyExpense):
    """
    Retourne l'historique des dépenses sous forme de graphique avec des flèches

    Entrée: historyExpense (list)
    Sortie: historyExpenseText (string)
    """
    # Définir les variables
    historyExpenseText = ''
    
    # Parcourir la liste historyExpense
    for i in range(len(historyExpense)):
        expense = historyExpense[i]
        historyExpenseText += str(expense) + '€'
        
        # Vérifier s'il y a une dépense suivante dans la liste
        if i < len(historyExpense) - 1:
            next_expense = historyExpense[i + 1]
            
            # Ajouter ↗️ si la dépense est inférieure à la dépense suivante
            if expense < next_expense:
                historyExpenseText += ' ↗️ '
            # Ajouter ↘️ si la dépense est supérieure à la dépense suivante
            elif expense > next_expense:
                historyExpenseText += ' ↘️ '
            # Ajouter ↔️ si la dépense est égale à la dépense suivante
            else:
                historyExpenseText += ' ↔️ '

    # Retourner l'historique des dépenses
    return historyExpenseText


# > Nettoyer la console
clearConsole()

# > Définir les conditions de départ
conditions = {
    "maxRainyDays": input('Nombre de jours de pluie consécutifs maximum : '),
    "budget": input('Budget maximum : ')
}

# > Vérifier que les conditions de départ sont correctes
if conditions['maxRainyDays'].isdigit() == False:
    # Si le nombre de jours de pluie maximum n'est pas un nombre, définir la valeur par défaut à 3
    conditions['maxRainyDays'] = 3
else:
    # Si le nombre de jours de pluie maximum est un nombre, le convertir en entier
    conditions['maxRainyDays'] = int(conditions['maxRainyDays'])

if conditions['budget'].isdigit() == False:
    # Si le budget maximum n'est pas un nombre, définir la valeur par défaut à 2000
    conditions['budget'] = 2000
else:
    # Si le budget maximum est un nombre, le convertir en entier
    conditions['budget'] = int(conditions['budget'])

if conditions['maxRainyDays'] < 0:
    # Si le nombre de jours de pluie maximum est inférieur à 0, afficher un message d'erreur et arrêter le programme
    print('\033[31m' + 'Le nombre de jours de pluie maximum doit être supérieur à 0 !')
    exit()

if conditions['budget'] < 500:
    # Si le budget maximum est inférieur à 500, afficher un message d'erreur et arrêter le programme
    print('\033[31m' + '\nLe budget maximum doit être supérieur à 500€ !')
    exit()

# > Définir les variables
rainyDays = 0
totalRainyDays = 0
totalSunnyDays = 0
Days = 0
departureDate = datetime(2023, 10, 1)
returnDate = departureDate

historyTemperature = []
historyWeather = []
historyDays = []
historyExpense = []

# > Afficher les conditions de départ
# Nettoyer la console
clearConsole()
# Afficher les conditions de départ
print(f'Conditions de départ :')
print('---------------------')
print(f'Nombre de jours de pluie consécutifs maximum : {conditions["maxRainyDays"]}')
print(f'Budget maximum à dépenser : {conditions["budget"]}€')
print(f'Date de départ : {departureDate.strftime("%d/%m/%Y")}')
print('---------------------')

# > Attendre que l'utilisateur appuie sur la touche Entrée pour continuer
input('\nAppuyez sur Entrée pour continuer...')
print('\n---------------------')

# > Boucle principale
while rainyDays < conditions['maxRainyDays']:
    # Définir les variables
    weather = randomWeather()
    temperature = randomTemperature(weather)
    expense = randomExpense()
    Reason = ''

    # Mettre à jour les variables globales
    conditions['budget'] -= expense
    Days += 1

    # Ajouter les valeurs dans les listes d'historique
    historyTemperature.append(temperature)
    historyWeather.append(weather)
    historyDays.append(Days)
    historyExpense.append(expense)

    # Afficher la date du jour
    print(f'\nDate du jour : {returnDate.strftime("%d/%m/%Y")}')

    # Vérifier si le budget est dépassé
    if expense > conditions['budget']:
        # Si le budget est dépassé enregistrer la raison dans la variable Reason et arrêter la boucle
        Reason = 'ils n\'ont plus assez d\'argent pour continuer leurs vacances.'
        break
    else:
        # Si le budget n'est pas dépassé, afficher l'argent dépensé et l'argent restant
        print(f'Les retraités ont dépensé {expense}€ et il leur reste {conditions["budget"]}€')

    # Vérifier la météo du jour
    if weather == 'rainy':
        # Si il pleut, afficher un message et ajouter 1 à rainyDays
        rainyDays += 1
        totalRainyDays += 1
        print(f'Il a plu et il faisait {temperature}°C')
    else:
        # Si il ne pleut pas, afficher un message et ajouter 1 à sunnyDays
        rainyDays = 0
        totalSunnyDays += 1
        print(f'Il a fait beau et il faisait {temperature}°C')

    # Ajouter 1 jour à la date de retour
    returnDate += timedelta(days=1)

# > Si le nombre de jours de pluie maximum est dépassé, enregistrer la raison dans la variable Reason
if rainyDays >= conditions['maxRainyDays']:
    Reason = 'il a plu trop de jours de suite.'

# > Afficher la conclusion
print('\n---------------------')
print(f"\nLes deux retraités sont restés {Days} jours dans le sud de la France, du {departureDate.strftime('%d/%m/%Y')} au {returnDate.strftime('%d/%m/%Y')}.")
print(f"Ils ont été obligés de rentrer car {Reason}")

# > Afficher les historiques
print('\n---------------------')
print(f'\nHistorique de la météo : {parseHistoryWeather(historyWeather)}')
print(f'\nHistorique de la température : {parseHistoryTemperature(historyTemperature)}')
print(f'\nHistorique des dépenses : {parseHistoryExpense(historyExpense)}')

# > Afficher les statistiques
print('\n---------------------')
print(f'\nNombre de jours : {Days}')
print(f'Nombre de jours de pluie : {totalRainyDays}')
print(f'Nombre de jours de soleil : {totalSunnyDays}')
print('\n')
print(f'Température minimale : {min(historyTemperature)}°C')
print(f'Température maximale : {max(historyTemperature)}°C')
print(f'Température moyenne : {round(sum(historyTemperature)/len(historyTemperature), 2)}°C')
print('\n')
print(f"Jour le plus chaud : {(timedelta(days=historyDays[historyTemperature.index(max(historyTemperature))]) + departureDate).strftime('%d/%m/%Y')}")
print(f"Jour le plus froid : {(timedelta(days=historyDays[historyTemperature.index(min(historyTemperature))]) + departureDate).strftime('%d/%m/%Y')}")
print('\n')
print(f'Dépense minimale : {min(historyExpense)}€')
print(f'Dépense maximale : {max(historyExpense)}€')
print(f'Dépense moyenne : {round(sum(historyExpense)/len(historyExpense), 2)}€')