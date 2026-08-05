---
title: "how to decrpyt windows laps encryted password using c++ using ADSI services(crypt32.lib)?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1403815/how-to-decrpyt-windows-laps-encryted-password-usin
question_id: 1403815
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other", "windows-development-api-win32"]
---
# how to decrpyt windows laps encryted password using c++ using ADSI services(crypt32.lib)?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1403815/how-to-decrpyt-windows-laps-encryted-password-usin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
while ((hr = pDirSearch->GetNextRow(hSearch2)) == S_OK)
		{
			ADS_SEARCH_COLUMN controlCol;
			hr = pDirSearch->GetColumn(hSearch2, L"msLAPS-EncryptedPassword", &controlCol);
			if (controlCol.dwNumValues > 0)
			{
				for (DWORD i = 0; i I am trying to decrypt "msLAPS-EncryptedPassword" attribute using c++(CryptUnprotectData method),But cant able to decrypt is there any procedure to follow to decrypt laps password.  

It throws ""error 13 .Data is invalid" Did I miss something?

## Answers

_No answers on this thread._
