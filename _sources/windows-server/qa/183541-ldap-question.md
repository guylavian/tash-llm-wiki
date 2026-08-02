---
title: "LDAP question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/183541/ldap-question
question_id: 183541
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# LDAP question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/183541/ldap-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Can someone tell me which march updates are for Enabling LDAP Channel Binding and LDAP Signing?  

my understanding is that this update in combination with some registery settings will allow us to log the LDAP connections issues and after solving that we can install the KB4586830 of November.  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-03*

Hi,  

1,If you configured the policy correctly and it works , the registry will be changed according the policy. It will be the same result with setting the registry directly.  

Normally, the policy is recommended instead of setting the registry directly.  

2,Important: The March 10, 2020 updates, and updates in the foreseeable future, will not change LDAP signing or LDAP channel binding default policies or their registry equivalent on new or existing Active Directory domain controllers.  

    The updates provide the LDAP security options for administrators to harden the configurations for LDAP channel binding on Active Directory domain controllers.  

If there is anything else we can do for you, please feel free to post here.  

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

Thank you for your reply,  

Did you set this already in your enviornment? may be you can help me to understand this.   

We have to yet install the march updates on all of DC's in the domain, we have 4 server 2012 DC's 1 server 2016 DC. After installing the updates we should set only these 2 policies:  

Domain controller: LDAP server channel binding token requirements  

Domain controller: LDAP server signing requirements  

Or we can instead after installing the march update use the registry setting? or we have to set the policy and also set the registry after installing the updates?  

Also I see this on the  DC 2012 that hosts all of the FSMO roles:  

Domain controller: LDAP server channel binding token requirements ( Not Defined)  

Domain controller: LDAP server signing requirements (None)  

Also what I dont understand is this registry 16 LDAP Interface Events is already set to 2 on all of the server 2102 DC's and we see the info event 1535.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-02*

Kindly go through the following Microsoft article:  

2020 LDAP channel binding and LDAP signing requirements for Windows
