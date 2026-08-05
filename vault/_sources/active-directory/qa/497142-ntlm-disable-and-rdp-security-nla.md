---
title: "NTLM disable and RDP security (NLA?)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/497142/ntlm-disable-and-rdp-security-nla
question_id: 497142
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services"]
answer_author_roles: ["Q&A User"]
---
# NTLM disable and RDP security (NLA?)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/497142/ntlm-disable-and-rdp-security-nla (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

as it seems that every month new issues with NTLM are being published and many clients wish to know their systems are secured we are now analyzing the impact of completely disabling NTLM in their systems - this time for real...  

Latest news about PetitPotam lead to nearly every customer asking about NTLM so they are pretty concerned about that.  

Now I managed to configure / migrate all mission critical systems and forced them to use kerberos but still one pretty important part is missing: RDP and RDG.  

I tested disabling NTLM completely by setting the following three policies on DCs:  

-  Network Security: Restrict NTLM: NTLM authentication in this domain = deny all  

-  Network Security: Restrict NTLM: Incoming NTLM traffic = deny all accounts  

-  Network Security: Restrict NTLM: Outgoing NTLM traffic to remote servers = deny all  

But then most RDP connections failed with the following error:   

An authentication error has occured.  

The function requested is not supported  

Remote Computer: 192.168.xxx.xxx  

This could be due to CredSSP encryption oracle remediation.  

For more information, see https://go.microsoft.com/fwlink/?linkid=866660  

We always use the FQDN to connect to the affected clients.  

Furthermore it always happens via VPN or from other clients that are not part of the lab domain.  

That for me makes sense as kerberos is not working in every case these issues MUST occur.  

But now for real: what should we do with such clients that are forced to work over VPN, are not part of the domain or have temporary kerberos issues due to some minor network issues?  

I read we could disable NLA - any comments`/ suggestions on that?  

For me this simple solution for NTLM issues "completely disable NTLM and add some exceptions if really necessary" is far away from reality or simply not clearly enough communicated...  

Thank you for any input!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-19*

@Yankee Penky    we are in the same (painful) process as you and tried to debug this a little deeper.    

on the RDG server (and only there) we set Network security: Restrict NTLM: Incoming NTLM traffic back to Allow All.    

additionally, on the domain controllers we added the RDG servers FQDN to Network security: Restrict NTLM: Add server exceptions in this domain    

this made authentication work from the non-domain-device to the RDG (we got an MFA prompt). but the next hop, connecting from RDG to the target system, failed with the CredSSP encryption oracle remediation message.    

my takeway on this is that the authentication does not switch on the RDG from NTLM to Kerberos (why would it), but the RDG keeps forward-authenticating to the target system with NTLM. so to make this scenario work, we would have to enable "incoming NTLM" also on all systems that should be reachable from the RDG. which in our case, would be all clients. which in turn makes the whole idea of NTLM blocking pointless.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-07*

If NTLM is disabled, what are you trying to connect with?  Kerberos.  Since you won't have all the kerberosy goodness you have in your domain, when reaching out to the lab, you're going to have a failure.  

You'll want to look into what you need to do to make kerberos connections work out to the lab.  You could build a jumphost or airlock setup.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-02*

Hi,

1) I don't think it has anything to do with CredSSP Encryption Oracle Remediation as both Client (Windows 10 20H2) and Server (2019) are up to date and the gpo is set to "Force updated clients".

2) Yes that is clear - that is the reason why I do not want to disable NLA. Some years ago when it was introduced we were grateful to improve rdp security through that.

3) The lab setup is the following (e.g.):  

I am working on a PC connected to domain "outside.local" that is connected to the lab network via VPN, named workstation1.  

The lab AD (target domain) is contoso.com.

I tried to RDP directly from workstation1.outside.local to server1.contoso.com via an AD (admin) account in contoso.com - through VPN.

As I understood you try to explain that RDP without NTLM only works for devices joined to the same AD because kerberos requires AD for all parties?  

That is a real show stopper as we never work from our clients' machines but rather vpn to all our clients' networks.

If that is a requirement we will not be able to disable any NTLM as this connection strategy is required for all our operations...

Should it should work through RDG though?

Best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-02*

Hi,

1.For the error message of RDP failure on authentication error, it normally occurred when  

you are trying to establish an insecure RDP connection, and the insecure RDP connection is blocked by an Encryption Oracle Remediation policy setting on the server or client.

Stated as the link of CredSSP encryption oracle remediation you've shared, it is suggested to install the patch on both clients and target servers and setup secure connection via group policy to eliminate error message.  

2.NLA is an authentication method that can be used to enhance RD Session Host server security by requiring that the user be authenticated to the RD Session Host server before a session is created.  

If it is disabled, it will reduce the security for remote connection since there is no procedure to authenticate the user before establishing a session.

3.Active Directory Domain Services is required for default Kerberos implementations within the domain or forest.  

https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview  

If Kerberos authentication failed, it will utilize NTLM as alternative method. In our case, you've disabled NTLM and authentication failed since the clients are not part of AD.  

May I know if you are remoting via domain account?

If the Answer is helpful, please click Accept Answer and upvote it.

Best Regards,  

Jenny
