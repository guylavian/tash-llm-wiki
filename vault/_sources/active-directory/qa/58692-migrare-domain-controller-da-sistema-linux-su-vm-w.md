---
title: "Migrare domain controller da sistema linux su vm windows server 2008"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58692/migrare-domain-controller-da-sistema-linux-su-vm-w
question_id: 58692
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrare domain controller da sistema linux su vm windows server 2008

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58692/migrare-domain-controller-da-sistema-linux-su-vm-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Buongiorno, ho un nas qnap come domain controller, vorrei sapere se è possibile migrare esso su una vm con windows server 2008 R2(livello schema uguale --> 47), facendo delle prove, dopo aver creato il domain controller sul nas ho aggiunto la vm al dominio e abilitato il ruolo di active directory, fino a qui tutto bene, il nas e la vm di DC riuscivano a comunicare tra di loro, e creando un utente dalla vm DC esso si è inoltre replicato sul nas, per prova ho spento il nas, e tutto è andato perso, non riesco più ad accedere all'utente che ho creato sul dc, ma soltanto all'utente che avevo creato sul nas e si ripristina tutte le volte che accedo, qualche idea per migliorare la mia situazione? grazie!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-05*

Hello AssistenzaNewsoft-6364,  

Thank you for posting in our Q&A forum.  

I am sorry, I do not understand Italian, so I will reply to you in English. Not sure if you can understand English. Thank you for your understanding and support.  

And I am sorry, we are not faimlar with nas qnap DC, however we are faimlar with Windows server DC, and I will try my best to help you.  

Based on the description, we have two DCs (nas qnap DC and 2008 R2 DC) in your domain, is that right?  

If so, not sure if all the data on nas qnap DC can be replicated to 2008 R2 DC automatically.   

We can check as below:  

1.Check if 2008 R2 DC is working fine by running Dcdiag /V on 2008 R2 DC.  

2.Check IF AD replication is working well by running repadmin /showrepl and repadmin /replsum on 2008 R2 DC.  

3.Check which DC is the FSMO roles holder by running netdom query fsmo on 2008 R2 DC (if we do not transfer FSMO roles to 2008 R2, the fsmo role holder should be nas qnap DC).  

4.Check if we can run gpupdate /force successfully on 2008 R2 DC.  

5.Check if SYSVOL folder and Netlogon folder are shared by running net share on 2008 R2 DC (the two folder should be shared).  

Check if there is any error after running the command above.  

Best Regards,  

Daisy Zhou
