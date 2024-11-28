# scripts
Ce repo contient divers scripts que j'ai créé dans le but de me faciliter la vie.

## md_title_converter.py

Ce script convertit les titres Markdown en "Headings IDs" pour les sommaires (voir la [doc Markdown](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids)).

Il y a pleins de paramètres à prendre en compte (pas de majuscules, pas d'espace, etc) et avoir un script automatisant la conversion peut faire gagner pas mal de temps (en plus d'éviter de rendre fou).


Bien qu'il est possible d'utiliser du HTML, il est souvent plus simple de fonctionner avec les "Headings IDs".


Par exemple, le titre `## Super titre 2` devient `#super-titre-2`, ce qui donne, pour le sommaire, le lien suivant `[Super titre 2](#super-titre-2)`.

## evtx_viewer

Ce script permet de visualiser les événements des fichiers .evtx dans une interface graphique multiplateforme. C'est une sorte d'observateur d'événement en Python.
