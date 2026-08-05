---
title: "Demoting AD Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1114139/demoting-ad-domain-controller
question_id: 1114139
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Demoting AD Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1114139/demoting-ad-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we try to force the demoting of an AD Domain Controller we keep getting the error below     

The operation failed because:    

Failed to prepare for or remove the sysvol replication     

the operation identifier is not valid

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-12-02*

The simplest solution may be to remove the failed one from network then perform some cleanup to remove remnants.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-02*

The new DC does not see the old one since we removed everything from sites and services and users and computers

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-02*

C:\Windows\system32>ntdsutil    

ntdsutil: metadata cleanup    

metadata cleanup: connections    

server connections: connect to server tf-dc1    

Binding to tf-dc1 ...    

DsBindWithSpnExW error 0x5(Access is denied.)    

ldap_search for attribute supportedCapabilities failed with 0x59(89 (Parameter Error).    

)    

server connections:

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-02*

C:\Windows\system32>ntdsutil    

ntdsutil: metadata cleanup    

metadata cleanup: remove selected server TF-DC1    

Binding to localhost ...    

Connected to localhost using credentials of locally logged on user.    

LDAP error 0x22(34 (Invalid DN Syntax).    

Ldap extended error message is 0000208F: NameErr: DSID-03100232, problem 2006 (BAD_NAME), data 8350, best match of:    

        'CN=Ntds Settings,TF-DC1'  

Win32 error returned is 0x208f(The object name has bad syntax.)    

)    

Unable to determine the domain hosted by the Active Directory Domain Controller (5). Please use the connection menu to specify it.
