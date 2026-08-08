---
title: "Upgrade from LDAP to LDAPs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/82825/upgrade-from-ldap-to-ldaps
question_id: 82825
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Upgrade from LDAP to LDAPs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/82825/upgrade-from-ldap-to-ldaps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys, just saw this article: https://www.aeb.com/support/en/news/ldap-change.php  

Do we have to upgrade from LDAP to LDAPs now? What impact will it have?   

Thanks  

ML

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-09-01*

Hi,  

Do we have to upgrade from LDAP to LDAPs now? What impact will it have?  

You should set LDAPS instead of LDAP if you application support LDAPS protocol.  

It's recommended to secure the LDAP communication between yours applications and domain controllers by forcing your application to use only LDAPS if it support it.  

If the application support it there is no impact. You should ask the editor or the developer to be sure if your applications support LDAPS protocol.  

You should monitor the certificate installed on domain controllers , because when the certificate is expired or delivered from untested PKI, it may generate application issue.  

Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-02*

Hello,  

Thank you so much for your feedback.  

The March 10, 2020 updates do not change LDAP signing or LDAP channel binding default policies or their registry equivalent on new or existing Active Directory domain controllers. March update will not make any change to signing or channel binding.  

Before making the changes, we will find out if Appliances/Devices/Applications support Signing and Channel Binding. Group device types into 1 of 3 categories:  

1,Appliance or router  

Contact the device provider.  

2,Device that does not run on a Windows operating system  

Verify that both LDAP channel binding and LDAP signing are supported on the operating system and then application by working with the operating system and application provider.  

3,Device that does run on a Windows operating system  

LDAP signing is available to use by all applications on all supported versions of Windows. Verify that your application or service is using LDAP signing.  

LDAP channel binding requires that all Windows devices have CVE-2017-8563 installed. Verify that your application or service is using LDAP channel binding.  

Yes, we need to have them both configured. According to the documents, below are the configure recommended values for Signing and CBT:  

LdapEnforceChannelBinding=1 (1 indicates enabled , when supported) (must have CVE-2017-8563)  

LDAPServerIntegrity=2 (2 indicates Require Signing)  

We could configured the Policy settings or the Registry Setting. As for the settings, we could refer to the provided documents. Here we would like to share more information with you about how to enable LDAP signing.   

https://support.microsoft.com/en-us/help/935834/how-to-enable-ldap-signing-in-windows-server  

For any question, please feel free to contact us.  

Best regards,  

Hannah Xiong

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-02*

When tried LDP, it says LDAPs is enabled.....I cannot see any reg keys saying enabled...Really confused now.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-02*

Hi Thanks for that.   

Would normal LDAP break so some old incompatible service stop?   

ML
