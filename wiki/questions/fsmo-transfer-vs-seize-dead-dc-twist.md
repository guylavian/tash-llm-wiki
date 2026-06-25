---
title: "FSMO Transfer vs Seize — DC1 מת, איך להחזיר תפקוד, ומתי אפשר להחזיר את המת לחיים"
type: question
domain: active-directory
slug: fsmo-transfer-vs-seize-dead-dc-twist
summary: "ניתוח ארבע-חלקי של FSMO transfer מול seize: ההבחנה המהותית, הסכנה בהחזרת DC מת, דחיפות שחזור תפקידים, והטוויסט — מתי דווקא אפשר להחזיר DC אחרי העברת תפקיד"
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - note:_sources/active-directory/ad-forest-recovery.md
  - note:_sources/active-directory/ad-metadata-cleanup.md
  - note:_sources/active-directory/rid-issuance-management.md
  - ref:reference/active-directory/ad-ds-understand-fsmo-roles.md
  - ref:reference/active-directory/ad-ds-ad-forest-recovery-seizing-operations-master-role.md
  - ref:reference/active-directory/ad-ds-ad-forest-recovery-perform-initial-recovery.md
  - ref:reference/active-directory/ad-ds-ad-forest-recovery-cleanup.md
provenance_extracted: 14
provenance_inferred: 3
provenance_ambiguous: 0
status: reviewed
updated: 2026-06-18
---

# FSMO Transfer vs Seize — DC1 מת, איך להחזיר תפקוד, ומתי אפשר להחזיר את המת לחיים

> תרחיש: DC1 (מחזיק את כל 5 תפקידי FSMO) קורס — דיסק מת, לא חוזר. DC2 חי, אבל לא מחזיק באף תפקיד.

---

## שאלה 1: Transfer מול Seize — למה ההבחנה מהותית?

### ההגדרה

| פעולה | תיאור | דרישה |
|-------|-------|-------|
| **Transfer** (העברה) | העברה **מתואמת** של תפקיד מ-DC מקור ל-DC יעד. המקור מודיע על העברת הבעלות, משחרר את התפקיד, והיעד מאשר קבלה. | **DC המקור חייב להיות Online** — הוא שותף פעיל בתהליך |
| **Seize** (תפיסה) | **לקיחה כפויה** של תפקיד מ-DC שאינו זמין. ה-DC היעד פשוט מכריז שהוא מחזיק בתפקיד, בלי אישור מהמקור. | DC המקור **מת/לא זמין** — לוקחים בכוח |

### למה Transfer בתרחיש הזה יכשל?

DC1 מת (דיסק נמחק). Transfer הוא **פרוטוקול דו-כיווני**:

1. ה-DC היעד (DC2) פונה אל DC1 (המקור) — מבקש להעביר
2. DC1 צריך לענות, לאשר, לסנכרן שינויים אחרונים, ולשחרר את התפקיד
3. אם DC1 לא זמין — הבקשה **מתייבשת ב-timeout**

התוצאה: `Move-ADDirectoryServerOperationMasterRole` (בלי `-Force`) ייכשל בהודעת שגיאה שה-FSMO holder לא ניתן להשגה.

### מה קורה בפועל?

```powershell
# יכשל — DC1 מת, לא עונה
Move-ADDirectoryServerOperationMasterRole -Identity DC2 -OperationMasterRole PDCEmulator
# Error: The FSMO operation failed. The current FSMO holder could not be contacted.

# יצליח — לוקח בכוח
Move-ADDirectoryServerOperationMasterRole -Identity DC2 -OperationMasterRole PDCEmulator -Force
# או: ntdsutil -> roles -> seize PDC
```

> **ההבחנה המהותית:** Transfer מניח **שיתוף פעולה** בין ה-DCs. Seize מניח **מוות** של המקור. בתרחיש שלנו (DC1 מת) — Transfer לא רלוונטי, Seize הוא המסלול היחיד.

---

