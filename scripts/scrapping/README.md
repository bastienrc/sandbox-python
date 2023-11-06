# Scrapping

Le web scraping consiste à extraire des données de site web de façon automatisé.

## Bibliothèques

### Requests

Elle permet d’exécuter des requêtes HTTP et permet de récupérer via une requête HTTP GET les données contenues dans une page web.

```sh
pip install requests
```

### Beautiful Soup

Facilite l’extraction d’informations sur des pages web. Elle fonctionne avec n’importe quel analyseur HTML ou XML et vous fournit tout ce dont vous avez besoin pour vos instructions d’itération, de recherche et de modification sur l’arborescence d’analyse. Notez que vous pouvez utiliser Beautiful Soup avec html.parser, interpréteur fourni avec la bibliothèque standard de Python, qui vous permet d’analyser des fichiers texte HTML. En particulier, Beautiful Soup peut vous aider à parcourir le DOM et à en extraire les données dont vous avez besoin.

```sh
pip install beautifulsoup4
```

### Selenium

Selenium est une infrastructure de test automatisée, avancée et open source qui vous permet d’exécuter des opérations sur une page web dans un navigateur. En d’autres termes, vous pouvez utiliser Selenium pour demander à un navigateur d’effectuer certaines tâches. Notez que vous pouvez également utiliser Selenium comme bibliothèque de web scraping afin de mettre à profit ses capacités de navigateur sans tête. Si vous n’êtes pas familier avec ce concept, un navigateur sans tête est un navigateur web qui s’exécute sans GUI (Interface utilisateur graphique). S’il est configuré en mode sans tête, Selenium exécutera le navigateur contrôlé en arrière-plan.

Les pages web visitées dans Selenium sont rendues dans un véritable navigateur. En conséquence, Selenium permet de faire du web scraping sur des pages qui utilisent JavaScript pour la récupération ou le rendu des données.

```sh
pip install selenium
```

## Webographie

- [OpenClassrooms - Apprenez les bases du langage Python > Extrayez et transformez des données avec l’extraction web](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-lextraction-web)
- TODO: [Le web scraping avec Python : un guide pas-à-pas](https://brightdata.fr/blog/savoir-faire/web-scraping-with-python)
- TODO: https://www.freecodecamp.org/news/use-scrapy-for-web-scraping-in-python

