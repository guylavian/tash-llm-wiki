---
title: "create new object in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3191353/create-new-object-in-active-directory
question_id: 3191353
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
---
# create new object in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3191353/create-new-object-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Sorry for the novice question, but I'm trying to create a new class object so that any other system admin can create a new instance of it in Active Directory (as when adding a new user or group).

I created 2 attributes and 1 class with ADExplorer:

cn: myAttribute1  

objectClass: attributeSchema  

attributeID: 1.3.6.1.4.1.38971.1.1.2  

attributeSyntax: 2.5.5.12  

isSingleValued: FALSE  

adminDisplayName: myAttribute1  

adminDescription: myAttribute1  

oMSyntax: 64  

searchFlags: 1  

lDAPDisplayName: myAttribute1  

systemOnly: FALSE

cn: myAttribute2  

objectClass: attributeSchema  

attributeID: 1.3.6.1.4.1.38971.1.1.1   

attributeSyntax: 2.5.5.12  

isSingleValued: FALSE  

adminDisplayName: myAttribute2  

adminDescription: myAttribute2  

oMSyntax: 64  

searchFlags: 1  

lDAPDisplayName: myAttribute2  

systemOnly: FALSE

cn: myClassObject  

objectClass: classSchema  

governsID: 1.3.6.1.4.1.38971.1.2.1  

rDNAttID: cn  

adminDisplayName: myClassObject  

adminDescription: myClassObject  

objectClassCategory: 1  

lDAPDisplayName: myClassObject  

name: myClassObject  

systemOnly: FALSE  

subClassOf: groupOfNames  

mayContain: myAttribute1  

mustContain: myAttribute2  

I rebooted the AD server.

I registered the schema management DLL and loaded it in MMC.

I confirmed that the object and attributes were there.

However, I have two issues:

-  I'd like to be able to add new myClassObject instances from the serverr's control panel instead of using AdExplorer or an ldif file. The object myClassObject  does not appear in the "create new" drop-down menu.

-  If I create a myClassObject instance with AdExplorer, and then assign a user as member all seems to work as expected except when I browse to the properties of the AD user, open the "membership" tab, scroll down the different groups, but as soon as I hover
 over and click myClassObject  with the mouse, the AD console crashes with an unknown error (nothing useful in the log).

Any ideas?

Anything wrong in my object/attribute definitions above?

Thanks

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2019-04-25*

Hi VDP1 

Greetings! I am Vijay, an Independent Advisor. I am here to work with you on this problem.

This is a consumer Windows forum. AD related question is best answered at Microsoft's Technet forum. I would suggest that you should post simultaneously (i.e. cross-post) to Technet forum also. So, your question will be on two forums - This and Technet. 

Technet AD forum - https://social.technet.microsoft.com/Forums/en-...

Do let me know if you require any further help on this. Will be glad to help you.