## שאלה 2: למה DC1 לעולם לא חוזר אחרי Seize — ומי התפקידים המסוכנים ביותר?

### הכלל המוחלט

אחרי **seize** של תפקיד מ-DC שמת, ה-DC ההוא **לעולם לא יחזור לרשת**. לא באותו שם, לא אחרי תיקון הדיסק, לא כלום. למה?

**כי DC1 עדיין "חושב" שהוא מחזיק בתפקיד.** התהליך:

1. DC2 תפס (seize) את תפקיד PDC Emulator מ-DC1
2. ה-`fsmoRoleOwner` attribute ב-AD מתעדכן ← DC2 הוא הבעלים החדש
3. DC1 **לא יודע** על זה — הדיסק שלו מת, הוא החמיץ את השינוי
4. אם DC1 חוזר לרשת (דיסק משוחזר, VM משוחזרת מסנאפשט) — הוא ינסה **להפעיל את התפקיד** במקביל ל-DC2

### RID Master — הסכנה הגדולה ביותר

ה-RID Master מנפיק **מאגרי RID** (Relative IDs) ל-DCs. כל אובייקט ב-AD מקבל SID שהוא `<domain SID>-<RID>`. אם DC1 חוזר אחרי seize:

1. DC1 חושב שהוא עדיין RID Master
2. DC1 מנפיק RID pools ל-DCs אחרים
3. DC2 (הבעלים החוקי) מנפיק RID pools שונים
4. **שני DCs מנפיקים RID pools חופפים ← duplicate SIDs**
5. אסון: משתמשים/קבוצות/מחשבים שונים מקבלים אותו SID ← הרשאות מתערבבות, חשבונות נשברים

ה-RID Master (ו-Schema Master) מסוכנים כי **יש להם state**:

- RID Master: מנהל global RID pool — מצב שצריך להיות ייחודי
- Schema Master: מנהל את schema — שינוי schema מ-DC חוקי ומזויף יכול לקרוס את כל ה-forest
- Domain Naming Master: דומה — יכול להוסיף domains/re-naming במקביל

### Schema Master — הסכנה במקבילה

אם DC1 ו-DC2 טוענים שניהם ל-Schema Master:

- Schema update מ-DC2 מתבצע
- DC1 מתעורר, "מחזיר לעצמו" את השליטה
- DC1 עלול לשנות schema בצורה מנוגדת
- או גרוע מכך: להחיל schema update עם version mismatch → forest corruption

### RID vs Schema — מי יותר מסוכן?

| תפקיד | הסכנה בהחזרת DC מת |
|-------|-------------------|
| **RID Master** | **המסוכן ביותר** — duplicate SIDs. נזק לטווח קצר מיידי (סתירות זהות). לרוב לא הפיך בלי forest recovery. |
| **Schema Master** | מסוכן — schema corruption. אבל לרוב דורש פעולה יזומה (schema update) כדי לגרום נזק. |
| **Domain Naming Master** | מסוכן — split-brain על מבנה ה-forest. אבל פעולה נדירה. |
| **PDC Emulator** | פחות מסוכן — password/lockout יגיבו לא עקבי. אבל זמני, לרוב לא הרסני (הכיוון הזמני מתקן את עצמו עם replication). |
| **Infrastructure Master** | הכי פחות מסוכן — phantom records לא מעודכנים. נזק איטי, קל לזיהוי. |

---

## שאלה 3: איזה תפקיד דחוף לשחזור מיידי ואיזה יכול לחכות?

### טבלת דחיפות

