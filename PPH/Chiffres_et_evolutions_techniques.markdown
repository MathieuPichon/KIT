# Fiche n°1 : Chiffres et Evolution technique/technologique des jeux vidéo



<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [Chiffres "classiques": € de chiffres d'affaire, nbre de joueurs, etc en France](#chiffres-classiques-de-chiffres-daffaire-nbre-de-joueurs-etc-en-france)
	* [Chiffre d'affaire total = 4.3 M€ :](#chiffre-daffaire-total-43-m)
	* [~~Ventes par genre~~ :](#~~ventes-par-genre~~)
	* [Profil des joueurs français :](#profil-des-joueurs-français)
	* [Evolutions remarquables :](#evolutions-remarquables)
* [Infrographie de l'évolution des support du jeu vidéo](#infrographie-de-lévolution-des-support-du-jeu-vidéo)
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


### ~~Ventes par genre~~ :
1. Console :
  1. Action
  2. Tir/FPS
  3. Jeux de rôle/RPG
  4. Sport
  5. Aventure
2. PC (uniquement vente physique qui représente 5% des ventes, donc difficilement représentatif):
  1. Stratégie
  2. Tir/FPS
  3. Action
  4. Rôle/RPG
  5. Jeux Casual (Plateau/Carte/Puzzles)

~~j'ai des doutes sur la pertinence de cette section~~

### Profil des joueurs français :

* **62% des français considèrent le jeu vidéo comme une activité positive**
* **80% des français considèrent ques les jeux vidéo son créés par des artistes**
* **77% des français considèrent le jeu vidéo comme un loisir pour toute la famille**
* **Moyenne d'âge du joueur de jeu vidéo : 34 ans**

Pourcentage de joueurs (jouant au minimum 2 fois par mois) par tranche d'âge :
1. 10-14 ans : 95%
2. 15-18 ans : 92%
3. 19-24 ans : 91%
4. 25-34 ans : 73%
5. 35-44 ans : 70%
6. 45-54 ans : 51%
7.  +55  ans : 46%

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
--> La dématérialisation est déjà rentrée dans les moeurs de consomation des français.
~~**Chiffre intéressant n°2**, le jeux le plus vendu sur PC en vente physique est Les Sims 4 et ses extensions. Jeux de gestion à l'utilisation très familliale, ce jeux est très loin d'avoir une composante compétitive ou multi-joueur ce qui tranche par rapport aux autres jeux figurant dans le top 20 des ventes.~~
--> Via ce chiffres et d'autres cités dans l'étude du SELL, on remarque

**Autre observation**, les consoles de salon représentent toujours le plus gros morceau de l'industrie, comme le souligne l'étude c'est probablement dûe à sa capacité à y jouer en famille, ce qui séduit probablement les parents en quête d'activité avec leurs enfants.


_2 Faiblesses notables de l'étude. 1) la non prise en compte du nombre de souscriptions aux jeux par abonnements ou services par abonnements (World of Warcraft, PS4 Pro) ni le volume des micro transactions réalisées dans les jeux à part pour l'écosysteme mobile où cela semble avoir été pris en compte. Or les microtransactions sont pour certains éditeurs au coeur du modèle économique. 2) Les données des ventes dématérialisées sont incomplètes dues aux réticences de certains des éditeurs majeurs du secteur de dévoiler leurs chiffres d'affaires complets (cf l'introduction de cette article gamekult [[3]]). Il est donc impossible de réaliser un top des ventes prenant en compte le secteur dématérialisés_

_____________________________

## Infrographie de l'évolution des support du jeu vidéo



_____________________________


## Références :
(1):https://www.afjv.com/news/8590_le-jeu-video-en-france-un-marche-de-4-3-milliards-d-euros.htm
(2):https://drive.google.com/file/d/1iWSkg41ZhGUQFiunD2DAnKHnuLU8AwqB/view
(3):https://www.gamekult.com/actualite/les-chiffres-du-jeu-video-en-france-pour-l-annee-2017-sont-disponibles-3050802893.html

[1]:https://www.afjv.com/news/8590_le-jeu-video-en-france-un-marche-de-4-3-milliards-d-euros.htm
[2]:https://drive.google.com/file/d/1iWSkg41ZhGUQFiunD2DAnKHnuLU8AwqB/view
[3]:https://www.gamekult.com/actualite/les-chiffres-du-jeu-video-en-france-pour-l-annee-2017-sont-disponibles-3050802893.html
