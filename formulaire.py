import base64
from tkinter import *
import os
from PIL import Image, ImageTk
from pathlib import Path


# Fenetre d'enregistrement
class ApplicationAuthentification():

    def enregister(self):
        global ecran_enregistrer
        global identifiant
        global mot_de_passe
        global identifiant_input
        global mot_de_passe_input
        ecran_enregistrer = Toplevel(ecran_principal)
        ecran_enregistrer.title("Ajout Compte")
        ecran_enregistrer.geometry("300x250")

        identifiant = StringVar()
        mot_de_passe = StringVar()
        Label(ecran_enregistrer, text="Entrer les informations suivantes", bg="yellow").pack()
        Label(ecran_enregistrer, text="").pack()
        identifiant_label = Label(ecran_enregistrer, text="Identifiant * ")
        identifiant_label.pack()
        identifiant_input = Entry(ecran_enregistrer, textvariable=identifiant)
        identifiant_input.pack()
        mot_de_passe_label = Label(ecran_enregistrer, text="Mot de passe * ")
        mot_de_passe_label.pack()
        mot_de_passe_input = Entry(ecran_enregistrer, textvariable=mot_de_passe, show='*')
        mot_de_passe_input.pack()
        Label(ecran_enregistrer, text="").pack()
        Button(ecran_enregistrer, text="Enregistrer", width=10, height=1, bg="yellow",
               command=self.enregistrer_utilisateur).pack()

    # implementer des evenements sur le boutton enregistrer
    def enregistrer_utilisateur(self):
        identifiant_info = identifiant.get()
        mot_de_passe_info = mot_de_passe.get()
        if not identifiant_info or not mot_de_passe_info:
            self.enregistrer_utilisateur_champs_vide()
        else:
            # ici pareil on cree le folder utilisateurs s'il n'exsite pas
            Path("utilisateurs").mkdir(parents=True, exist_ok=True)
            list_fichiers = os.listdir("utilisateurs/")
            identifiant_info = base64.b64encode(identifiant_info.encode("utf-8"))
            if identifiant_info in list_fichiers:
                # afficheer une fenetre qui dit que l'uitlisateur existe deja
                self.utilisateur_existe_deja()
            else:
                # on ecrit les fichiers de logins dans le folder utilisateurs
                fichier = open("utilisateurs/" + identifiant_info.decode(), "w")
                mot_de_passe_info = base64.b64encode(mot_de_passe_info.encode("utf-8"))
                fichier.write(identifiant_info.decode() + "\n")
                fichier.write(mot_de_passe_info.decode())
                fichier.close()

                identifiant_input.delete(0, END)
                mot_de_passe_input.delete(0, END)

                Label(ecran_enregistrer, text="Registration Success", fg="green", font=("calibri", 11)).pack()


    # implementer des evenements sur le boutton login

    def verfier_login(self):
        identifiant_1 = verifier_identifiant.get()
        mot_de_passe_1 = verifier_mot_de_passe.get()
        if not identifiant_1 or not mot_de_passe_1:
            self.enregistrer_utilisateur_champs_vide()
        else:
            identifiant_login_input.delete(0, END)
            mot_de_passe_login_input.delete(0, END)
            # ici pareil on cree le folder utilisateurs s'il n'exsite pas
            Path("utilisateurs").mkdir(parents=True, exist_ok=True)
            list_fichiers = os.listdir("utilisateurs/")
            identifiant_1 = base64.b64encode(identifiant_1.encode("utf-8"))
            mot_de_passe_1 = base64.b64encode(mot_de_passe_1.encode("utf-8"))
            if identifiant_1.decode() in list_fichiers:
                fichier = open("utilisateurs/" + identifiant_1.decode(), "r")
                verify = fichier.read().splitlines()
                if mot_de_passe_1.decode() in verify:
                    self.authentification_reussie()

                else:
                    self.mdp_non_reconnu()

            else:
                self.utilisateur_non_trouve()

    def charger_logo(self, ecran):
        path = "logo/1.png"
        image = Image.open(path)
        image_tk = ImageTk.PhotoImage(image.resize((50, 50), Image.ANTIALIAS))
        panel = Label(ecran, image=image_tk)
        panel.image = image_tk
        panel.pack(side=TOP, anchor=NW)

    #  popup for login reussi

    def authentification_reussie(self):
        global ecran_login_reussie
        ecran_login_reussie = Tk()
        ecran_login_reussie.title("Success")
        ecran_login_reussie.geometry("150x100")
        Label(ecran_login_reussie, text="Authentification Reussie").pack()
        Button(ecran_login_reussie, text="OK", command=self.supprimer_login_reussi).pack()

    def utilisateur_existe_deja(self):
        global ecran_utilisateur_existe_deja
        ecran_utilisateur_existe_deja = Tk()
        ecran_utilisateur_existe_deja.title("Utilisateur existe deja !!")
        ecran_utilisateur_existe_deja.geometry("150x100")
        Label(ecran_utilisateur_existe_deja, text="Utilisateur existe deja !!").pack()
        Button(ecran_utilisateur_existe_deja, text="OK", command=self.supprimer_utilisateur_existe_deja).pack()

    #  popup pour mot de passe non reconnu

    def mdp_non_reconnu(self):
        global ecran_mdp_non_reconnu
        ecran_mdp_non_reconnu = Tk()
        ecran_mdp_non_reconnu.title("Success")
        ecran_mdp_non_reconnu.geometry("150x100")
        Label(ecran_mdp_non_reconnu, text="Mot de passe incorrect ").pack()
        Button(ecran_mdp_non_reconnu, text="OK", command=self.supprimer_mdp_non_reconnu).pack()

    #  popup pour utilisateur non trouve

    def utilisateur_non_trouve(self):
        global ecran_utilisateur_non_trouve
        ecran_utilisateur_non_trouve = Tk()
        ecran_utilisateur_non_trouve.title("Success")
        ecran_utilisateur_non_trouve.geometry("150x100")
        Label(ecran_utilisateur_non_trouve, text="L'Utilisateur n'existe pas !!").pack()
        Button(ecran_utilisateur_non_trouve, text="OK", command=self.supprimer_utilisateur_non_trouve).pack()

    def enregistrer_utilisateur_champs_vide(self):
        global ecran_enregistrer_utilisateur_vide
        ecran_enregistrer_utilisateur_vide = Tk()
        ecran_enregistrer_utilisateur_vide.title("Champs vides !!")
        ecran_enregistrer_utilisateur_vide.geometry("400x100")
        Label(ecran_enregistrer_utilisateur_vide,
              text="L identifiant et le mot de passe sont vides, \n merci de les renseigner").pack()

        Button(ecran_enregistrer_utilisateur_vide, text="OK", command=self.supprimer_utilisateur_champs_vides).pack()

    # supprimer les popup
    def supprimer_login_reussi(self):
        ecran_login_reussie.destroy()

    def supprimer_mdp_non_reconnu(self):
        ecran_mdp_non_reconnu.destroy()

    def supprimer_utilisateur_non_trouve(self):
        ecran_utilisateur_non_trouve.destroy()

    def supprimer_utilisateur_champs_vides(self):
        ecran_enregistrer_utilisateur_vide.destroy()

    def supprimer_utilisateur_existe_deja(self):
        ecran_utilisateur_existe_deja.destroy()

    def reset_input(self):
        identifiant_login_input.delete(0, END)
        mot_de_passe_login_input.delete(0, END)


