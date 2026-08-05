---
title: "Active Directory에 가입된 Windows 11을 사용중인 유저가 선택적 기능을 설치하려고 할 때 발생하는 오류에 대한 그룹 정책 문의"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1368819/active-directory-windows-11
question_id: 1368819
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Active Directory에 가입된 Windows 11을 사용중인 유저가 선택적 기능을 설치하려고 할 때 발생하는 오류에 대한 그룹 정책 문의

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1368819/active-directory-windows-11 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
안녕하세요.

저희는 사내에서 Active Diretory를 사용하여 사용자들을 관리하고 있습니다.

대부분의 사용자는 Windows 10 또는 11 버전을 사용하고 있고, Windows의 선택적 기능 (Rsat 또는 OpenSSH 등의 선택적 기능)을 설치하려고 할 때 관리자에게 문의하라고 하거나, 이유를 알 수 없이 실패한다고 알려줍니다.

이와 관련하여 구글에 흔히 제안하고 있는 방법들은 당장의 해결책이 될 수는 있지만, 근본적인 원인을 찾을 수는 없습니다. 제가 시도해 본 방법은 아래와 같습니다.

1. 레지스트리에서 WSUS AU의 DWORD 값을 변경하고, update services를 재시작

   => 이 방법은 DWORD 값을 변경하여 Windows 관련 업데이트를 모두 거부하는 것이 되므로 원하지 않습니다. 원하는 선택적 기능을 설치한 뒤에는 다시 DWORD 값을 복구 해 주어야 하는 번거로운 작업이 반복됩니다.

   => 다음번 선택적 기능을 추가할 때에도 또다시 위 방법을 반복해야만 합니다.

2. sfc 또는 dism을 통해 손상된 파일을 검사하고 복구합니다.

   => 당연히 문제가 없고, 복구 될 것도 없었습니다. 근본적인 해결이 되지 않습니다.

3. Active Directory에서 GPO를 확인 해 보았지만, Windows Update & Windows Install 관련 정책은 설정되어있지 않습니다.

    => 관련 정책이 설정되어 있지 않은데도 문제는 이미 발생했고, 반복해서 발생하고 있습니다.

4. PowerShell을 통하여, 원하는 선택적 기능 설치를 사용할 때마다 자동으로 DWORD 레지스트리를 변경하고 업데이트를 정지, 시작시키는 스크립트를 배포 할 계획을 가지고 있지만, 이것 또한 설치할 때마다 실행시켜주어야 하는 상황으로, 원하지 않습니다.

이와 관련하여, AD 서버의 그룹 정책 또는 근본적인 원인을 해결하기 위해 어떤 시도를 해야하는지 알려주시면 감사하겠습니다.

추가적으로, Active Directory의 GPO에서 모든 설정이 Not Configured 상태이면 기본적으로 allow가 아닌 deny되는 항목도 있는지 알려주세요.
```

## Answers

_No answers on this thread._
