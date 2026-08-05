---
title: "Get active directory picture using c++ code"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1017018/get-active-directory-picture-using-c-code
question_id: 1017018
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-cpp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Get active directory picture using c++ code

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1017018/get-active-directory-picture-using-c-code (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working on a java web application with active directory using JNI interface. i want to get the active directory users picture and found that the picture is stored as a octet string . I used IADsUser to get the value of the picture but i cant find any documentation or code how to use that value. I want to send this data through jni to java where i can render the picture. Code i used to get the picture.    

`    HRESULT GetUserObject()     {         IADsUser* pUser;       CoInitialize(NULL);       CComBSTR  path = L"LDAP://WIN-F94H2MP3UJR.Test.local/CN=Arun";       path += L",CN=Users,DC=Test,DC=local";       HRESULT hr = ADsOpenObject(path, L"Administrator", L"Arun@12",           ADS_SECURE_AUTHENTICATION, // For secure authentication           IID_IADsUser,           (void**)&pUser);       if (FAILED(hr)) { return NULL; }       VARIANT var;       hr = pUser->get_Picture((VARIANT*)&var);       std::string message = std::system_category().message(hr);       std::cout << message << std::endl;       return hr;   }    `    

Microsoft documentation i used to code this Link. In this documentation they specified Get picture method which is what am looking for. Here as the hr prints operation completed successfully . Help me how to work with this value or atleast help me to print the value stored in var in c++. Thank you.

## Answers

_No answers on this thread._
