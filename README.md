# Pylogger

Le logiciel 
Programmation simple et discrète d'un keylogger en python implémentant un démarrage automatique.
La trace écrite des touches saisies au clavier est stockée dans un fichier texte en local dans le dossier du keylogger, et le logiciel envoie un mail comportant ce fichier à une fréquence en secondes facilement paramétrable.

Installation de python
Système d’exploitation: windows10.
Télécharger une version récente de python de préférence.. La version Python 3.7 ainsi que la version Python 2 permettent d'exécuter notre programme python sur nos ordinateurs.
L'utilisateur a le choix d'installer python sur le site internet officiel de python : https://www.python.org/downloads/
Ou bien, il peut simplement installer la version 3.7.1 que l'on fournit directement dans le dossier Keylogger en double-cliquant sur "install_python37".

Installation des deux librairies utilisées dans notre logiciel 
A la main, l’utilisateur peut entrer ces deux commandes :
$ py -m pip install pynput ou $ python -m pip install pynput
$ py -m pip install pywin32 ou $ python -m pip install pywin32
Ou alors, il peut simplement double-cliquer sur le fichier batch “installation-librairies”, qui fera les installations automatiquement.

Exécution
Pour que le Keylogger démarre automatiquement, on doit d'abord exécuter une première fois le Keylogger en double-cliquant sur le fichier batch “exécution”, ou en exécutant indépendamment les fichiers pythons send_mail.py et logger.py de la manière suivante :
$ py logger.py
$ py send_mail.py

TODO liste des bugs et évolutions souhaitées
Ajouter les captures d’écran à l’enregistrement des frappes de touches  du clavier et pouvoir les envoyer par mail.
Intégrer d’autres systèmes d’exploitation.
Utiliser le keylogger dans des serveurs distants.
 






