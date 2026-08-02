---
title: "GPO configuration ordinateurs ne s'applique pas aux unité organisationnelle"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163866/gpo-configuration-ordinateurs-ne-sapplique-pas-aux
question_id: 1163866
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# GPO configuration ordinateurs ne s'applique pas aux unité organisationnelle

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163866/gpo-configuration-ordinateurs-ne-sapplique-pas-aux (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Bonjour, 

J'ai actuellement un problème avec des GPO configurations ordinateurs qui ne s'applique pas quand je les mets dans une unité organisationnelle. Si je met la GPO dans la racine du domaine elle s'applique mais quand elle est mise dans une OU non. Je tourne en boucle pourriez vous m'aider ?

La GPO en question est Install ReportBuilder.msi

Voici le rapport gpresult la gpo est bien prise en compte mais n'installle pas le logiciel en question (voir rapport GPO)

Le logiciel ne s'installe pas (voir GPO IN OU) 

Le Logiciel s'installe

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-10*

Hello,

I have the same issue, when deploying a MSI package by GPO on a OU, I perform a gpupdate /force  installation working after reboot.

but if I tried to just reboot computer without the gpupdatep /force the software not installed after reboot.

By the way, if a make the GPO on domaine racine, this installation working fine after  a simple reboot.

What's block installation from OU ?

Bonjour,

J'ai exactement le même problème quand je déploie un racket MSI par GPO . J'effectue un gpupdate /force l'installation fonctionne après le redémarrage.

Mais si j'essaye de juste redémarrer sans faire le gpupdate /force the logiciel n'est pas installé après le redémarrage.

Dans tous les cas, si je fait la GPO a la racine du domaine, l'installation fonctionne après un simple redémarrage.

Qu'est ce qui bloque l'installation depuis les OU ?

Merci d'avance pour votre aide.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

I have linked an article below that may help solve your issue. Here is what the article has to say:

According to Daisy Zhou, a Microsoft Employee, you can log in to one member server using the domain "Y" account and password if the GPO setting is user configuration.

-  Next, make a new folder called Folder on the C drive.

Opening CMD (do not run as Administrator).

-  Enter the command gpresult /h C:\Folder\wallpaper.html

4.Open wallpaper.html and look under "User Details" to see if there is a comparable GPO setting.

If you configured a GPO option under "User Details" but there isn't one there.

REFERENCE: https://learn.microsoft.com/en-us/answers/questions/311749/gpo-doesnt-apply-to-user-of-the-ou-that-is-linked

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-24*

Hi @Xavier GAILLARD  

My answer will be in english because we are in english forum :)

If I understood your issue , the GPO setting is applied  but the MSI is not installed. 

In this case it's not GPO issue because we can see settings the GPO settings applied in GPresult

This kind of behavior is known when you want to deploy MSI through GPO without adding another GPO setting to let the impacted machine wait network to be connected at computer startup to be able to access on the share of MSI file:

Always wait for the network at computer startup and logon

Please don't forget to mark helpful answer as accepted
