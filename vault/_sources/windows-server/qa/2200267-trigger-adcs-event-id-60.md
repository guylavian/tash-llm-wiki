---
title: "Trigger ADCS Event ID: 60"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2200267/trigger-adcs-event-id-60
question_id: 2200267
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# Trigger ADCS Event ID: 60

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2200267/trigger-adcs-event-id-60 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Community,

I need to trigger event :

60
High
Active Directory Certificate Services refused to process an extremely long request from %1. This may indicate a denial-of-service attack. If the request was rejected in error, modify the MaxIncomingMessageSize registry parameter via certutil -setreg CA\MaxIncomingMessageSize <bytes>. Unless verbose logging is enabled, this error will not be logged again for 20 minutes.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786423(v=ws.11)

Any tip on how to submit a request.size > 10000 bytes (Default)?

Thanks,

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-21*

Hello   

Good day!  

Microsoft-Windows-CertificationAuthority

Did you enable Audit Certification Services on CA server? You should.

  

Did you check the it via Application\Windows Logs\Microsoft-Windows-CertificationAuthority (below)?  

  

I have done a test in my lab, I cannot see it either.  

The link you provided in the original applies to the OS version below, my CA server is windows 2022.  

I'm not sure if the latest version of the server doesn't have this ID, or because the triggering conditions aren't correct.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-20*

Daisy, 

With the command prompt, I get 'Unknown argument: -keysize' error  

I have duplicated the template to use different keysizes for my tests:

Using MMC, I am not able to issue a enroll a certificate with keysize= 8192 when the MaxIncomingMessageSize= 1000  

Using MMC, I am able to issue a certificate with keysize= 16384 when the MaxIncomingMessageSize= 10000. Is this a bug? 

There is no event ID =60 under the EventsViewer list

Regards,  

Youcef

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-20*

Hello   

Good day!  

You can try request the certificate via mmc and select the key size 16384 (the request size below), then check if it will generate the event ID you want.

  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-20*

Hi, 

I have executed the below & restarted the CA:

certutil -setreg CA\MaxIncomingMessageSize 10

I get: 

The message provided exceeds the maximum size allowed for this parameter <CA NAME> 

Error parsing Request. The message provided exceeds the maximum size allowed for this parameter. 0x800710f0 (WIN32: 4336 ERROR_MESSAGE_EXCEEDS_MAX_SIZE)

There is no corresponding event in Events Viewer.

Regards,

Youcef

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-14*

Hello Yocef,  

Thank you for posting in Microsoft Community forum. 

How to generate an extremely long request ADCS? 

A: To generate an extremely long request in ADCS, you can use the CertReq.exe command-line tool with the "-new" parameter followed by the "-attrib" parameter and the "CertificateTemplate:" attribute.

For example, the following command will generate a certificate request for a template named "WebServer" with a key size of 4096 bits: 

```
certreq -new -attrib "CertificateTemplate:WebServer" -keysize 4096 mycert.req
```

Or you can try request the certificate via mmc, maybe the key size is the request size below:

Note that the maximum size limit applies to all certificate requests submitted to the CA, regardless of the method used to submit them.

I hope the information above is helpful. 

If you have any question or concern, please feel free to let us know. 

Best Regards, 

Daisy Zhou