# Fonction main (point d entree du code)
def main():
    global ecran_principal
    ecran_principal = Tk()
    auth_application = ApplicationAuthentification()
    auth_application.charger_logo(ecran_principal)
    ecran_principal.geometry("400x400")
    ecran_principal.title("Compte Login")
    Label(ecran_principal, text="Entrer vos infomrations d'authentification").pack()
    Label(ecran_principal, text="").pack()

    global verifier_identifiant
    global verifier_mot_de_passe

    verifier_identifiant = StringVar()
    verifier_mot_de_passe = StringVar()

    global identifiant_login_input
    global mot_de_passe_login_input

    Label(ecran_principal, text="Identifiant * ").pack(padx=15, pady=5)
    identifiant_login_input = Entry(ecran_principal, textvariable=verifier_identifiant)
    identifiant_login_input.pack()
    Label(ecran_principal, text="").pack()
    Label(ecran_principal, text="Mot de passe * ").pack(padx=15, pady=5)
    mot_de_passe_login_input = Entry(ecran_principal, textvariable=verifier_mot_de_passe, show='*')
    mot_de_passe_login_input.pack()
    Label(ecran_principal, text="").pack()

    Button(ecran_principal, text="Reset", height="2", width="15", command=auth_application.reset_input).pack(side=LEFT,
                                                                                                             padx=5)
    Button(ecran_principal, text="OK", height="2", width="15", command=auth_application.verfier_login).pack(side=LEFT,
                                                                                                            padx=5)

    Button(text="Ajout Compte", height="2", width="15", command=auth_application.enregister).pack(side=RIGHT, padx=5)

    ecran_principal.mainloop()


if __name__ == "__main__":
    main()
