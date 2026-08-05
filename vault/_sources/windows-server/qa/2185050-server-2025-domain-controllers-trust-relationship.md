---
title: "Server 2025 Domain Controllers - Trust relationship issues on workstations after 30 days as \"pwdLastSet\" value unable to be updated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185050/server-2025-domain-controllers-trust-relationship
question_id: 2185050
fetched: 2026-07-25
answer_count: 54
has_accepted_answer: false
upvotes: 71
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Server 2025 Domain Controllers - Trust relationship issues on workstations after 30 days as "pwdLastSet" value unable to be updated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185050/server-2025-domain-controllers-trust-relationship (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

We have 4 Domain controllers upgraded to server 2025 and about 30+ still on 2022. The newly upgraded servers appear to have a bug where by any workstations going through them are unable to update their "pwdLastSet" value and so after the 30 day limit on that field is hit they then fall into a trust relationship issue with the domain. Is this a known bug of server 2025? Are there any known fixes for this issue?

## Answer (community) — community member

*upvotes: 3 · updated: 2025-02-25*

Hello Erin Teu

We have the same exact problem after updating our DC's to 2025. The Problem can be seen on Windows 10 22H2 PC's as well. Besides the machine password expiration issue, we ran into a problem where our two Cisco radius servers are no longer able to succesfully negotiate with 2025 DC's.

Cisco Support has identified the problem and it points down to a Microsoft kerberos bug. See the reply from Cisco Support below.

Hello, Team

I hope you are doing well today!

My name is Abdullah Lodhi and I am with Cisco Systems AAA team and I will be working on your case SR 698715209.

I have gone through the case notes and I am looking into this issue. So this bug is for Windows Server when it is 2025 the integration with ISE is failing due to a microsoft check. It has been traced back to the krb5 library in the ADRT in the gmt_mktime.c file in the krb5int_gmt_mktime function. In it, there is an explicit check to see if the received timestamp is after the year 2038 and if so, the assert fails and returns -1.  The function is called by the asn1_decode_generaltime function in the asn1_decode.c file which then returns the LW_ERROR_KRB5_ASN1_BAD_TIMEFORMAT error.

This flow is triggered by the first TGT obtaining during kerberos. In the AS-REP, AD 2025 sends a default expiry time of year 2100 (expiry time of the session key that is used to encrypt the traffic between the client and the KDC) and when processing this response the ADRT eventually gets to parsing the expiry date and throws the LW_ERROR_KRB5_ASN1_BAD_TIMEFORMAT error.

As from our side the only workaround is to revert back to 2022 Windows AD as there is no fix from Cisco as the issue is on Microsoft Side and we are pending a fix from them. Please let me know if you have any questions in regards to the bug, if not please let me know if we can proceed with case closure.

Thank you,

Until Microsoft releases a fix to our problem, i will set the password expiration date in the meantime to infinit.

Best regards

Christian

## Answer (community) — community member

*upvotes: 3 · updated: 2025-02-12*

No fix in Update 2025-02.

## Answer (community) — community member

*upvotes: 3 · updated: 2025-01-16*

More confirmation that this is an issue with 23H2

Anything with version 26100 (24H2) is updating.

Anything with version 22631 (23H2) is not updating and generating bad password attempts.  

I also am seeing kerberos preauth failures in wireshark captures from both the client and domain controller.  

As a test I also added a computer to the domain administrators group in case there may be some strange permissions issue, forced a computer password change, then waited a day (per the test GPO requirements) and the password did not change.

## Answer (community) — community member

*upvotes: 3 · updated: 2025-01-06*

I am seeing the trust relationship breaking on 2 networks now with Server 2025 domain controllers. One is standalone, the other has 3 DCs. I am putting this fix out there as it has helped work around most of the issues temporarily.

The fix so far has been:  

-  Unplug network cable on client machine

-  Log into the machine using a cached or local administrator account

-  Connect network cable

-  Run "reset-computermachinepassword -credentials domain\domainadminuser -server domaincontroller"

-  Disable and enable the network connection or reboot

Client machines are other Server 2025 servers, other DCs, and Windows 11 Pro workstations that have upgraded to 24H2. One network is an in-place upgrade from Server 2022 and the other is a fresh Server 2025 install. The in-place had a fresh DC installed with the page size altered to the 32k page size. The previous DCs were demoted and then enrolled to pick up the new 32k page size.

I am still troubleshooting and trying to locate event logs that are relevant.

My gut feeling is due to NTLMv1 being removed as I am seeing several Kerberos pre-authentication errors in the logs around the timeframes the issues start occurring. Event ID 4771  

I also found some of the machines lost rights to update their own records in DNS as the GUID for their computer object has changed.  

My guess is many large organizations have not updated to Server 2025 yet, so all these behaviors will be noticed on smaller test networks first.

## Answer (community) — community member

*upvotes: 2 · updated: 2025-01-09*

I set the maximum machine age policy to 3 days on a test domain with Windows 11 24H2 clients and they all lost their trust relationship and would not authenticate. They also did not update their pwdlastset values in AD.

Immediately after unlinking the GPO, they were able to authenticate again. Setting to a higher value of 365 days and linking the GPO also allowed them to authenticate.

Using the reset-computermachinepassword command does change the pwdlastset date.

I've enabled several logs on the domain controllers and am attempting to decipher which may be of value. The biggest standout is a large number of event 4771 pre-kerberos authentication events from the workstations

Log Name:      Security

Source:        Microsoft-Windows-Security-Auditing

Date:          1/9/2025 8:04:41 AM

Event ID:      4771

Task Category: Kerberos Authentication Service

Level:         Information

Keywords:      Audit Failure

User:          N/A

Computer:      DC.domain.com

Description:

Kerberos pre-authentication failed.

Account Information:

```
Security ID:		domain\workstation$

Account Name:		workstation$
```

Service Information:

```
Service Name:		krbtgt/domain.com
```

Network Information:

```
Client Address:		::ffff:10.0.44.102

Client Port:		65463
```

Additional Information:

```
Ticket Options:		0x40810010

Failure Code:		0x18

Pre-Authentication Type:	2
```

Certificate Information:

```
Certificate Issuer Name:		

Certificate Serial Number: 	

Certificate Thumbprint:
```

Certificate information is only provided if a certificate was used for pre-authentication.

Pre-authentication types, ticket options and failure codes are defined in RFC 4120.

If the ticket was malformed or damaged during transit and could not be decrypted, then many fields in this event might not be present.
