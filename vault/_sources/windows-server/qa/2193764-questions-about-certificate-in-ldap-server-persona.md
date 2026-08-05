---
title: "Questions about certificate in LDAP server personal store"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193764/questions-about-certificate-in-ldap-server-persona
question_id: 2193764
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# Questions about certificate in LDAP server personal store

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193764/questions-about-certificate-in-ldap-server-persona (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,

I have been working on an issue for a while and I have questions regarding our auto renewed certificate.

We have a 2 tire Microsoft PKI on-prem and some certs are auto renewed and auto enrolled. There are 2 certificates located in our local ldap server personal store and one of them is Kerberos and one is NAS, both of them providing Server Authentication for LDAPs.

The issue right now is that our services now doing LDAPs are now using NAS cert as it's just renewed with the furthest expiration time. I am trying to find a solution that we can use Kerberos for LDAPs.

I have the following questions if you can help me:

-  If I want to enforce the Kerberos one to be pushed when the services connect to our domain controller, with both 2 certs offering server authentication, how can I do that, I am not really considering import it to NTDS/personal as we will need to do it every year when it's renewed and it seems auto renewed cert won't work, and i will need to manually generate the cert for each domain controllers?

-  If I want to remove NAS cert from the personal store, in order to know the impact of removal, how can I tell if that certificate is applied somewhere and in use so i can plan the removal properly.

The PKI was set up by one of my colleagues and he left without transferring all the information, I am trying to figure out everything myself, please help me out if you know how to deal with this situation.

Thank you in advance. 

Have a nice day.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-12*

Hello Gina Qu,  

Good day!  

The kerberos cert is configured with auto renew and auto enroll every 2 years. 

A: How did you configure the kerberos cert with auto renew? Did you configure it via GPO?  

I saw from the documentations, the cert in NTDS/PERSONAL store won't be auto renewed, so I will need to import it every 2 years, is it correct?

A: I know we can auto renew user certs and machine certs via GPO (no service certs).  

If I import the kerberos cert to NTDS/personal, will the auto-renewal and auto enrolment still work and i need to import it every time when it's auto renewed? Can I automate this?  

A: If you import the kerberos cert to NTDS/personal, the auto-renewal and auto enrolment will still work.  

But i am not sure if you need to import it every time manually when it's auto renewed (I suggest you can do such a test in your lab, check the one cert in NTDS\Personal on DC will be installed after it is auto renewed).  

If I deleted the NAS certificate, and import it back again later on, will the auto-enrolment procedure will be broken?  

A: Auto-enrolment procedure will be not broken.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-09*

Hi Daisy,

Thank you so much for your detailed reply. Let me answer your question one by one.

-  I am talking about the domain controllers as our ldap server and to be honest with you, I do not know where our NAS and IAS servers are and if they are still in use. However, from my previous colleagues notes, the NAS/IAS cert is using for NPS radius authentication and NPS is running on domain controllers

-  yes, Both Kerberos Cert and NAS cert are installed on all domain controllers and in the same local computer/personal store

-  No, we did not install the kerberos certificate into NTDS/personal on the domain controller. The kerberos cert is configured with auto renew and auto enroll every 2 years. I saw from the documentations, the cert in NTDS/PERSONAL store won't be auto renewed, so I will need to import it every 2 years, is it correct?

If I import the kerberos cert to NTDS/personal, will the auto-renewal and auto enrolment still work and i need to import it every time when it's auto renewed? Can I automate this?

-  yes, NAS cert is installed on all domain controllers local computer\personal store

-  No, they use different template Kerberos using the Kerberos template and the NAS cert using the NAS/IAS template

-  the Key usage is different, but they have same ones overlapped, please see below:

the Kerberos cert has the following key usage

for RAS/IAS server one is below

If this one is used for NPS radius, i cannot remove it if there is an issue, everyone will be affected.

If I deleted the NAS certificate, and import it back again later on, will the auto-enrolment procedure will be broken?

Here is the certificates on one of our Domain controllers:

Now in term of the server authentication, the one used for NPS Radius is pushed our for LDAPS.

Thank you again.

Hello Gina Qu,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description, do you mean "local ldap server" is also Domain Controller and NAS server?  

2.Do you install the Kerberos Certificate and NAS certificate on the same server (Domain Controller and NAS server)?  

3.Do you install Kerberos certificate into NTDS/personal on the server?  

  

4.Do you install NAS certificate into Local Computer\Personal on the server?  

5.Please check if the two certificate has the same certificate template.

6.Please check if the Key Usage are the same on both two certificates.

You can back up\export the NAS certificate on other location and delete it on Local Computer\Personal on the server and check if there is any issue during the working day. If there is any issue related to the NAS certificate, you can import this certificate again into Local Computer\Personal on the server.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

Hi @Daisy

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-08*

Hello Gina Qu,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description, do you mean "local ldap server" is also Domain Controller and NAS server?  

2.Do you install the Kerberos Certificate and NAS certificate on the same server (Domain Controller and NAS server)?  

3.Do you install Kerberos certificate into NTDS/personal on the server?  

  

4.Do you install NAS certificate into Local Computer\Personal on the server?  

5.Please check if the two certificate has the same certificate template.

6.Please check if the Key Usage are the same on both two certificates.

You can back up\export the NAS certificate on other location and delete it on Local Computer\Personal on the server and check if there is any issue during the working day. If there is any issue related to the NAS certificate, you can import this certificate again into Local Computer\Personal on the server.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
