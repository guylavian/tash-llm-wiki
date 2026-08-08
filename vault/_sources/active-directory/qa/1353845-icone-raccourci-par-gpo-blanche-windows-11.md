---
title: "Icone raccourci par GPO blanche windows 11"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1353845/icone-raccourci-par-gpo-blanche-windows-11
question_id: 1353845
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Icone raccourci par GPO blanche windows 11

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1353845/icone-raccourci-par-gpo-blanche-windows-11 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Bonjour,

Dans notre infrastructure, nous avons des postes sous Windows 11 et Windows 10.

Nous avons un serveur 2016 qui héberge le DC et donc les GPO.

Nous avons différents raccourcis vers des pages web avec l'icône de l'application, l'icône est hébergée sur le sysvol. 

Depuis le passage à windows 11, une icône blanche apparait sur certain raccourci à la place des icônes personnalisées.

Les raccourcis redescendent bien et sont fonctionnels.

Détail de la GPO :

-  Nous utilisons la configuration utilisateur.

-  La configuration du raccourci est identique (seul le nom, l'icône et le lien sont différents)

-  Les icônes sont au format ".ico" dans le même dossier.

Je précise est remplacée par une feuille blanche UNIQUEMENT sur Windows 11, sous Windows 10 aucun problème, le raccourci fonctionne avec la bonne icône.

Je vous remercie par avance pour votre aide,

Cordialement

## Answer (community) — community member

*upvotes: 2 · updated: 2024-04-24*

Bonjour,

Dans l'institution où je travaille, nous étions aussi inquiet par rapport à ce problème mais il est solutionnable de cette manière (sans devoir copier localement les fichiers .ico) :

Ouvrez un GPEDIT.msc -> Configuration ordinateur -> Modèles d'administration -> Composants Windows -> Explorateur de fichiers Paramètre : Autoriser l'utilisation de chemins distants dans les icônes de raccourci de fichiers

Le texte de description implique la « sécurité » comme raison potentielle pour laquelle ce paramètre a changé entre 10 et 11.

Une fois le paramètre activé, les icônes s'affichent aussitôt (un refresh peut être nécessaire).

Bien à vous,  

Melvyn

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-15*

Hello LDEDSIY,

Thank you for posting in Q&A forum.  

Does the issue occur on all the Windows 11 clients? If so, you can try workaround below.  

1.You can put all the Icon files on Win 11 clients locally instead of shared path as ketro mentioned.  

1-1.Create folder on all clients via GPO.  

1-2.Copy Icon files to all clients via GPO  

2.You can also try workaround here:  

Reference  

https://www.prajwaldesai.com/create-desktop-shortcut-using-group-policy/  

3.Also, you can feedback your question via "Feedback Hub" by searching "Feedback Hub" at start menu .  

Hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
