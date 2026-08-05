---
title: "Group Policies Replication in progress - Sysvol related error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1016367/group-policies-replication-in-progress-sysvol-rela
question_id: 1016367
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Group Policies Replication in progress - Sysvol related error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1016367/group-policies-replication-in-progress-sysvol-rela (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Some context first :    

We have a 2 Windows 2016 AD DS servers configured with one Domain.    

We would like to migrate them to Windows 2022.    

So far, one of the two servers (DC1) was upgraded to 2022, the other one is still 2016 (DC2).    

Everything is installed and configured in French (FYI)    

Might also be important : This Domain was originally configured with 2012R2 AD DS Server, was upgraded to 2016 and has now 2016 functionnal level.    

When opening Group Policy Management Console, we have a warning with the replication status of the GPOs.    

The error can be (badly) translated in English by :    

Sysvol Authorizations on one or more GPOs on this domain controller are not synchronized with the GPOs authorizations on the base domain controller !    

![243017-image.png][1]    

Followed by a list of ~20 GPO names.    

We have about ~60 GPOs in total.    

I think I tried all the repadmin/dcdiag/dfsrdiag I could find not showing any errors...    

Worthless to say that the SYSVOL\domain on the two servers have the same file/folder/size count !    

Any ideas ?    

Regards,    

GS

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-25*

Hello,

Sounds like you are right ! or at least not too far !

Here is a snip of errors I can find in the log file :

<ERRORS><ERROR><STATUS>SYSVOL_ACL_MISMATCH</STATUS><SECONDARY folder='1'>\DC2.mydomain.univ.fr\sysvol\mydomain.univ.fr\policies{0B7A2270-D69E-4B6E-972E-C5B0035B8179}</SECONDARY></ERROR></ERRORS></POLICY><POLICY>

<DC>  

<NAME>DC1.mydomain.univ.fr</NAME>  

</DC>

I need to test the latest NetTools debug options :)

GS.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-25*

Hi @Guenael Sanchez       

You can enable additional debug information with GPMC which may help identify the reason for the ACL errors, if you create the following registry entries on the machine that is running GPMC:    

    

```
HKLM\Software\Microsoft\Windows NT\CurrentVersion\Diagnostics  
Value: GPMgmtTraceLevel  
Type: REG_DWORD  
Data: 2  

HKLM\Software\Microsoft\Windows NT\CurrentVersion\Diagnostics  
Value: GPMgmtLogFileOnly  
Type: REG_DWORD  
Data: 1
```

This will result in the gpmgmt.log file being created in the %Temp% directory, i.e. TEMP=C:\Users\ADMINI~1\AppData\Local\Temp    

When you run the Detect Now on the Status tab of the GPO the log file will contains the details of the Permissions that have been found in both the AD and Sysvol.  The logging seems a little inconsistent as caching seems to change what is logged and may require GPMC to be restarted a few times to get the full details into the log.    

From the testing I've done so far, it looks like the order of the permissions in the Sysvol DACL is important, while the overall permissions are the same, if they are in a different order the GPMC Status seems to report an ACLs issue as shown below.    

    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-21*

Hey,    

Thanks for your reply ! It seems interesting ! And thanks for the debugging on NetTools ;)    

My first guess was to create a file in sysvol folder and It's immediatly replicating on the other AD DS Server.    

But Modifying ACLs on a buggy GPO impacts local (DC1) SYSVOL GPO Folder ACLs and those ACLs are not replicated on DC2 SYSVOL GPO Folder.    

Running again dcdiag on DC2 shows some errors about unavailable RPC on DC1 (same errors about DC2 when running dcdiag on DC1):    

```
Démarrage du test : DFSREvent
```

```
The DFS Replication Event Log.   
     Impossible d'interroger le journal des événements DFS Replication sur  

     le serveur DC1.mydomain.univ.fr. Erreur 0x6ba  

     « Le serveur RPC n'est pas disponible. »  

     ......................... Le test DFSREvent  

      de DC1 a échoué  
  Démarrage du test : SysVolCheck  

     * Test de préparation de SYSVOL pour le service de réplication de  

     fichiers   
     SYSVOL du service de réplication de fichiers est prêt   
     ......................... Le test SysVolCheck  

      de DC1 a réussi
```

DFSREvent test fail with unavailable RPC    

SysVolCheck passes.    

when Initial connectivity and RPC tests pass on both DC1 and DC2 :    

Exécution des tests initiaux nécessaires    

   Test du serveur : Default-First-Site-Name\DC2    

```
Démarrage du test : Connectivity  

     * Active Directory LDAP Services Check  
     Determining IP4 connectivity   
     Determining IP6 connectivity   
     * Active Directory RPC Services Check  
     ......................... Le test Connectivity  

      de DC2 a réussi
```

   Test du serveur : Default-First-Site-Name\DC1    

```
Démarrage du test : Connectivity  

     * Active Directory LDAP Services Check  
     Determining IP4 connectivity   
     Determining IP6 connectivity   
     * Active Directory RPC Services Check  
     ......................... Le test Connectivity  

      de DC1 a réussi
```

Still digging...    

Regards,    

GS.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-21*

Hi @Guenael Sanchez       

Have a look at this question which might help.    

https://learn.microsoft.com/en-us/answers/questions/845559/problems-with-sysvol-replication-gpos-out-of-sync.html    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-20*

screenshot did not make it in the previous post ...
