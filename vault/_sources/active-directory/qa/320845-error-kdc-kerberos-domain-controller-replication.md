---
title: "Error KDC Kerberos domain controller replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320845/error-kdc-kerberos-domain-controller-replication
question_id: 320845
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error KDC Kerberos domain controller replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320845/error-kdc-kerberos-domain-controller-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i'm facing issue while launch command repadmin /syncall, the 2 DC's report the following error:  

CALLBACK MESSAGE: Error issuing replication: -2146892990 (0x80090342): The encryption type requested is not supported by the KDC.  

I've already tried to restart Kerberos Key Distribution Center service Modify Local Policies - Network security: Configure encryption types allowed for Kerberos with RD4_HMAC_MD5 - AES128_HMAC_SHA1 - AES256_HMAC_SHA1 - Future encryption types  

for all the DC's and also tried forcing it via GPO.  

Tried to enable support Kerberos encryption 128bit and 256bit on the users account  

Of course restarting the 2 DC's  

Bust no one of the listed operations solved my issue. Can you please help me with this? i finished the reasearches in Google for this issue.... Thanks a lot in advance M.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-19*

Hi,  

Following method for your reference:  

Stop the KDC service on the destination domain controller. To do it, run the following command at a command prompt:  

net stop KDC  

Start replication on the destination domain controller from the source domain controller. Use AD Sites and Services or Repadmin.  

Repadmin replicate destinationDC sourceDC DN_of_Domain_NC  

For example, if replication is failing on ContosoDC2.contoso.com, run the following command on ContosoDC1.contoso.com:  

Repadmin replicate ContosoDC2.contoso.com ContosoDC1.contoso.com "DC=contoso,DC=com"  

Start the Kerberos KDC service on the destination domain controller by running the following command:  

net start KDC  

2,If it can't solve the issue, try to :  

Reset the computer account password of the source domain controller.  

3,If still can't solve the issue, try to use the tool :Network Monitor to check more error details when sync the replication.  

Best Regards,
