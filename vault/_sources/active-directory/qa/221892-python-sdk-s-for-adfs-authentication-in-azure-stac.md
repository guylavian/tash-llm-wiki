---
title: "Python SDK’s for ADFS authentication in Azure stack."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/221892/python-sdk-s-for-adfs-authentication-in-azure-stac
question_id: 221892
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Python SDK’s for ADFS authentication in Azure stack.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/221892/python-sdk-s-for-adfs-authentication-in-azure-stac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Are there any python SDK’s available for Azure stack authentication using ADFS (Active Directory Federation Services)?

For authentication using Azure Active Directory (AAD) we use ServicePrincipalCredentials from azure.common.credentials to get the credentials object by providing the Client ID and Client secret and then pass this credentials object to ResourceManagementClient, StorageManagementClient, ComputeManagementClient, NetworkManagementClient, ManagementLockClient :  

self.resourceclient = ResourceManagementClient(credentials,  

subscriptionid,  

base_url=cloud_base_url,  

profile=profile)  

self.storageclient = StorageManagementClient(credentials,  

subscriptionid,  

base_url=cloud_base_url,  

profile=profile)  

self.computeclient = ComputeManagementClient(credentials,  

subscriptionid,  

base_url=cloud_base_url,  

profile=profile)  

self.networkclient = NetworkManagementClient(credentials,  

subscriptionid,  

base_url=cloud_base_url,  

profile=profile)  

self.lockclient = ManagementLockClient(credentials, subscriptionid,  

base_url=cloud_base_url,  

profile=profile)

Is there a way to authenticate using ADFS authentication?

Thanks and Regards,  

Rasika.

## Answers

_No answers on this thread._