| תפקיד | דחיפות | למה? |
|-------|--------|------|
| **PDC Emulator** | 🔴 **מידי** — שבירת התחברויות | זמן ה-domain (W32Time) נקבע ע"י PDC Emulator. בלי PDC Emulator, ל-DCs אחרים אין מקור זמן אמין → **שעון סוטה ב-5+ דקות → Kerberos נשבר (`KRB_AP_ERR_SKEW`)**. בנוסף: password changes לא מעובדים בעדיפות, account lockouts לא עקביים, GPO edits (GPMC) עלולים להיכשל. **בימים הראשונים זה ישבור login.** |
| **RID Master** | 🟠 **גבוהה** — שבירת יצירת אובייקטים | DCs מחזיקים RID pool ל-500 אובייקטים כברירת מחדל. אם ה-pools קיימים → יום-יומיים של עבודה רגילה. אבל ברגע ש-DC מאתחל או שה-pool שלו נגמר → "המערכת לא יכולה ליצור את האובייקט כי Directory Service לא הצליחה להקצות RID". **זה ישבור provisioning של משתמשים/מחשבים/קבוצות.** |
| **Infrastructure Master** | 🟢 **נמוכה** — כמעט לא מורגש | Cross-domain reference updates מתעכבות. SID-to-name translations עלולים להראות "S-1-5-..." במקום שמות. באף אחד לא שם לב שבוע-שבועיים. **אם Recycle Bin מופעל (DFL 2008R2+), התפקיד הזה לא נדרש כלל** — כל DC מטפל בעצמו. |
| **Domain Naming Master** | 🟢 **נמוכה** — לא מורגש עד לפעולה נדירה | צריך רק כשמוסיפים domain חדש או application partition. אם לא מתכננים להרחיב את ה-forest — לא מורגש. |
| **Schema Master** | 🟢 **נמוכה** — לא מורגש עד לפעולה נדירה | צריך רק כשמריצים `adprep /forestprep`, מתקינים Exchange, או מוסיפים schema extensions. **שבועות/חודשים יכולים לעבור בלי שחסר.** |

### סדר הפעולות המומלץ

```
שעה 0: PDC Emulator ← seize (Kerberos תלוי בזה)
שעה 1: RID Master ← seize (אם ה-pools אוזלים)
שעה 2: Infrastructure Master ← seize (אם Recycle Bin OFF)
שבועות: Domain Naming + Schema ← מתי שנוח
```

---

## טוויסט-על: מתי הכלל "אל תחזיר את ה-DC שתפסת ממנו" דווקא **לא** חל?

### התשובה: אחרי **Transfer** (לא Seize)

הכלל "לעולם אל תחזיר" הוא מוחלט ל-**seize**. אבל אחרי **transfer** — ההפך הוא הנכון: **אתה יכול, ואפילו צריך, להחזיר את ה-DC המקורי לרשת.**

### למה ההבדל?

| שלב | Transfer | Seize |
|-----|----------|-------|
| DC1 יודע שאיבד את התפקיד? | ✅ **כן** — הוא שיתף פעולה, אישר, שחרר. ה-attribute `fsmoRoleOwner` מתעדכן ב-DC1 עצמו. | ❌ **לא** — הוא מת בזמן ה-seize. עדיין חושב שהוא הבעלים. |
| DC1 חוזר לרשת → מה קורה? | DC1 יודע ש-DC2 הוא הבעלים החדש. לא מנסה להפעיל את התפקיד. **לא נוצר split-brain.** | DC1 חושב שהוא עדיין הבעלים. מנסה להפעיל במקביל ל-DC2. **split-brain.** |
| Metadata cleanup נדרש? | לא — transfer עושה cleanup אוטומטי. | ✅ **כן** — metadata cleanup של DC1 חייב להתבצע. |
| מה צריך לעשות לפני שמחזירים? | כלום מיוחד. DC1 יכול לחזור מיד. | **לעולם לא להחזיר.** גרוטאות. |

### דוגמה קלאסית: PDC Emulator במהלך upgrade

תרחיש שבו transfer + חזרה הם **נוהג תקין**:

