---
title: "Progress Types"
type: reference
domain: sccm
slug: develop-progress-types
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/progress-types
family: develop
documentKind: "reference"
abstract: "Progress states for a download. For a non-status change (for example, if there was just transfer of bytes), specify NULL for progress type."
---

# Progress Types

# Progress Types
Progress states for a download.

> [!NOTE]
>  For a non-status change (for example, if there was just transfer of bytes), specify NULL for progress type.

## Syntax

```
//  Progress types:
//******************************************************************************
static const WCHAR S_DTS_PROGRESS_DOWNLOADING_MANIFEST[]    = L"DownloadingManifest";
static const WCHAR S_DTS_PROGRESS_PROCESSING_MANIFEST[]     = L"ProcessingManifest";
static const WCHAR S_DTS_PROGRESS_CREATING_DIRECTORIES[]    = L"CreatingDirectories";
static const WCHAR S_DTS_PROGRESS_PREPARING_DOWNLOAD[]      = L"PreparingDownload";
static const WCHAR S_DTS_PROGRESS_DOWNLOADING_DATA[]        = L"DownloadingData";

```

## Types

|Progress type|Description|
|-|-|
|S_DTS_PROGRESS_DOWNLOADING_MANIFEST|Determining list of files to download.|
|S_DTS_PROGRESS_PROCESSING_MANIFEST|Processing list of files.|
|S_DTS_PROGRESS_CREATING_DIRECTORIES|Creating subdirectories based on list of files.|
|S_DTS_PROGRESS_PREPARING_DOWNLOAD|Manifest processing complete, starting download.|
|S_DTS_PROGRESS_DOWNLOADING_DATA|Downloading files.|

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).
