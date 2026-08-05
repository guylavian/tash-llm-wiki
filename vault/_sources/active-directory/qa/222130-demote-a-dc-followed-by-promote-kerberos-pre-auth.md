---
title: "Demote a DC followed by promote. Kerberos PRE-AUTH, mandating RC4-HMAC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222130/demote-a-dc-followed-by-promote-kerberos-pre-auth
question_id: 222130
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Demote a DC followed by promote. Kerberos PRE-AUTH, mandating RC4-HMAC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222130/demote-a-dc-followed-by-promote-kerberos-pre-auth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I am working with Windows 2019 Server and observing a weird behavior.    

My server was promoted as a DC. Then for testing reasons, I had to demote it and then re-promote it.    

What I now observe is that the encryption types sent by AD for the KRB PRE-AUTH step specify only 1 enctype - RC4-HMAC    

    

While it was supporting both AES and RC4 just before demotion, for the same user    

    

I thought maybe I did something wrong. So fired up another DC, ran the same scenario and verified that it's the same behavior. I ran this scenario now on 3 different DCs, yup I had that much free time ;)    

For a newly created user, however, both the enctypes are being supported for pre-auth step:    

    

Things become more interesting if I now try to disable RC4 on the AD server. Since the pre-auth still mandates RC4 for the old user, it fails in the very next step with unsupported enctype error.    

Like this. Client replies in RC4 enctype    

    

But server says not supported :). Dude !! You asked for RC4 a couple of frames ago

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-27*

Hello @Varun Mittal  ,    

I have done the test.    

Step 1    

I deploy a domain with a 2019 DC and a Windows server 2016.    

Join this 2016 server to the domain.    

Capture the netmon when I join the 2016 server to domain on both DC and client.    

Here is the netmon on DC    

    

Here is the netmon on client.    

    

Step 2    

Demote the DC.    

Remove the server from domain.    

Step 3    

Re-promote the DC.    

Re-join the client.    

Capture the netmon when I join the 2016 server to domain on both DC and client.    

Here is the netmon on DC    

    

Here is the netmon on client.    

    

I can also see via one pre-auth as below.    

    

Note: I kept the same password for the administrator user on DC and client, 'Password123!', after promote/demote. Did not change the password at all    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-14*

Hello @Varun Mittal  ,    

Thank you for your update.    

I did a test in my lab yesterday.    

Here is AD domain environment.    

Domain name: a.com    

Two Windows server 2019 DCs (Primary DC---PDC and backup DC---BDC).    

PDC:2019standard 192.168.3.50    

BDC:AdditionalDC 192.168.3.57    

Test one     

-  On BDC, I disabled KDC.    

-  On PDC, open network monitor (right click network monotor and run as Administrator), start capture.    

-  On BDC, run command: ipconfig /flushdns to clean DNS cache, and nbtstat -RR to clean NETBIOS cache.  Run klist purge command.    

-  Logon the BDC using domain Administrator.    

-  On PDC, stop cauture.    

Time stamp: 2020/1/13 14.13PM    

Test two    

Demote BDC as member server in the domain.    

And logon this member server using domain Administrator and capture the netmon as above.    

Time stamp: 2020/1/13 15.12PM    

Test three    

Repromote the member server (BDC server) as DC again.    

And logon new BDC server using domain Administrator and capture the netmon as above.    

Time stamp: 2020/1/13 16.18PM    

In the three netmon, I find the same result as below.    

    

Test one result:    

    

Test two result:    

    

Test three result:    

    

You can set up a test lab if possible, and check the result to see if the result is the same as you mentioned in the post.    

Best Regards,    

Daisy Zhou

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-08*

Hi,    

By default , RC4 still enabled for kerberos encrytion on new operating system.    

Before disable this encryption type , you have to check if all kerberos clients in your environment can support AES 256.    

To disable RC4, you have two methods you can use the attribute of the computer account  msDS-SupportedEncryptionTypes or use a GPO settings to specify the lis of supported kerberos encryption type.    

You can read this article to get more details about how you can disbale RC4 : windows-configurations-for-kerberos-supported-encryption-type    

----------    

Please don't forget to mark the helpful reply as answer

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-08*

Hello @Varun Mittal  ,    

Thank you for posting here.    

Based on the description "While it was supporting both AES and RC4 just before demotion, for the same user", I understand the DC before demotion supports AES and RC4.    

And the new created user all the new promoted DCs supports AES and RC4.    

Based on the description "What I now observe is that the encryption types sent by AD for the KRB PRE-AUTH step specify only 1 enctype - RC4-HMAC", do you mean the re-promoted DC only supported RC4?    

Here we can see encryption types configuration as below:    

Attribute    

msDS-SupportedEncryptionTypes    

UserAccountControl    

Group Policy    

Network Security: Configure Encryption types allowed for Kerberos    

Registry    

SupportedEncryptionTypes    

DefaultEncryptionType    

KdcUseRequestedEtypesForTickets    

Here is the Etype of authenticator in pre-authentication below.    

If  registry setting DefaultEncryptionType is set to a non-zero value    

     Client will use this value as the Etype in pre-authentication  

Else    

       If  Etype related Group Policy is set  

            Client will pick the strongest Etype in the supported list set in GP  

       Else  

             If client is running on machine before Windows 7/Windows 2008  

                  Its supported encryption list includes RC4 and DES  

             Else  

                  Its supported encryption list includes AES, RC4 and DES  

We can check the following registry values on this DC and user's domain PC:    

SupportedEncryptionTypes (corresponding to GPO setting Network Security: Configure Encryption types allowed for Kerberos)    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\SupportedEncryptionTypes    

KdcUseRequestedEtypesForTickets    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Kdc\KdcUseRequestedEtypesForTickets (DWORD)    

If the value of this key is non-zero, the server will try and use the highest encryption level supported by the client PC.     

DefaultEncryptionType    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\DefaultEncryptionType    

Entry: DefaultEncryptionType    

Type: REG_DWORD    

This value indicates the default encryption type for pre-authentication. Default value is RC4 is 23 (decimal) or 0x17 (hexadecimal)    

When you want to use AES, set the value to the following:    

aes256-cts-hmac-sha1-96: 18 or 0x12    

aes128-cts-hmac-sha1-96: 17 or 0x11    

Tips:    

If you can not find SupportedEncryptionTypes or DefaultEncryptionType under     

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\SupportedEncryptionTypes    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\DefaultEncryptionType    

You can find SupportedEncryptionTypes or DefaultEncryptionType under     

HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\SupportedEncryptionTypes    

HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\DefaultEncryptionType    

Hope information above is helpful. If anything is unclear, please feel free to let us know.    

References    

Kerberos protocol registry entries and KDC configuration keys in Windows    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/kerberos-protocol-registry-kdc-configuration-keys    

Decrypting the Selection of Supported Kerberos Encryption Types    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797    

Use the UserAccountControl flags to manipulate user account properties    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties    

Best Regards,    

Daisy Zhou
