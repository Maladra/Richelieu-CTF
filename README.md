# Write-Up Richelieu CTF

1) Consulter le code source du site https://www.challengecybersec.fr/ on y trouve


```javascript
if (login === password) {
    document.location="./Richelieu.pdf";
```


2) Télécharger le PDF a l'adresse https://www.challengecybersec.fr/Richelieu.pdf


3) Realiser un petit script en Python en utilisant la librairie "pdftotext" pour extraire les données brutes du PDF.


```python
import pdftotext

with open("ctf.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print("\n\n".join(pdf))

print(len(pdf))

myvar = "".join(pdf)
fo = open("myfile", "w")
fo.write(myvar.encode('utf-8'))
fo.close()
```

4 ) A partir du fichier obtenu précedemment supprimer les premieres lignes, pour conserver uniquement le reste qui est codé en Base64, a partir de la nous obtenons une image 

![Image obtenue](https://github.com/Maladra/Richelieu-CTF/blob/master/images/clear_file&s=150)


5) En faisant un `strings` sur l'image l'on trouve quelques informations intéressantes : 

```
.bash_historyUT  
Le mot de passePK  
suite.zipUT  
de cette archivePK  
prime.txtUT  
est : DGSE{t.D=@Bx^A%n9FQB~_VL7Zn8z=:K^4ikE=j0EGHqI}PK  
public.keyUT  
motDePasseGPG.txt.encUT  
lsb_RGB.png.encUT
```


6) Utiliser le tool Binwalk pour extraire les données de l'image `binwalk -e clear_file`, nous obtenons un dossier `_clear_file.extracted` contenent 6 fichiers: 
- 6CCBC.zip : fichier ZIP a décompresser a l'aide du mot de passe `DGSE{t.D=@Bx^A%n9FQB~_VL7Zn8z=:K^4ikE=j0EGHqI}`
- lsb_RGB.png.enc : fichier empty
- motDePasseGPG.txt.enc : fichier empty
- prime.txt : fichier empty
- public.key : fichier vide
- suite.zip : fichier ZIP


7)  Obtention de nouveaux fichiers interessants prime.txt, public.key, lsb_RGB.png.enc, motDePasseGPG.txt.enc