1. אתה מרים DC3 עם Windows Server 2025 (חדש)
2. מעביר (transfer) את PDC Emulator מ-DC1 ל-DC3
3. DC1 יודע שהוא איבד את התפקיד — הוא כבר לא PDC Emulator
4. אתה עושה upgrade ל-DC1 (למשל: Windows Server 2022 → 2025)
5. מחזיר (transfer) את PDC Emulator מ-DC3 ל-DC1 (או משאיר על DC3)
6. **הכל תקין** — DC1 חזר לרשת, בלי split-brain, בלי בעיות

> **ההבדל המהותי:** Transfer משאיר את DC1 במצב עקבי — הוא יודע שהוא כבר לא הבעלים. Seize משאיר את DC1 לא מודע — הוא "מאמין" שהוא עדיין הבעלים, וכשיחזור ינסה להפעיל את התפקיד.

### מה אם בכל זאת רוצים להחזיר DC אחרי seize?

זה אפשרי, אבל **רק אחרי metadata cleanup + reformat + re-promote**:

1. להריץ **metadata cleanup** (ntdsutil) שמסיר את ה-DC object של DC1 מה-AD ← ה-DC1 הישן נמחק מהמסד
2. **לפרמט** את הדיסק של DC1 לחלוטין
3. להתקין מחדש Windows Server
4. לקדם (promote) כ-DC חדש עם **שם חדש** (או אפילו שם חדש)

> 🚫 **מה אסור:** להחזיר את DC1 עם ה-NTDS.DIT הישן שלו. זה יביא איתו את ה-InvocationID הישן, ה-RID pool הישן, והאמונה השגויה שהוא בעל התפקיד — מה שיגרום ל-USN rollback, duplicate SIDs, ו-split-brain.

---

## סיכום השוואתי

| מאפיין | Transfer | Seize |
|--------|----------|-------|
| DC1 חייב להיות זמין? | ✅ Required | ❌ Not required |
| DC1 יכול לחזור לרשת? | ✅ **כן** — רגיל, בלי חשש | ❌ **לעולם לא** (אלא אחרי reformat + re-promote) |
| Split-brain risk? | ❌ לא | ✅ **כן** — במיוחד RID/Schema |
| Ntdsutil syntax | `transfer <role>` | `seize <role>` |
| PowerShell | `Move-ADDirectoryServerOperationMasterRole` | `... -Force` |
| Use case | Planned maintenance, upgrades, load balancing | Disaster recovery, DC dead |

---

## References

### Ground truth (`note:` / `ref:`)
- **note:_sources/active-directory/fsmo-roles.md** — raw note: transfer vs seize definition, per-role descriptions
- **ref:reference/active-directory/ad-ds-understand-fsmo-roles.md** — FSMO role descriptions, placement guidelines
- **ref:reference/active-directory/ad-ds-ad-forest-recovery-seizing-operations-master-role.md** — explicit seize procedure with ntdsutil, including the RID master synchronization caveat and the "click Yes to confirm" dialog
- **ref:reference/active-directory/ad-ds-ad-forest-recovery-perform-initial-recovery.md** — forest recovery: seize all roles onto restored DC, the "never bring back" rule
- **ref:reference/active-directory/ad-ds-ad-forest-recovery-cleanup.md** — transfer roles as part of cleanup after restore
- **ref:reference/active-directory/ad-ds-managing-rid-issuance.md** — RID pool management, duplicate SID risk

### Wiki (`[[slug]]` pages)
- [[fsmo-roles]] — the five roles, transfer vs seize basics
- [[ad-forest-recovery]] — full disaster recovery procedure
- [[ad-metadata-cleanup]] — cleaning orphaned DC metadata after forced removal
- [[rid-issuance-management]] — RID pool and duplicate SID risk
- [[active-directory-overview]] — AD DS orientation

### Upstream (`web:`)
- web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide (AD Forest Recovery Guide, fetched 2026-06-18)
- web:https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-operation-master-roles-in-ad-ds (Transfer or Seize FSMO roles, fetched 2026-06-18)
- web:https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc816779(v=ws.10) (Seize Operations Master Role, fetched 2026-06-18)
