---
title: "Kerberos delegation & Applications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3189033/kerberos-delegation-applications
question_id: 3189033
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Kerberos delegation & Applications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3189033/kerberos-delegation-applications (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Helllo all,

Here below is my understanding about Kerberos delegation :  

1] Unrestricted delegation (W2000): Windows 2000 allows a authorized user to forward a TGT: he asks for a forwardable TGT (Authentication Service) and can then ask for a forwarded TGT (Ticket
 Granting Service) he may .. forward along with the session key (shared with the KDC for this forwarded TGT) to a service (krb_cred message). The service may then request a ticket service on the user's behalf for any service and may in turn also forward the
 TGTto any other service [proxiable/proxy tickets are out of scope since it seems not to be used due to the prerequisites it requires],

2] Restricted delegation (since W2003) : A IT admin can configure a service in the AD (SPN) to be authorized to request a ticket service on behalf of a user for a set of services (SPN) : "Allowed-To-Delegate-To"
 (A2D2) parameter. Moreover, a new extensions (S4U2Proxy) allows a service to request a ticket service on the user's behalf for an other service since it is able to present a valid and forwardable ticket on the behalf of the user for itself (so, it means there
 is no need anymore to get the TGT from the user and its associated session key). To get a forwardable ticket for itself, the service shall be tagged as "Trusted-To-Authenticate-For-Delegation" (T2A4D),

3] Protocol Transition (S4U2self) (since W2003) : A service may ask the KDC for a ticket service (for itself) on behalf of the user without showing any evidence to the KDC indicating the user
 has been authenticated by Kerberos. This can be done by enabling the flag "Use any protocol" in the configuration of the SPN in the AD. Then, it could use constrained delegation if the proper flags (T2A4D and A2D2) are set for this service,

4] Constrained delegation cross domains (since W2012) :

¤ Where before it wasn't possible to use delegation cross domains (because not possible to set a SPN out ot the current domain of a SPN), authorization can now be configured on the target service instead of
 the source service (conceptually, it's more logical).

¤ A specific SID ($$) may be configured on the target service to authorize or not a delegation when the user was not explictely authenticated by the KDC (it means when a service used its protocol transition
 ability to get a ticket for itself) : in order for this to work, it means (I guess) that the ticket service granted to the source service for the target service contains this information.

What is not clear to me:

-  After reading MS articles, I understand that forwarded TGTs cannot be used to do constrained delegation although there is clearly a "forwarded" flag in the TGT. Indeed, this is quite different compared to
 a service which uses its own TGT with a ticket service for itself, because with the user's TGT, the service is authenticated as the user which requests a service ticket. Is there any meaning in using the "address" field of a ticket request, which is intended
 to contain the iP/DNS address of the requestor (this could be modifiable of course) ? Is there any parameter to refuse a ticket request when a forwarded TGT is used ? Why not use the adress field (client) to check the associated rights ? Is it because it's
 not reliable (address may be spoofed) or because it's not precise enough to identify a SPN ?

-  Introducing the SID ($$) implies to me that the forwardable service ticket does contain a specific information saying this ticket was obtained through S42Uself extensions or was directly obtained by the
 user. But I don't know what it is,

-  Forwarded TGTs seem to be "deprecated" if it means delegation cannot be constrained. So, I don't understand why there are one forwardable and one forwarded TGT (so for delegation) when I display my cached
 tickets using klist (Windows 10 machine in a corporate environment, and this for two different compagnies). Is is a standard and recommended practice or do I miss something ?

Thanks a lot for your feedback !! Have a great day.

OolaHoop.

## Answer (community) — community member

*upvotes: 0 · updated: 2019-05-16*

Best to ask in below forums:

-  https://social.msdn.microsoft.com/forums/

-  https://social.technet.microsoft.com/forums/en-us/home
