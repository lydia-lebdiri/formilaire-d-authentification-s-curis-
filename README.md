# Presentation du programme:

Pour le lancement du programme il suffit juste de cliquer sur l’executer de l’IDE et le point d'entrée est la fonction ```main()``` dans le code.
la fonction main instancié un objet de la classe ApplicationAuthentification pour appeler ses fonctions
elle crée la fenetre principal auquels elle rajoute
- 1 logo qui est une image en appellant la fonction charger_logo(ecran)
- 2 labels (identifiant, mot de passe)
- 3 boutons (Reset, Ajout compte, OK) qui sont decrits en detail ci-dessous.

![plot](..\main\capture\capture.png)

J'ai également utilisé les modules suivants:
- tkinter: Tkinter propose tous les éléments cités suivnants (fenêtre graphique, widgets, gestionnaire d'événements)
- PILLOW: pour l'importation des image (ici c’est le logo d'authentification)
- pathlib:Pour la création de chemin de répertoire ou en stock les logins et plus précisément en utilisant la fonction mkdir(création du répertoire utilisateur)
- os : le module os permet d’effectuer des opérations courantes liées au système d’exploitation. Il est indépendant par rapport au système d’exploitation de la machine.

## Explication du déroulement du programme :
J'ai utilisé une classe ApplicationAuthentification qui contient toutes les fonctions de mon application.

Bouton Reset:il permet de supprimer les champs d'authentification avec la fonction ```reset_input()```

Bouton Ajout compte:C'est pour ajouter un utilisateur qui appelle la fonction ```enregister()``` et cette fonction crée une nouvelle fenetre avec un bouton enregistrer qui appelle la fonction ```enregistrer_utilisateur():```
- si l'utilisateur laisse les champs vides un messagebox va apparaître pour nous dire que les champs sont vides avec la fonction ``` enregistrer_utilisateur_champs_vide()``` et en clique sur le bouton OK pour fermer l'écran du message afficher avec la fonction  ```supprimer_utilisateur_champs_vides()```

![plot](../main/capture/enregistrer_utilisateur.png)

- si l'utilisateur existe déjà il affiche un autre popup pour nous informer qu'il est déjà existant avec la fonction ```utilisateur_existe-déjà``` et pour supprimer cette fenêtre on a juste a cliquer sur le bouton ok qui est manipuler par la fonction ```supprimer_utilisateur_existe_deja```


![plot](../main/capture/utilisateur_existe_déja.png)

- sinon le programme vas enregistrer et stocker le nouveau login dans le folder utilisateur  et en même temps vas nous afficher un message que l'enregistement a reussi


![plot](../main/capture/enregisitrer_avec_succès.png) 


- si l'utilisateur laisse les champs vide un messagebox vas apparaître pour nous dire que les champs sont vide avec la fonction 
``` enregistrer_utilisateur_champs_vide()```

![plot](../main/capture/champs_vide_enregistrement.png)

Et en clique sur le bouton OK pour fermer l'ecran du message afficher avec la fonction ``` supprimer_utilisateur_champs_vides() ```

Bouton OK: permet de verifier si un utilisateur peut se connecter et appelle la fonction ```verfier_login()```,
- si l'identifiant ou le modt de passe sont vides la fonction ```enregistrer_utilisateur_champs_vide()``` est appelée et qui affiche un popup.

 ![plot](../main/capture/champ_vide_OK.png) 
 
- si l'identifiant est correct et le mot de passe aussi alors la fonction ```authentification_réussi()``` va s’exécuter est un popup vas afficher un message d'authentification réussi et pour la fermer on clique sur le bouton ok qui appelle la fonction ```supprimer_login_reussi()```

![plot](../main/capture/authentification_reussi.png)

- si l'identifiant n'exste pas alors la fonction ```utilisateur_non_trouve()``` sera appelée et un message popup sera affichée que l'utilisateur n'existe pas et qui peut être fermee en cliquant sur le bouton ok qui appelle la fonction ```supprimer_utilisateur_non_trouve()```

 ![plot](../main/capture/utilisateur_existe_pas.png) 
 
- si l'identifiant exite  et le mot de passe est incorrect alors la focntion ```mdp_non_reconnu()``` sera appelée qui affiche un écran pour dire que le mdp est incorrect et qui pareil peut être fermé avec le bouton OK qui appelle la fonction ```supprimer_mdp_non_reconnu()```.


 ![plot](../main/capture/mdp_incorrect_ok.png) 


NB: tous les boutons ok des popups sont détruits avec le .destroy
`  




