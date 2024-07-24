''' Programme qui permet de ranger des fichiers d'un répertoire
dans leurs fichiers respectifs appropriés en fonction de leurs types '''

import os
import shutil


class DirCleaner:

    def cleaner(self):
        get_dir = os.getcwd()  # Avoir le chemin du "current directory"
        # création des dossiers
        pdfs = os.getcwd() + '\\Pdfs'
        textes = os.getcwd() + '\\textes'
        images = os.getcwd() + '\\images'
        videos = os.getcwd() + '\\vidéos'
        logiciels = os.getcwd() + '\\logiciels'
        archives = os.getcwd() + '\\archives'
        musiques = os.getcwd() + '\\musiques'
        pages_web = os.getcwd() + '\\pages_web'

        try:
            os.mkdir(pages_web)
        except:
            pass
        try:
            os.mkdir(pdfs)
        except:
            pass
        try:
            os.mkdir(textes)
        except:
            pass
        try:
            os.mkdir(images)
        except:
            pass
        try:
            os.mkdir(videos)
        except:
            pass
        try:
            os.mkdir(logiciels)
        except:
            pass
        try:
            os.mkdir(archives)
        except:
            pass
        try:
            os.mkdir(musiques)
        except:
            pass

        exPdf = ["pdf", "PDF", "djvu", "epub"]
        exImage = ["jpeg", "jpg", "png", "psd", "webp"]
        exVideo = ["mp4", "avi", "mov", "flv", "FLV", "mkv", "wmv", "ts"]
        exTexte = ["txt", "odt", "docx", "doc"]
        exLogiciel = ["msi", "exe", "bat"]
        exArchive = ["zip", "rar", "iso", "gz"]
        exMusique = ["flac", "wav", "mp3", "ogg", "m4a"]
        exPageWeb = ["html", "mhtml", "htm"]

        # Ici nous allons parcourir les fichiers qui sont dans le dossier et les sous-dossiers du répértoire actuel
        for chemin, sous_rep, fichiers in os.walk(get_dir):
            for fichier in fichiers:
                new_path = os.path.join(chemin, fichier)
                # Selon l'extention du fichier, nous allons le placer dans le dossier approprié
                for s in exPdf:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, pdfs)
                        except:
                            pass
                for s in exTexte:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, textes)
                        except:
                            pass
                for s in exImage:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, images)
                        except:
                            pass
                for s in exVideo:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, videos)
                        except:
                            pass
                for s in exLogiciel:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, logiciels)
                        except:
                            pass
                for s in exArchive:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, archives)
                        except:
                            pass
                for s in exMusique:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, musiques)
                        except:
                            pass
                for s in exPageWeb:
                    if new_path.endswith(s):
                        try:
                            shutil.move(new_path, pages_web)
                        except:
                            pass


if __name__ == "__main__":
    DirCleaner().cleaner()
