# EduShare Education

Le logiciel EduShare, est un outil de travail numérique, permettant aux élèves comme aux professeurs de partager des fichiers entre eux. Il est sécurisé et permet de partager, de gros, comme de petits fichiers rapidement, sans utiliser de serveur entre les deux parties.

Ce logiciel est sous licence [MIT](https://github.com/likapi/edushare/blob/main/LICENSE) donc, toute personne, souhaitant réutiliser, le code source du logiciel y est autorisé, uniquement si elle n'oublie pas, de mentionner la fondation [Likapi](https://likapi.github.io/), en tant que propriétaire du code source. 

Notre équipe, avons programmés ce logiciel, dans l'objectif d'améliorer le partage de fichiers dans le domaine éducatif, tout en restant le plus simple possible, au niveau de l'utilisation du logiciel, de son interface ainsi que de son installation.

Nous remercions par avance, chaque personne contribuant au développement du projet qui vise à favoriser le développement, des outils numériques dans les établissements scolaires sans pour autant compliquer leurs utilisations par les étudiants.

## Installation

L'installation du logiciel a été simplifiée au maximum pour éviter aux élèves de se perdre dans l'installation. Elle se fait donc en un clic pour la version Windows et en une commande pour la version Linux.

### Windows :

### Linux :

```shell
~# wget https://github.com/likapi/edushare/releases/download/v1.0-beta-linux/v1.0-beta-linux-edushare.deb
~# sudo dpkg -i v1.0-beta-linux-edushare.deb
```

## Utilisation

```shell
~# sudo edushare
~# sudo edushare-gui
```

### Fonctionnalités :

- [x] Partage de fichiers (Socket)
- [x] Réception de fichiers (Socket)
- [x] Compression de fichiers (.zip)
- [x] Affichage des tunnels (Ngrok)
- [x] Modification de la région (Ngrok)
- [x] Ajout d'un AuthToken (Ngrok)
- [ ] Affichage de l'historique
- [ ] Guide d'utilisation du logiciel
- [x] Fermeture du client

### Fonctionnalités à venir :

- Envoi de message (Socket)
- Vérification du hash d'un fichier
- Interface graphique
- Installateur Windows

## Contribution

Les rapports de bogues et les demandes de pull requests sont les bienvenus sur GitHub à l'adresse https://github.com/likapi/edushare. Ce projet, se veut un espace de collaboration sûr et accueillant, et les contributeurs doivent adhérer au [code de conduite des contributeurs](https://www.contributor-covenant.org/).

### Modification de code :

1. Ouvrir une [Pull request](https://github.com/likapi/edushare/pulls)
2. Assurez-vous que tous les tests CI réussissent
3. Attendez la révision du code
4. Publiez la nouvelle version du code

### Conception et développement :

1. Le moins de dépendances possible
2. Aucun script de construction nécessaire
3. Expérience graphique facile et simple
4. Installation rapide en quelques clics

