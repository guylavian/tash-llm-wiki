---
title: "Some DCs require GSSAPI for LDAP connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163642/some-dcs-require-gssapi-for-ldap-connections
question_id: 1163642
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Some DCs require GSSAPI for LDAP connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163642/some-dcs-require-gssapi-for-ldap-connections (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have weird issue that has cropped up. We have 8 writable Domain Controllers and 2 RODCs, all are 2016.  

We updated all but 3 DCs to block use of TLS1.0/1.1 and bunch of depricated hashes and cyphers etc.  

After this we have noticed some issues with LDAP queries from some applications to specific DCs, they appear to make a connection but can not enumerate AD.  

I have reverted the changes, even to the extent of positively allowing the previously blocked stuff, but the problem persists.  

Using LDP and LDAPAdmin I can make a connection, however, a Bind fails unless I use GSSAPI on LDAPAdmin and Negotiate on LDP.

Additionally, if, when using LDP, I bind with a Domain Admin account it will work, if i bind with a normal User it fails.

Note: ADUC works with out any issues on all accounts.  

As far as I can tell all DCs are configured the same, with the same group policies being applied, the only difference is some registry settings to block the use of old TLS and hash versions.

I have enabled additional auditing of LDAP connections but can see nothing in the event logs for these failed connections.  

Looking at the connection logs, there is no difference between one that fails and that works in LDP.  

The only mention i can find in the logs for GSSAPI is  

"supportedSASLMechanisms (4): GSSAPI; GSS-SPNEGO; EXTERNAL; DIGEST-MD5;"

This is the same for all DCs, we are not using LDAPS for connection to the DCs at the moment.

Am looking for pointers as we have a number of systems that don't seem to want to play with the updated servers

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-20*

I believe the issue was an incorrect registry key.  

The below key should be set as  

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders]  

"SecurityProviders"="credssp.dll, pwdssp.dll"

 

But on broken servers it is

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders]  

"SecurityProviders"="credssp.dll"

Without that pwdssp.dll it treats all LDAP binds as Anonymous and so they don't work as expected. Adding it back and restarting teh server and all is well again.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-08*

Sorry taken me 2 weeks of searching Microsoft to get back to these support pages rather than all other ones....

Basically Blocked TLS 1.0 and 1.1, Blocked use of RC4, DES 56/56, Triple DES 168. by setting registry keys in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL.

Also enforced SMB signing and added a couple of reg keys to enforce strict authenticode signing.

I have reverted all the changes, to the extent of positively allowing the settings, but it seems to have tripped a switch, also not updated servers appear to be affected for some apps but are for others.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-25*

Hi,

Are you able to share what changes you made to TLS and which ciplher you disabled?

By default, LDP will use the LDAP protocol (port 389) to connect to the server, so disabling TLS wouldn't impact an LDAP connection. However, LDAPS connection could be impacted.  Typically LDAPS connections are used by third party application or devices for authentication and authorization.  Disabling ciphers might impact an LDAP connection but would need to see what ciphers have been disabled, and if you implemented any changes to the msDS-SupportedEncryptionTypes associated to any of the application accounts.

Gary.
