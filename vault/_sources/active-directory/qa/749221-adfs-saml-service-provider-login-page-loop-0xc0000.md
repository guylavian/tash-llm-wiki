---
title: "ADFS - SAML service provider login page loop: 0xC00002FD An error occurred during Logon"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/749221/adfs-saml-service-provider-login-page-loop-0xc0000
question_id: 749221
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - SAML service provider login page loop: 0xC00002FD An error occurred during Logon

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/749221/adfs-saml-service-provider-login-page-loop-0xc0000 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I setup the ADFS on windows server 2016 and added the relying party trust. There seem to be similar docs but I followed this https://help.talentlms.com/hc/en-us/articles/360014573874-How-to-configure-SSO-with-Microsoft-Active-Directory-Federation-Services-2-0-ADFS-2-0-Identity-Provider

I tried to login through the service provider and it directs to SSO page in AD FS but once I enter the correct credentials I see the same AD FS login page again - no errors. And, if i enter wrong credentials it displays the right error.

Upon some digging in Event Viewer on AD FS side I was able to see some Audit Failures under Security event viewer. It says the following error. I already chose SHA1 encryption for the relying party trust but still stuck with the below error.

Account For Which Logon Failed:  

Security ID: NULL SID  

Account Name:  

Account Domain:

Failure Information:  

Failure Reason: An Error occured during Logon.  

Status: 0xC00002FD  

Sub Status: 0x0

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

Adding the Active Directory tag as this is not an AD FS centric issue.  

The error message format you have here looks like the content of an event id 4625 (please confirm). That's not an AD FS thing, that's Windows failing to authenticate the user. The error 0xC00002FD seem to map STATUS_KDC_UNKNOWN_ETYPE. Which looks like the issue is with a Kerberos authentication encryption type. Nothing to do with the AD FS relying party trust signature configuration.   

As this point, there's not much we can investigate on the AD FS servers. You will need to look at the Kerberos oeverall configuration of your environment. It looks like a Kerberos Encryption Type issue.   

Some element you can add to help us out...  

-  Give us the actual event id.  

-  Is the AD FS service account a gMSA account or a regular account?  

-  What is the version of your Active Directory domain controllers?  

-  Have you tried to test with a newly freshly created user on another machine? Maybe you have some restrictions on the Kerberos encryption type you can use with your account/machine.
