---
title: "Can a non-domain Windows client use Kerberos to access a domain SMB share with domain credentials?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277125/can-a-non-domain-windows-client-use-kerberos-to-ac
question_id: 2277125
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can a non-domain Windows client use Kerberos to access a domain SMB share with domain credentials?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277125/can-a-non-domain-windows-client-use-kerberos-to-ac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm working in a Windows environment with the following components:

-  An Active Directory Domain Controller (Windows Server),

A file server (SMB) that is joined to the domain,

A Windows client that is not joined to the domain (workgroup machine).

From this non-domain client, I am trying to access a file share on the domain-joined SMB server using domain user credentials (e.g., `DOMAIN\username`).

I would like to understand in detail which authentication mechanism is used in this scenario.

My questions are:

Can a non-domain client use Kerberos to authenticate to the SMB server using domain credentials?

If not, does the authentication automatically fall back to NTLM? If so, what is the detailed flow between the client, the file server, and the domain controller?

Is there any way to enable or force Kerberos authentication in this scenario without joining the client to the domain?

Additional Information:

-  The SMB server is accessible via its FQDN and is correctly joined to the domain.

-  The client is running Windows 10.

-  The SPN is correctly configured on the SMB server's domain computer account.

I've looked for a clear explanation in the Microsoft documentation, but I haven't been able to find a definitive answer. If anyone can clarify this behavior, it would be greatly appreciated.

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-05-26*

Hi all,

That's the old question but I did see the Kerberos authention on Windows Server 2022 file server for the logon attempt from a standalone workstation. More information is here: 

https://learn.microsoft.com/en-in/answers/questions/5646439/authentication-problem

In short:

"Kerberos authentication is only available when both the client and server are domain-joined and can communicate with a domain controller. For non-domain (workgroup) computers, NTLM is typically used for authentication to domain resources. Cached credentials in the registry (the encrypted verifier) are only relevant for offline interactive logons on domain-joined machines, not for network share access from non-domain systems.

If you are seeing Kerberos authentication from a standalone (non-domain) computer to a domain server, this is unexpected according to standard Windows authentication workflows. Normally, such a connection would use NTLM, unless there is some mechanism (such as a domain trust, or the client is actually domain-joined or has access to domain credentials) that allows Kerberos to be used."

From the other hand:

https://serverfault.com/questions/455793/kerberos-authentication-for-workstations-not-on-domain

In short:

"Old question, but the answers are not particularly accurate.

Windows doesn't especially care whether your computer is domain joined or not. The domain join in this stage of authentication is really just a hint to tell the client what domain it maybe should try contacting if enough information isn't present.

The way Kerberos auth works is it takes a look at the creds presented to it during authentication. If the username provided has enough information to resolve a domain controller it will happily attempt Kerberos immediately. It will only fall back to NTLM if there isn't enough information provided by the user for the client to find a DC. It basically works like this:

User types `\\foo\share`

*User is prompted for creds, enters *****@bar.domain.com and password

Windows sees bar.domain.com and does something called DC location, which, amongst other things, tries to resolve `SRV _kerberos._tcp.bar.domain.com` from DNS, which either points to a domain controller or it doesn't.

If a DC is returned, Windows attempts to get a TGT from the DC using the creds entered in (2).

If this fails it may do one of these depending on the errors returned:

a) go back to (3) and do round robin

b) fall back to NTLM

c) fail the attempt outright

Now it has a TGT for the user and it stuffs it into the ticket cache (see `klist.exe`).

With the TGT and DC it can talk to, it requests a service ticket for the SPN `cifs/foo`.

If the DC found a service account with that SPN it then returns a service ticket, otherwise it returns an error and Windows falls back to NTLM.

The service ticket is cached.

The client sends the service ticket to `\\foo\share` and SMB does it's thing.

This more or less is how it works on workgroup or domain joined computers. The only difference is step 2 and 3 differ. On a domain joined computer the creds are already known, and the domain is already known, so it uses the native SSO creds. DC location is still attempted, but it doesn't have to reason about the user's domain because it already knows it.

So the trick here is entering creds into step (2) such that Windows has enough information to find a DC. That means using the fully qualified domain name and not any custom friendly UPNs you have have added. It also means the legacy NetBIOS method of `bar\user` probably won't work. Maybe it will if you have enough legacy infrastructure to support it (remember NetBEUI?)."

Regards,  

Michael Firsov

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-20*

Hello,

Thank you for your response. The issue is that I haven't been able to find any official Microsoft documentation explicitly stating that, in order to obtain a TGT, the machine must be a domain member and that communication with the domain controller requires the machine account or its key.

For example, in the following document: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772815(v=ws.10), it is clearly mentioned that the system key is used only for acquiring a TGS and during interactive logon. However, when accessing a network resource, there is no indication that the system key is used, either for the TGT or the TGS.

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-19*

In short, no. The client would have to be domain-joined

Kerberos requires the client to obtain a Ticket Granting Ticket (TGT) from the KDC (a domain controller). Only machines that are part of the domain can securely authenticate to the KDC and obtain a TGT (which requires a secure channel with the domain via the machine account). Non-domain (workgroup) clients do not have a computer account or trust relationship with the domain, so they cannot request or receive Kerberos tickets.

Authentication could fall back to NTLMv2 given that both client and server support it.

Here is the corresponding authentication flow:

Step 1: Initial SMB connection

-  Client connects to the file server using SMB over TCP (typically port 445).

-  SMB session setup begins.

Step 2: Server challenges the client

-  The SMB server detects that the client is not using Kerberos (no TGT).

-  Server issues an NTLM challenge to the client.

Step 3: Client prompts for credentials (or uses cached ones)

-  The user provides `DOMAIN\username` and password.

-  The client generates an NTLM authentication response using the password.

Step 4: Server forwards the NTLM response to the domain controller

-  The file server, which is domain-joined, acts as a proxy for NTLM authentication.

-  It sends the challenge and the client’s response to the domain controller via Netlogon or LSASS.

-  This is known as NTLM pass-through authentication.

Step 5: Domain controller verifies credentials

-  The DC validates the NTLM response using the stored password hash of `DOMAIN\username`.

-  If successful, the DC replies with success to the SMB server.

Step 6: Server grants access

-  SMB server establishes the session with the authenticated user.

-  User accesses the share with the privileges defined for `DOMAIN\username`.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
