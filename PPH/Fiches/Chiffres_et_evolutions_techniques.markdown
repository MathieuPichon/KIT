# Fiche n°1 : Chiffres et Evolution technique/technologique des jeux vidéo



<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=2 orderedList=false} -->
<!-- code_chunk_output -->

* [Chiffres "classiques": € de chiffres d'affaire, nbre de joueurs, etc en France](#chiffres-classiques-de-chiffres-daffaire-nbre-de-joueurs-etc-en-france)
* [Infographie de l'évolution des support du jeu vidéo](#infographie-de-lévolution-des-support-du-jeu-vidéo)
* [Références :](#références)

<!-- /code_chunk_output -->


## Chiffres "classiques": € de chiffres d'affaire, nbre de joueurs, etc en France

Chiffre d'affaire de l'industrie en France pour l'année **2017**, chiffres venant du Syndicat des Editeurs de Logiciels de Loisirs (SELL) en partenariat avec 3 organismes collectant les données (GSD, GameTrack et AppAnnie) [cf [1] & [2]] :

### Chiffre d'affaire total = 4.3 M€ :
1. Tout support confondus :
	1. Ventes Hardware (Consoles, ordinateurs et accessoires) = 1.69 G€
	2. Vente Software (Jeux) = 2.61 G€
2. Par écosysteme/support :
	1. Consoles = 2.401 G€
	2. PC = 1.12 G€
	3. Mobile = 778 M€


### Profil des joueurs français :

* **62% des français considèrent le jeu vidéo comme une activité positive**
* **80% des français considèrent ques les jeux vidéo son créés par des artistes**
* **77% des français considèrent le jeu vidéo comme un loisir pour toute la famille**
* **Moyenne d'âge du joueur français : 34 ans**


Pourcentage de joueurs (jouant au minimum 2 fois par mois) par tranche d'âge :

```vega-lite
{
  "data": {
    "values": [
    {"a": "10-14 ans","b":95}, {"a": "15-18 ans","b":92},{"a": "19-24 ans","b":91},
    {"a": "25-34 ans","b":73}, {"a": "35-44 ans","b":70},
    {"a": "45-54 ans","b":51}, {"a": "55 ans et +","b":46}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type":"nominal", "axis":{"title":"Categories d'age"}},
    "y": {"field": "b", "type":"quantitative", "axis":{"title":"Pourcentage de joueurs par categorie d'age"}}
  }
}
```




### Evolutions remarquables :

**Chiffre intéressant n°1**, la vente des jeux dématérialisés représente désormais 41% des ventes sur consoles (+46% par rapport à 2016) et 95% (!) des ventes sur PC (stables par rapport à 2016).
--> La dématérialisation est déjà rentrée dans les moeurs de consomation des français. Ceci est en grande partie dû à l'essor des plates-formes d'achat Steam, Electronic Arts, ...

**Chiffre intéressant n°2**,


**Autre observation**, les consoles de salon représentent toujours le plus gros morceau de l'industrie, comme le souligne l'étude c'est probablement due à sa capacité à y jouer en famille.


_2 Faiblesses notables de l'étude. 1) la non prise en compte du nombre de souscriptions aux jeux par abonnements ou services par abonnements (World of Warcraft, PS4 Pro) ni le volume des micro transactions réalisées dans les jeux à part pour l'écosystème mobile où cela semble avoir été pris en compte. Or les microtransactions sont pour certains éditeurs au coeur du modèle économique. 2) Les données des ventes dématérialisées sont incomplètes dues aux réticences de certains des éditeurs majeurs du secteur de dévoiler leurs chiffres d'affaires complets (cf l'introduction de cette article du site web Gamekult [[3]]). Il est donc impossible de réaliser un top des ventes prenant en compte le secteur dématérialisés_

_____________________________

## Infographie de l'évolution des support du jeu vidéo

Dates à graphiquer :
* ???? : Avènement des jeux de rôle sur plateau ou avec un "Game Master" en tout cas
* ???? : invention du premier jeux vidéo
* 1972 : sortie de Pong par Atari
* 1977 : sortie de l'Atari 2600, première console de salon
	- 1978 : Space Invaders
	- 1983 : entrée du Japon dans l'arène avec la Famicon (NES dans le reste du monde)
	- 1985 : sortie de Super Mario Bros. sur NES
* 1989 : sortie de la Gameboy (console portable)
* ...
* 1997 : sortie de Ultima Online, cité comme le premier gros MMORPG ~~fonctionnant sur ARPANET~~
* 2004 : sortie de World of Warcraft, énorme popularité du MMORPG (mais pas le premier, qui doit être Ultima ou Dark Age of Camelot)
* 2004 : sortie de la Nintendo DS, première console portable véritablement tactile (ayant eu du succès)
* 2006 : sortie de la Wii, première grosse console à intégrer des élément de motion capture (la playstation avait déjà un module mais l'usage était bien plus limité à quelque jeux)
* ???? : Sortie de la VR
* 2003 : création de la plateform Steam, combinant vente en ligne, aspect social avec profil utilisateur et amis, gestion du multi-joueur, gestion des sauvegarde en ligne

_____________________________


## Références :
(1):https://www.afjv.com/news/8590_le-jeu-video-en-france-un-marche-de-4-3-milliards-d-euros.htm
(2):https://drive.google.com/file/d/1iWSkg41ZhGUQFiunD2DAnKHnuLU8AwqB/view
(3):https://www.gamekult.com/actualite/les-chiffres-du-jeu-video-en-france-pour-l-annee-2017-sont-disponibles-3050802893.html

[1]:https://www.afjv.com/news/8590_le-jeu-video-en-france-un-marche-de-4-3-milliards-d-euros.htm
[2]:https://drive.google.com/file/d/1iWSkg41ZhGUQFiunD2DAnKHnuLU8AwqB/view
[3]:https://www.gamekult.com/actualite/les-chiffres-du-jeu-video-en-france-pour-l-annee-2017-sont-disponibles-3050802893.html
