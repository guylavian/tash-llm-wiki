---
title: "ADsOpenObject() has failed with LDAP error 0x8007200f (- 2147016689) The directory service is unavailable"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1509297/adsopenobject-has-failed-with-ldap-error-0x8007200
question_id: 1509297
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADsOpenObject() has failed with LDAP error 0x8007200f (- 2147016689) The directory service is unavailable

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1509297/adsopenobject-has-failed-with-ldap-error-0x8007200 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings!
When I call ADsOpenObject(LdapPath, userName, password, dwReserved, IID_IADs, (void**)&pObject); it is failed with "0x8007200f", whereas the LdapPath is like
LDAP://<Server Address>/DC=AD_domain,DC=com.
Please refer to the code snippet below, thanks!

```
IADs *pObject = NULL;
HRESULT hr = CoInitialize(NULL);
if ( FAILED(hr) )
{
    return hr;
}

DWORD dwReserved = ADS_SECURE_AUTHENTICATION; //ADS_SECURE_AUTHENTICATION = 1

hr = ADsOpenObject(LdapPath, //LdapPath=LDAP:///DC=AD_domain,DC=com
	userName,
	password,
	dwReserved,
	IID_IADs,
	(void**)&pObject); //Here it is failed with 0x8007200f.

if (FAILED(hr))	
{
	if(LdapPath!=NULL)
		delete[] LdapPath;
	CoUninitialize();
	return hr;
}
else
{
	. . .
}
```

## Answers

_No answers on this thread._
