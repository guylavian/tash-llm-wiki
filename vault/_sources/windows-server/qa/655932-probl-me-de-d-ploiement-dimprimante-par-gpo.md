---
title: "Problème de déploiement d'imprimante par GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/655932/probl-me-de-d-ploiement-dimprimante-par-gpo
question_id: 655932
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
---
# Problème de déploiement d'imprimante par GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/655932/probl-me-de-d-ploiement-dimprimante-par-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Bonjour,  

J'ai des soucis de déploiement d'imprimante par GPO. J'ai un serveur d'impression sous Windows server 2019 et idem pour le DC.  

Je déploie les imprimantes par GPO. Avant les soucis du mois d'octobre  et des mises à jour, tout fonctionnait bien.  

J'ai mis les postes à jour et j'ai toujours un souci avec les imprimantes déployées par GPO. Les imprimantes sont déployées pour l'administrateur mais pas pour les autres utilisateurs. Les postes sous Windows 10 ont la version 21H1 ou 21H2  

Les GPO sont des GPO par ordinateur, stratégies, Paramètres Windows et Connexions aux imprimantes (lorsque l'on fait un clic droit sur une imprimante partagée et déployer avec la stratégie de groupe). La GPO par ordinateur, Préférences, Paramètres du Panneau de configuration donne le même résultat.  

Les utilisateurs peuvent installer les imprimantes en ajoutant une imprimante qui se trouve dans l'annuaire.  

Merci pour votre précieuse aide.  

Bonne journée  

Wilfried

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-10*

Bonjour  

Merci pour votre question et votre réponse.  

Si les utilisateurs ne sont pas en mesure d'installer ou d'imprimer, cela peut être dû au correctif Print night mare appliqué sur vos serveurs.  

Par défaut, les utilisateurs non administrateurs ne pourront plus effectuer les opérations suivantes à l'aide de Pointer et imprimer sans élévation de privilèges d'administrateur :  

Installer de nouvelles imprimantes à l'aide de pilotes sur un ordinateur ou un serveur distant  

Mettez à jour les pilotes d'imprimante existants à l'aide des pilotes d'un ordinateur ou d'un serveur distant.  

Veuillez consulter l'article Microsoft ci-dessous qui traite de la même chose.  

https://support.microsoft.com/fr-FR/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872  

--Si la réponse est utile, veuillez voter pour et accepter comme réponse--
