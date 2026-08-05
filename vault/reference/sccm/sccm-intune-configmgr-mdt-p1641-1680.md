---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1641-1680"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1641-1680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1641-1680
family: sccm
documentKind: "doc"
abstract: "SetPageInfo C++ HRESULT SetPageInfo(ISettingsProperties *pPageInfo) This method is called internally, and you should not call it yourself. It provides the page's XML to the form controller. Validate C++ HRESULT Validate(void) This method executes all the validators attached to c"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1641-1680

<!-- p.1641 -->

SetPageInfo

  C++

  HRESULT SetPageInfo(ISettingsProperties *pPageInfo)

This method is called internally, and you should not call it yourself. It provides the
page's XML to the form controller.

Validate

  C++

  HRESULT Validate(void)

This method executes all the validators attached to controls. If a validator does not pass,
the form controller displays a warning message and disables the Next button, then
stops processing validators. Typically, you only need to call this method at the end of
your OnWindowCreated method; it always returns S_OK.

AddToGroup

  C++

  AddToGroup(int groupControlId, int controlId)

This method adds a control as a "child" of a check box or radio button, as shown in
Table 30. All such child controls will be disabled when the parent control is not selected.
The method always returns S_OK.

Table 30. AddToGroup

                                                                                 ﾉ   Expand table

 Parameter        Description

 groupControlId   The ID of the check box or radio button that will control the enable state of the
                  child control

 Controlld        The ID of the control that you want to add as a child

UpdateCheckGroup

<!-- p.1642 -->

  C++

  HRESULT UpdateCheckGroup(int groupControlId)

This method updates the enable or disable status of a group's child controls based on
the status of the parent control. Generally, you do not need to call this method yourself,
because the form controller calls it for you.

AddValidator

  C++

  HRESULT AddValidator(int controlId, IValidator *pValidator, IControl
  *pControl = 0)

Call this method only if you have a validator you want to create in code instead of with
the XML. This method always returns S_OK.

AddValidator

  C++

  HRESULT AddValidator(int controlId, LPCWSTR validatorId, LPCWSTR message,
  IValidator **ppValidator = nullptr)

Call this method only if you have a validator you want to create in code instead of with
the XML.

DisableValidation

  C++

  HRESULT DisableValidation(int controlId, BOOL disable)

Call this method to either explicitly disable validator for a control or restore normal
validation, as shown in Table 31. This method is useful, for example, when you have
enable/disable rules for controls that are not covered with form validation and you need
to disable validation for a control. In other words, you would not normally call this
method. This method always returns S_OK.

Table 31. HRESULT DisableValidation

<!-- p.1643 -->

                                                                                    ﾉ   Expand table

 Parameter      Description

 controlId      The control for which you want to enable or disable validation

 Disable        Set to TRUE to disable validation and to FALSE to restore normal validation

AddField

  C++

  HRESULT AddField(LPCWSTR fieldName, int controlId, BOOL suppressLog,
  DialogControlTypes type)

Add a control mapping between the name in a Field element of the .config XML file and
the control ID in your page's dialog box, as shown in Table 32. You must call this method
before the call to InitFields, because InitFields uses this information. This method always
returns S_OK.

Table 32. HRESULT AddField

                                                                                    ﾉ   Expand table

 Parameter      Description

 Fieldname      Name of the field as it appears in your page's XML

 controlId      The ID of the control in your page's dialog box template

 suppressLog    Set to TRUE if you do not want the values from this field written to the log file;
                always set this parameter to TRUE for password or PIN fields

 Type           The type of control, which is one of the following:

                - CONTROL_STATIC_TEXT
                - CONTROL_COMBO_BOX
                - CONTROL_LIST_VIEW
                - CONTROL_PROGRESS_BAR
                - CONTROL_GENERIC
                - CONTROL_RADIO_BUTTON
                - CONTROL_CHECK_BOX
                - CONTROL_TREE_VIEW

AddRadioGroup

<!-- p.1644 -->

  C++

  HRESULT AddRadioGroup(LPCWSTR groupName, int radioControlId)

This method adds a control to a named radio button group, as shown in Table 33. You
must call this before the InitFields method, because that method uses attributes on the
RadioGroup element to control settings for all the radio button controls in the group.
Radio groups can be locked, for example, so that all the radio buttons are disabled, but
child controls are enabled or disabled based only on which radio button is selected. This
method always returns S_OK.

Table 33. HRESULT AddRadioGroup

                                                                               ﾉ     Expand table

 Parameter           Description

 groupName           A string that defines a group of radio buttons on this page

 radioControlId      The ID of a single radio button to add to this group

EnableRadioGroup

  C++

  HRESULT EnableRadioGroup(LPCWSTR groupName, BOOL enable)

This method allows you to enable or disable an entire radio button group. Disabling a
radio group disables all the radio button controls in the group as well as any children of
those radio buttons that have been added with AddToGroup. See Table 34 and Table 35.

Table 34. EnableRadioGroup

                                                                               ﾉ     Expand table

 Parameter    Description

 groupName    Name of a radio button group that you defined already with a call to
              AddRadioGroup

 Enable       Set to TRUE to enable the radio button group and FALSE to disable the group

<!-- p.1645 -->

Table 35. HRESULT EnableRadioGroup

                                                                            ﾉ    Expand table

 HRESULT             Description

 S_OK                Group enabled or disabled

 E_INVALIDARG        There is no radio button group with the name you provided

InitFields

  C++

  HRESULT InitFields(IFieldCallback *pFieldCallback = nullptr)

Before calling this method, call AddField for each field that the XML can control. This
method always returns S_OK.

The pFieldCallback parameter is optional. If you provide it, the form controller calls
SetFieldDefault for controls that are not either CONTROL_STATIC_TEXT or
CONTROL_CHECK_BOX. This behavior allows you to retrieve a default value from the
XML and set it in the control yourself.

SaveFields

  C++

  HRESULT SaveFields(IFieldCallback *pFieldCallback = nullptr)

This method saves field values to task sequence variables and to the summary data that
will be shown on the Summary page. Providing a pointer in pFieldCallback allows you
to handle saving values for controls that do not support CONTROL_STATIC_TEXT.

IsFieldDisabled

  C++

  BOOL IsFieldDisabled(int controlId)

This method allows you to determine whether a field has been disabled in the XML.

<!-- p.1646 -->

InitSection

  C++

  HRESULT InitSection(LPCWSTR key, LPCWSTR sectionCaption)

This method initializes the summary data that will be shown on the Summary page, as
shown in Table 36. Call this method in your OnNextSelected method before calling
SaveFields. This method always returns S_OK.

Table 36. HRESULT InitSection

                                                                                 ﾉ    Expand table

 Parameter         Description

 Key               This parameter should be unique to your page. It is used to ensure that each
                   page has its own summary information.

 sectionCaption    The header that will be shown on the Summary page for this page's summary
                   information. Typically, you use DisplayName() as the value for this parameter.

AddSummaryItem

  C++

  HRESULT AddSummaryItem(LPCWSTR first, LPCWSTR second)

This method allows you to add summary items to the Summary page above and
beyond those items set with the XML. See Table 37.

Table 37. HRESULT AddSummaryItem

                                                                                 ﾉ    Expand table

 Parameter        Description

 First            The caption for the summary item, which is shown on the left side

 Second           The value that will be shown on the right side

SuppressLogValue

<!-- p.1647 -->

  C++

  HRESULT SuppressLogValue(LPCWSTR tsVariableName)

Call this method for task-sequence variables for which you do not want the values to be
written to the log file. Call this method for task sequence variables that store passwords,
PINs, or other sensitive values a user might enter.

SaveText

  C++

  HRESULT SaveText(int controlId, LPCWSTR tsVariableName, LPCWSTR
  summaryCaption)

This method saves the value of a text control to both a task sequence variable and the
summary section. Typically, you will not need to call this method yourself, because the
form controller does this for all fields. See Table 38.

Table 38. HRESULT SaveText

                                                                                ﾉ   Expand table

 Parameter          Description

 controlId          The ID of the text box that contains the value you want to save (or any other
                    control that can return text)

 tsVariableName     Name of the task sequence variable that you want to modify

 summaryCaption     The caption on the Summary page for this value

LoadText

  C++

  HRESULT LoadText(int controlId, LPCWSTR tsVariableName)

This method reads the value of a task sequence variable and sets the text box to this
value.

ControlEvent

<!-- p.1648 -->

  C++

  void ControlEvent(WORD eventId, WORD controlId)

Call this method on your OnControlEvent method to ensure that the form controller can
process control events, which it needs to do to function correctly. The values you pass to
this method are the same values passed to the OnControlEvent method.

IsValid

  C++

  BOOL IsValid(void)

This method returns the status of the most recent validation of the form. If any of the
control validators reported an error, this method returns FALSE. In other words, it returns
TRUE only if all the controls on the page are valid.

IValidator Interface

  C++

  __interface IValidator : IUnknown
  {
      HRESULT Init(IControl *pControl, LPCTSTR message);
      HRESULT Init(IControl *pControl, IWizardPageContainer *pContainer,
  IStringProperties *pProperties);
      BOOL, IsValid(LPBSTR pMessage);
      HRESULT SetProperty(int propertyId, LPVARIANT pValue);
      HRESULT SetProperty(int propertyId, IUnknown *pUnknown);
      HRESULT SetProperty)(int propertyId, LPCTSTR pValue);
  };

Overview

Validators are components that can validate a single control on your page. The easiest
way to implement a validator is to make it a subclass of the BaseValidator class, which is
defined in the BaseValidator.h header file.

HRESULT Init(IControl *pControl, LPCTSTR message)

If you create a validator in code, you can call this method to initialize the validator. See
Table 39.

<!-- p.1649 -->

Table 39. HRESULT Init

                                                                                  ﾉ     Expand table

 Parameter       Description

 pControl        The control that your validator must validate

 Message         The message to display on the page if the control is not valid

HRESULT Init(IControl *pControl, IWizardPageContainer
*pContainer, IStringProperties *pProperties)

The form controller calls this method to initialize validators that it creates based on the
page's XML. See Table 40.

Table 40. HRESULT Init Method

                                                                                  ﾉ     Expand table

 Parameter     Description

 pControl      The control that your validator must validate

 pContainer    In case your validator needs access to the logger or needs to create other
               components

 pProperties   Provides access to the properties (setter elements) for your validator

BOOL, IsValid(LPBSTR pMessage)

This method returns TRUE if the control is valid or FALSE if the control is invalid. On
return, pMessage should be filled in with a new BSTR that contains the message to
display when the control is not valid.

HRESULT SetProperty(int propertyId, LPVARIANT pValue)

You can implement this method if you need extra values that are not provided in the
XML.

HRESULT SetProperty(int propertyId, IUnknown *pUnknown)

<!-- p.1650 -->

You can implement this method if you need extra values that are not provided in the
XML.

HRESULT SetProperty)(int propertyId, LPCTSTR pValue)

You can implement this method if you need extra values that are not provided in the
XML.

IRegEx Interface

  C++

  __interface IRegEx : IUnknown
  {
      BOOL MatchesRegex(LPCTSTR input, LPCTSTR regex);
      HRESULT GetMatch(size_t index, LPBSTR pValue);
  };

This method is implemented by the ID_Regex component (IRegex.h) and provides
support for regular expression processing.

BOOL MatchesRegex(LPCTSTR input, LPCTSTR regex)

This method runs the regular expression against the input text. It uses the C++ standard
library's regex_match function to do the actual work. The method returns TRUE if there
were matches, FALSE otherwise.

HRESULT GetMatch(size_t index, LPBSTR pValue)

This method allows you to retrieve the matches from the most recent MatchesRegex
call. Note that there is no error processing in this method, and it either returns S_OK or
throws an exception.

ISummaryInfo Interface

  C++

  __interface ISummaryInfo : IUnknown
  {
      size_t Count(void);
      HRESULT Clear(void);
      HRESULT AddInfo(LPCTSTR pFirst, LPCTSTR pSecond);
      HRESULT GetInfo(size_t index, LPBSTR pFirst, LPBSTR pSecond);

<!-- p.1651 -->

        HRESULT GetCaption(LPBSTR pCaption);
        HRESULT SetCaption(LPCTSTR caption);
  };

You should not need to use this interface directly. Instead, use IFormController.

ISummaryBag

  C++

  __interface ISummaryBag : IUnknown
  {
      size_t Count(void);
      HRESULT GetInfoByIndex(size_t index, [out] ISummaryInfo **ppSummary);
      HRESULT GetInfoByKey(LPCTSTR key, [out] ISummaryInfo **ppSummary);
  };

You should not need to use this interface directly. Instead, use IFormController.

ITSVariableBag Interface

  C++

  __interface ITSVariableBag : IUnknown
  {
      void GetValue([in] LPCTSTR variableName, [out] LPBSTR pValue);
      void SetValue([in] LPCTSTR variableName, [in] LPCTSTR pValue);
      void Clear(void);
      HRESULT Remove([in] LPCTSTR variableName);
      HRESULT SuppressLogValue([in] LPCTSTR variableName);
      void Save(void);
  };

This interface provides access to task sequence variables. You can access this interface
using your page's TSVariables() method.

void GetValue([in] LPCTSTR variableName, [out] LPBSTR pValue)

This method reads the value of a task sequence variable.

  ７ Note

  Values are cached after the first read.

<!-- p.1652 -->

void SetValue([in] LPCTSTR variableName, [in] LPCTSTR pValue)

This method sets the value of a task sequence variable. This value is saved in memory.
Task sequence values are written once you select Finish in the UDI Wizard.

void Clear(void)

This method removes all task sequence values that have been saved in memory.

HRESULT Remove([in] LPCTSTR variableName)

This method removes a specific task sequence value from memory. The next time you
call GetValue with the same task sequence name, the method attempts to retrieve it
from the task sequence.

HRESULT SuppressLogValue([in] LPCTSTR variableName)

Whenever task sequence variables are written, such as when you select Finish in the UDI
Wizard, the names and values are written to the log file. Call this method to suppress
logging of sensitive values, such as passwords or PINs, for a specific task sequence
variable.

void Save(void)

This method saves all task sequence values that have been set with calls to SetValue.

ITSVariableRepository Interface

  C++

  __interface ITSVariableRepository : IUnknown
  {
      void GetValue([in] LPCTSTR variableName, BOOL logValue, [out] LPBSTR
  pValue);
      void SetValue([in] LPCTSTR variableName, BOOL logValue, [in] LPCTSTR
  value);
  };

This interface is for internal use by TSVariableBag for reading and writing task sequence
variables.

IWizardFinish Interface

<!-- p.1653 -->

  C++

  __interface IWizardFinish : IUnknown
  {
      HRESULT Canceled(void);
      HRESULT Finished(void);
  };

This interface is useful in advanced scenarios where you want to perform additional
processing when you select Finish or Cancel in the UDI Wizard. The UDI Wizard contains
a Finish task that saves task sequence variables when you select Finish. If you cancel the
wizard, the task only sets the OSDSetupWizCancelled task sequence variable to TRUE
and does not save changes to any other task sequence variables.

If you create your own finish component, you need to register it with code like this:

  C++

  Register<MyFinishTaskFactory>(ID_MyFinishTask, pRegistry);

  PWizardFinish pFinish;
  CreateInstance(pRegistry, ID_MyFinishTask, &pFinish);

  PWizardFinishService pService;
  GetService<IWizardFinishService>(pRegistry, &pService);

  pService->Register(pFinish);

IBindableList Interface

  C++

  __interface IBindableList : IUnknown
  {
      size_t Count(void);
      HRESULT GetCaption(size_t index, LPBSTR pCaption);
  };

Implement this interface if you have a data source component that you want to bind to
a combo box by calling its Bind method.

size_t Count(void)

This method returns the number of items in the list.

<!-- p.1654 -->

HRESULT GetCaption(size_t index, LPBSTR pCaption)

This method returns the caption of the item at a specific index.

IDataNodes Interface

  C++

  __interface IDataNodes : IUnknown
  {
      size_t Count();
      HRESULT SetCaptionProperty(LPCTSTR captionProperty);
      HRESULT GetProperty(size_t index, LPCTSTR propertyName, [out] LPBSTR
  propertyValue);
      HRESULT GetNode(size_t index, [out] ISettingsProperties **ppNode);
  };

This interface provides access to hierarchical data that can be saved in a page. You
obtain this interface via methods on the ISettingsProperties interface, which is available
to your page through the Settings method.

Data in a page's XML can look something like this

  XML

         <Data Name="Network">
           <DataItem>
             <Setter Property="DisplayName">Public</Setter>
             <Setter Property="Share">\\servername\Share</Setter>
           </DataItem>
           <DataItem>
             <Setter Property="DisplayName">Dev Team</Setter>
             <Setter Property="Share">\\servername\DevShare</Setter>
           </DataItem>
         </Data>

Calling Settings()->GetDataNode(L"Network", &pData) gives you an IDataNodes
instance with two data items (each of which in turn has two properties).

size_t Count()

This method returns the number of DataItem elements.

HRESULT SetCaptionProperty(LPCTSTR captionProperty)

<!-- p.1655 -->

The component that supports this interface also supports IBindableList, which makes it
easy to populate a combo box with data from the page's XML. This method controls
which property (setter) in each DataItem element will be used for this binding. For
example, you could call this method with DisplayName, and it would use that setter
property for data binding. The combo box would then contain Public and Dev Team as
items.

HRESULT GetProperty(size_t index, LPCTSTR propertyName, [out]
LPBSTR propertyValue)

This method gets a property from one of the DataItem elements. See Table 41 and Table
42.

Table 41. DataItem GetProperty

                                                                                ﾉ     Expand table

 Parameter       Description

 Index           The index value (starting with 0) of the DataItem for which you want to retrieve
                 a property value

 propertyName    Name of the setter property for which you want to retrieve a value

 propertyValue   On return, contains the string value of a property

Table 42. HRESULT GetProperty

                                                                                ﾉ     Expand table

 HRESULT                       Description

 S_OK                          The property was retrieved.

 E_INVALIDARG                  The index is past the end of the array.

HRESULT GetNode(size_t index, [out] ISettingsProperties
**ppNode)

This method is similar to GetProperty, but instead of returning one value from a
DataItem, it returns the entire DataItem wrapped in an ISettingsProperties interface.
See Table 43 and Table 44.

<!-- p.1656 -->

Table 43. HRESULT GetNode

                                                                                 ﾉ   Expand table

 Parameter   Description

 Index       The index value (starting with 0) of the DataItem for which you want to retrieve a
             property value

 ppNode      On exit, the ISettingsProperties interface that wraps the DataItem node

Table 44. HRESULT GetNode Results

                                                                                 ﾉ   Expand table

 HRESULT                       Description

 S_OK                          The node was retrieved.

 E_INVALIDARG                  The index is past the end of the array.

IFactoryRegistry Interface

  C++

  __interface IFactoryRegistry : IUnknown
  {
      void Register(LPCTSTR type, IClassFactory *pFactory);
      HRESULT LoadAndRegister(LPCTSTR dllName, ILogger *pLogger);
      BOOL Contains(LPCTSTR type);
      HRESULT GetFactory(LPCTSTR type, IClassFactory **ppFactory);
      HRESULT CreateInstance(LPCTSTR type, IUnknown **ppInstance);
      HRESULT SetContainer(IWizardPageContainer *pContainer);
      HRESULT RegisterService(REFGUID iid, IUnknown *pService);
      HRESULT GetService(REFGUID iid, IUnknown **ppService);
  };

Overview

When you create a new custom page, at a minimum you need to create a page factory—
a class that implements IClassFactory. (You can use ClassFactoryImpl as a base class for
your factory.)

void Register(LPCTSTR type, IClassFactory *pFactory)

<!-- p.1657 -->

This method registers a class factory with the registry. See Table 45.

Table 45. IClassFactory void Register

                                                                                   ﾉ    Expand table

 Parameter   Description

 Type        A string that identifies the factory you are registering; generally, this parameter
             should have your company name in the string to ensure that it is unique

 pFactory    A pointer to your class factory instance

HRESULT LoadAndRegister(LPCTSTR dllName, ILogger *pLogger)

This method is for internal use only.

BOOL Contains(LPCTSTR type)

This method is generally for internal use. It checks to see whether a class factory has
been registered for a type.

HRESULT GetFactory(LPCTSTR type, IClassFactory **ppFactory)

This method allows you to retrieve the class factory. Typically, you would call
CreateInstance. However, if you are going to create a large number of the same
component, it is more efficient to retrieve the factory, and then ask it to create the
instances for you.

HRESULT CreateInstance(LPCTSTR type, IUnknown **ppInstance)

This method creates a new instance of a component, given its type. Use the
CreateInstance template method instead, which allows type-safe object creation.

HRESULT SetContainer(IWizardPageContainer *pContainer)

This method is for internal use only.

HRESULT RegisterService(REFGUID iid, IUnknown *pService)

Services are single instances of a component that can be used in multiple places. You
can use this method to register a service on one page, and then retrieve that same

<!-- p.1658 -->

instance from another page.

HRESULT GetService(REFGUID iid, IUnknown **ppService)

This method retrieves a service that was previously registered with a call to
RegisterService.

HRESULT SetLanguage(LANGID languageId)

This method sets the language of the UDI Wizard to the language identifier you
provided in the languageId parameter.

LANGID GetLanguage()

This method returns the value of the language identifier you provided with the /locale
command-line parameter for the UDI Wizard. The method returns one of the following
values:

     Value of the language identifier provided with the /locale command-line
     parameter

     0, if you did not provide the /locale command-line parameter

ILogger Interface

  C++

  __interface ILogger : IUnknown
  {
      HRESULT Init(LPCWSTR logFilename);
      HRESULT MoveLog(LPCWSTR logFilename);
      HRESULT LogBase(EMessageType messageType, LPCTSTR component, SYSTEMTIME
  eventTime, LPCTSTR message);
      HRESULT Log(EMessageType messageType, LPCTSTR component, LPCTSTR
  message);
      HRESULT Error(HRESULT error, LPCTSTR component, LPCTSTR message);
      HRESULT Error2(HRESULT error, LPCTSTR component, LPCTSTR message,
  LPCTSTR message2);
      HRESULT Normal(LPCTSTR component, LPCTSTR message);
      HRESULT Normal2(LPCTSTR component, LPCTSTR message, LPCTSTR message2);
      HRESULT Verbose(LPCTSTR component, LPCTSTR message);
      HRESULT Verbose2(LPCTSTR component, LPCTSTR message, LPCTSTR message2);
      HRESULT Debug(LPCWSTR component, LPCWSTR message);
      HRESULT EnableDebug(BOOL debug);
      HRESULT Close(void);

<!-- p.1659 -->

        HRESULT GetLogFilename(LPBSTR pFilename);
  };

Overview

The UDI Wizard logs information to a log file, which helps troubleshoot issues found in
the field. It is a good idea for your pages to log information. You can obtain a pointer to
this interface from within your page using the page's Logger() method. Lines in the log
file contain a "level" number that represents error, normal, verbose, or debug messages.

  ７ Note

  Debug messages are not saved to the log file unless debug support is turned on.
  You can turn on debug support by adding the following line to the Style element in
  the .config file:

  XML

  <Setter Property="debug">true</Setter>

Init

  C++

  HRESULT Init(LPCWSTR logFilename)

This method is for internal use only.

MoveLog

  C++

  HRESULT MoveLog(LPCWSTR logFilename)

This method is for internal use only.

LogBase

  C++

<!-- p.1660 -->

  HRESULT LogBase(EMessageType messageType, LPCTSTR component, SYSTEMTIME
  eventTime, LPCTSTR message)

This method is for internal use only.

Log

  C++

  HRESULT Log(EMessageType messageType, LPCTSTR component, LPCTSTR message)

This method is for internal use only.

Error

  C++

  HRESULT Error(HRESULT error, LPCTSTR component, LPCTSTR message)

Call this method to log information about an error. See Table 46.

Table 46. HRESULT Error

                                                                                  ﾉ   Expand table

 Parameter    Description

 Error        The error code returned by a call (This code will be displayed in the log entry as a
              number.)

 Component    A string that identifies the source of the error, which is generally your page or the
              component that you have written

 Message      The message that explains what caused the error

Error2

  C++

  HRESULT Error2(HRESULT error, LPCTSTR component, LPCTSTR message, LPCTSTR
  message2)

<!-- p.1661 -->

This method is like the Error method but allows you to provide a two-part message. The
final message will have "message," and then "message2" in the output file. This is simply
a convenience method.

Normal

  C++

  HRESULT Normal(LPCTSTR component, LPCTSTR message)

This method logs a normal message. See the description of the Error method for
parameters.

Normal2

  C++

  HRESULT Normal2(LPCTSTR component, LPCTSTR message, LPCTSTR message2)

This method logs a normal message. See the description of the Error2 method for
parameters.

Verbose

  C++

  HRESULT Verbose(LPCTSTR component, LPCTSTR message)

This method logs a verbose message. See the description of the Error method for
parameters.

Verbose2

  C++

  HRESULT Verbose2(LPCTSTR component, LPCTSTR message, LPCTSTR message2)

This method logs a verbose message. See the description of the Error2 method for
parameters.

<!-- p.1662 -->

Debug

  C++

  HRESULT Debug(LPCWSTR component, LPCWSTR message)

This method logs a debug message. See the description of the Error method for
parameters. Debug messages are not saved to the file unless enabled. See the Overview
section for details.

EnableDebug

  C++

  HRESULT EnableDebug(BOOL debug)

This method is for internal use only.

Close

  C++

  HRESULT Close(void)

This method is for internal use only.

GetLogFilename

  C++

  HRESULT GetLogFilename(LPBSTR pFilename)

This method retrieves the name of the log file.

IOrientation Interface

  C++

  __interface IOrientation : IUnknown
  {
      void SetController(IWizardDialogController *pController);
      int AddPage(LPCTSTR name);

<!-- p.1663 -->

        void SelectPage(int index);
  };

This interface is for internal use only.

ISettings Interface

  C++

  __interface ISettings : IUnknown
  {
      int NumDlls();
      int NumPages();

        HRESULT SetStage(LPCWSTR stageName);
        HRESULT GetDllName(long index, __out LPBSTR pDllName);
        HRESULT GetPageInfo(long index, __out ISettingsProperties **ppPageInfo);
        HRESULT GetStyle(__out ISettingsProperties **ppStyleInfo);
  };

This interface is for internal use only.

ISettingsProperties Interface

  C++

  __interface ISettingsProperties : IUnknown
  {
      HRESULT GetAttribute(LPCTSTR attributeName, __out LPBSTR
  attributeValue);
      IStringProperties * Properties();
      HRESULT SelectNodes(LPCTSTR xPath, __out IXMLDOMNodeList **ppList);
      HRESULT SelectSingleNode(LPCTSTR xPath, __out IXMLDOMNode **ppNode);
      HRESULT GetDataNode(LPCTSTR name, __out ISettingsProperties **ppNode);
      HRESULT GetDataNodes(__out IDataNodes **ppNodes);
      HRESULT GetChildDataNodes(LPCTSTR childeName, __out IDataNodes
  **ppNodes);
  };

Overview

This interface provides access to page data. To get to the top level of page data, use the
page's Settings() method.

<!-- p.1664 -->

HRESULT GetAttribute(LPCTSTR attributeName, LPBSTR
attributeValue)

This method allows you to retrieve the values of attributes on the main node, which is
the Page node when you are using the Settings() method of the page.

IStringProperties * Properties()

This method provides access to the setter property values under the main node. For a
page, these are the top-level properties.

HRESULT SelectNodes(LPCTSTR xPath, IXMLDOMNodeList
**ppList)

Call this method if you want to directly get a list of XML nodes using an XPath
expression. It is better to use one of the other methods if you can. Use this method only
if you cannot get to nodes any other way.

HRESULT SelectSingleNode(LPCTSTR xPath, IXMLDOMNode
**ppNode)

Call this method if you want to directly get a single XML node using an XPath
expression. It is better to use one of the other methods if you can. Use this method only
if you can't get to a node any other way.

HRESULT GetDataNode(LPCTSTR name, ISettingsProperties
**ppNode)

Retrieve a Data element based on that element's Name attribute.

HRESULT GetDataNodes(IDataNodes **ppNodes)

This method retrieves a list of DataItem elements under the current node. From the
page level, call GetDataNode to retrieve an ISettingsProperty interface for the data.
Then, on that instance, call GetDataNodes to retrieve the list of records. For example,
given this XML:

  XML

        <Page ...>
          <Data Name="Network">
            <DataItem>
              <Setter Property="DisplayName">Public</Setter>

<!-- p.1665 -->

             <Setter Property="Share">\\servername\Share</Setter>
           </DataItem>
           <DataItem>
             <Setter Property="DisplayName">Dev Team</Setter>
             <Setter Property="Share">\\servername\DevShare</Setter>
           </DataItem>
         </Data>

  C++

  PSettingsProperties pData;
  Settings()->GetDataNode(L"Network", &pData);
  PDataNodes pNodes;
  pData->GetDataNodes(&pNodes);

HRESULT GetChildDataNodes(LPCTSTR childeName, IDataNodes
**ppNodes)

This method provides a quick way to get to the set of DataItem nodes under a specific
Data node. Using the XML from the GetDataNodes example, the following code does
exactly the same thing as the four lines of code in the example under GetDataNodes
but with error checking:

  C++

  ISimpleStringProperties Interface

ISimpleStringProperties Interface

  C++

  __interface ISimpleStringProperties : IStringProperties
  {
  void Add(LPCTSTR propertyName, LPCTSTR value);
  };

By itself, this interface may not be useful. However, it is implemented by the
ID_SimpleStringProperties component, which also implements the IStringProperties
interface. You can use this component in cases where you need to pass a set of
properties to another component, such as a task, but you want to add values
programmatically instead of using values from XML. Here is an example of how you
would use this interface:

<!-- p.1666 -->

  C++

  PSimpleStringProperties *pProperties;
  CreateInstance(Container(), ID_SimpleStringProperties, &pProperties);
  pProperties->Add(L"filename", L"%windir%\\system32\\cscript.exe");
  pTask->Init(pProperties, nullptr);
  IStringProperties
  __interface IStringProperties : IUnknown
  {
      HRESULT Get(LPCTSTR propertyName, [out] LPBSTR pPropValue);
  };

This interface provides simple access to a set of setter elements that come from XML.
This interface is available for the properties of a page using Settings()->Properties().

HRESULT Get(LPCTSTR propertyName, [out] LPBSTR pPropValue)

This method retrieves a single property value. See Table 47 and Table 48.

Table 47. IHRESULT Get Property Value

                                                                                   ﾉ    Expand table

 Parameter       Description

 propertyName    Name of the property that you want to read

 pPropValue      On exit, contains the property value as a string (This value will be nullptr if there
                 is no such property.)

Table 48. IHRESULT Get Property Value Results

                                                                                   ﾉ    Expand table

 HRESULT                 Description

 S_OK                    Property value is retrieved.

 E_INVALIDARG            There is no property with the name you provided.

ITaskManager Interface

  C++

<!-- p.1667 -->

  __interface ITaskManager : IUnknown
  {
      HRESULT Init(IWizardPageView *pPageView, int idListView, int idMessage,
  int idRetryButton, ISettingsProperties *pPageInfo, ITaskManagerCallback
  *pCallback);
      HRESULT SetFailMessage(LPCWSTR message);

       HRESULT Start(void);

       HRESULT GetTaskMessage(size_t index, LPBSTR message);
       HRESULT GetResultType)(size_t index, LPBSTR type);
       HRESULT GetProperty(size_t index, LPCTSTR propertyName, LPBSTR value);
       int GetSelectedIndex(void);
       HRESULT Wait(DWORD waitMilliseconds);
       size_t FailedCount(void);
       size_t WarningCount(void);
       size_t SucceedCount(void);
       size_t RunningCount(void);

       void OnCommonControlEvent(WORD controlId, LPNMHDR pInfo);
       void OnControlEvent(WORD eventId, WORD controlId);
       void EnableButtons(BOOL enable);
  }

This interface is implemented by the TaskManager component (ID_TaskManager in
ITaskManager.h), which is the component that runs tasks on the preflight page. You can
either use the preflight page directly, which is what you do most of the time, or build
your own page, letting this component do most of the work.

HRESULT Init(IWizardPageView *pPageView, int idListView, int
idMessage, int idRetryButton, ISettingsProperties *pPageInfo,
ITaskManagerCallback *pCallback)

You must call this method before calling any other method. It initializes the
TaskManager component. See Table 49.

Table 49. HRESULT Init

                                                                                   ﾉ   Expand table

 Parameter      Description

 pPageView      Provides access to the page that will be running tasks (This page must have a
                specific set of controls, which are outlined in the next few parameters.)

 idListView     The control ID of a ListView control that will display the list of tasks and the
                status of those tasks

<!-- p.1668 -->

 Parameter        Description

 idMessage        The control ID of a text box that will be used to display a message for the task
                  that you select

 idRetryButton    The control ID of a button you can select to run the tasks again

 pPageInfo        A wrapper around the page's XML (TaskManager loads the set of tasks to run
                  from this XML.)

 pCallback        Can be null (If this parameter is not null, TaskManager calls the Started method
                  when it starts a task and the Finished method for each task that finishes
                  running.)

HRESULT SetFailMessage(LPCWSTR message)

This method sets the message that will be displayed if one or more tasks fail.

HRESULT Start(void)

This method starts all the tasks. Each task is started on a separate thread.

HRESULT GetTaskMessage(size_t index, LPBSTR message)

This method is for internal use only. It retrieves the current message for a task based on
its index in the list of tasks.

HRESULT GetResultType)(size_t index, LPBSTR type)

This method retrieves the current "type" for a task. Table 50 shows the available types.

Table 50. HRESULT GetResultType

                                                                                     ﾉ   Expand table

 Type          Description

 0             Represents a task that succeeded

 1             Represents a tasks that returned a warning

 -1            Represents a failed task

<!-- p.1669 -->

The type is retrieved by looking at the task's exit or error code and finding a match in
the task's <ExitCodes> XML element.

HRESULT GetProperty(size_t index, LPCTSTR propertyName,
LPBSTR value)

This method is used by the progress and preflight pages to retrieve the BitmapFilename
setter property so it can display an image next to the message for the task that you
highlight. In other words, you can add a custom setter to the task's XML, and then
retrieve it with this method.

int GetSelectedIndex(void)

This method retrieves the index of the currently selected task, which is useful if you want
to retrieve additional information about the task (see GetProperty method) to display
for the selected task. The progress and preflight pages use this method to display an
image for the selected task.

HRESULT Wait(DWORD waitMilliseconds)

This method mainly helps with unit tests so the test can ensure that tasks finish before
the unit test exits. You would not normally call this method. It returns either when all
tasks finish running or the wait time has elapsed.

size_t FailedCount(void)

This method returns the number of tasks currently marked as failed.

size_t WarningCount(void)

This method returns the number of tasks currently marked as warning.

size_t SucceedCount(void)

This method returns the number of tasks currently marked as succeeded.

size_t RunningCount(void)

This method returns the number of tasks currently running.

<!-- p.1670 -->

void OnCommonControlEvent(WORD controlId, LPNMHDR pInfo)

Call this method from your page's OnCommonControlEvent so the TaskManager can
process events it needs.

void OnControlEvent(WORD eventId, WORD controlId)

Call this method from your page's OnControlEvent so the TaskManager can process
events it needs.

void EnableButtons(BOOL enable)

This method is for internal use only.

IWizardComponent Interface

  C++

  __interface IWizardComponent : IUnknown
  {
      HRESULT SetContainer(IWizardPageContainer *pContainer);
  };

Overview

Typically, you will not implement this interface directly but instead through the
WizardComponent template class. If your component implements this interface and you
have registered a class factory with the registry, your component receives a pointer to
the IWizardPageContainer instance when it is created. This helps you, for example,
access the Logger or the registry for creating other components that your component
might need.

IWizardDialogController Interface

  C++

  __interface IWizardDialogController : IUnknown
  {
      void Initialize(ISettings *pSettings);
      void InitPages(void);
      void Start();
      void Next();
      void Finish();

<!-- p.1671 -->

        void Previous();
        int NumPages();
        void Cancel();

        HRESULT Focus(WizardButtons button);
        HRESULT SetEnable(WizardButtons button, BOOL enable);
        void ShowWarningMessage(LPCTSTR message);
        void HideWarningMessage();

        void ChangePage(size_t newIndex);
        IUnknown *CurrentPage(void);
        HRESULT GetCurrentTitle([out, retval] LPBSTR pDisplayName);
  };

This interface is for internal use only.

IWizardDialogView Interface

  C++

  __interface IWizardDialogView : IUnknown
  {
      HRESULT LoadBannerImage(LPCTSTR bannerFilename);
      HRESULT LoadPage(LPCTSTR pageType, ISettingsProperties *pPageSettings,
  IWizardPageView **view);
      HRESULT SetEnable(WizardButtons button, BOOL enable);
      HRESULT Focus(WizardButtons button);
      void EnableFinish(BOOL isFinish);
      void Exit(int exitCode);
      void ShowWarningMessage(LPCTSTR message);
      void HideWarningMessage(void);
      void SetTitle(LPCTSTR title);
      void SetPageTitle(LPCTSTR title);
      int ShowMessageBox(LPCTSTR message, LPCTSTR lpCaption, UINT uType);
      HWND GetHwnd(void);
      void UpdateFocus(void);
  };

This interface is for internal use only.

IWizardPage Interface

  C++

  __interface IWizardPage : IUnknown
  {
      HRESULT SetPageSettings(ISettingsProperties *pPageSettings);
      HINSTANCE GetInstanceHandle(void);
      int GetDialogResourceId(void);

<!-- p.1672 -->

      void WindowCreated(IWizardPageView *pView, IWizardPageContainer
  *pContainer);
      void WindowShown(void);
      void WindowHidden(void);

      HRESULT NextSelected(void);
      void ControlEvent(WORD eventId, WORD controlId);
      void CommonControlEvent(WORD controlId, LPNMHDR pInfo, LPBOOL pCancel);
      void UnhandledEvent(HWND hwnd, UINT message, WPARAM wParam, LPARAM
  lParam);
  };

Overview

This interface is implemented by WizardPageImpl, so you will not typically have to
implement this it yourself. The wizard calls all of these methods for you when it interacts
with your custom pages.

IWizardPageContainer Interface

  C++

  __interface IWizardPageContainer : IUnknown
  {
      ILogger * Logger(void);
      IPropertyBag * Properties(void);
      HRESULT CreateInstance(LPCTSTR type, [out] IUnknown **ppInstance);
      HRESULT GetService(REFIID iid, [out] IUnknown **ppInstance);
      HRESULT ReplaceVariables(LPCTSTR source, [out] LPBSTR pDest);
      HRESULT GotoPage(LPCTSTR pageName);
      int ShowMessageBox(LPCTSTR message, LPCTSTR lpCaption, UINT uType);
      BOOL InPreview(void);
      HWND GetHwnd(void);
  };

Overview

This interface is available to your page via the Container method (implemented by
WizardPageImpl) and gives you access to various services of the wizard.

ILogger * Logger(void)

Use this method to write messages to the log file—for example:

  C++

<!-- p.1673 -->

  Logger()->Verbose(s_component, L"Message for log file");

IPropertyBag * Properties(void)

This method provides access to "memory" variables, which are properties that are in
memory only while the UDI Wizard is running. These properties are available to other
pages either in code or in the XML using the $memoryVarName$ syntax.

HRESULT CreateInstance(LPCTSTR type, [out] IUnknown
**ppInstance)

This method allows you to create a new instance of any component that has been
registered. However, it is better to use the template function CreateInstance, because it
is strongly typed.

HRESULT GetService(REFIID iid, [out] IUnknown **ppInstance)

This method allows you to retrieve a service that has been registered. However, it is
better to call the GetService template function, which is strongly typed (instead of using
IUnknown).

HRESULT ReplaceVariables(LPCTSTR source, [out] LPBSTR pDest)

This method handles working with variables inside string values. It supports the formats
shown in Table 51 and Table 52.

Table 51. HRESULT ReplaceVariables

                                                                                  ﾉ   Expand table

 Format      Description

 $Name$      Replaces the value of a memory variable with this name (If there is no memory
             variable with the name, the "token" will be removed.)

 %Name%      Either a task sequence variable or an environment variable. The order is as follows:

             1. Use the value of a task sequence variable, if present.
             2. Use the value of an environment variable, if present.
             3. Otherwise, remove this text from the string.

<!-- p.1674 -->

Table 52. HRESULT Parameter

                                                                                 ﾉ   Expand table

 Parameter   Description

 Source      The input string, which can contain any combination of $ and % variables or none at
             all

 pDest       On return, contains a new string that has all the tokens replaced according to Table
             51

HRESULT GotoPage(LPCTSTR pageName)

This method has not been fully tested. The idea is that you can switch directly to a
specific page based on the name of the page as defined in the .config XML file. Calling
this method bypasses the OnNextSelected on your page. In addition, the behavior of
this method is subject to change, so use it at your own risk.

int ShowMessageBox(LPCTSTR message, LPCTSTR lpCaption, UINT
uType)

This method displays a message box with the text and caption that you provide. The
uType parameter is any value that you can supply to the MessageBox Win32 function.

BOOL InPreview(void)

This method returns TRUE if you launched the wizard in "preview" mode by supplying
the /preview switch. In preview mode, the Next button is never disabled. This method
allows you to bypass code in preview mode, for example, that could cause issues when
you do not have valid data on the page.

HWND GetHwnd(void)

This method returns the HWND for the main dialog box. Use this method with care.
Generally, the UDI Wizard application programming interface is designed so that you
never work directly with window handles.

IWizardPageView Interface

  C++

<!-- p.1675 -->

  __interface IWizardPageView : IUnknown
  {
      HRESULT GetControlWrapper(int itemId, DialogControlTypes controlType,
  IUnknown **ppControl);
      HWND GetHwnd(void);
      HWND GetControl(int itemId);
      HRESULT Show (void);
      HRESULT Hide(void);
      HRESULT Focus(int itemId);
      IWizardPage * Page(void);
      IFormController * Form(void);

        HRESULT FocusWizardButton(WizardButtons button);
        HRESULT SetEnable(WizardButtons button, BOOL enable);
        void ShowWarningMessage(LPCTSTR message);
        void HideWarningMessage(void);
  };

This interface is available to the code in your page through the View method
(implemented by WizardPageImpl).

HRESULT GetControlWrapper(int itemId, DialogControlTypes
controlType, IUnknown *ppControl)

The UDI Wizard uses wrappers, which are really façades for interacting with the controls
on your page. Using these façades instead of the actual controls makes it much easier to
write tests for your page, because you can provide mock façades from your tests.

Instead of using this method directly, it is better to use the GetControlWrapper
template method, which is strongly typed—for example:

  C++

  PComboBox m_pLanguagePackCombo;
  GetControlWrapper(View(), IDC_MY_COMBO, CONTROL_COMBO_BOX, &m_pCombo);

HWND GetHwnd(void)

This method returns the window handle for your page. Generally, you should not need
access to this window handle.

HWND GetControl(int itemId)

If you must, you can call this method to get the window handle for a control on your
page. (It is better to call the GetControlWrapper template function).

<!-- p.1676 -->

HRESULT Show (void)

This method is for internal use only.

HRESULT Hide(void)

This method is for internal use only.

HRESULT Focus(int itemId)

Set the input focus to a specific control.

IWizardPage * Page(void)

This method is for internal use only.

IFormController * Form(void)

This method is for internal use only.

HRESULT FocusWizardButton(WizardButtons button)

Sets the focus to one of the wizard's buttons.WizardButtons has two values: BackButton
and NextButton.

HRESULT SetEnable(WizardButtons button, BOOL enable)

Request that one of the wizard buttons be enabled or disabled. The button might not
match the state that you request. For example, if you run the UDI Wizard with the
/preview switch, the buttons will always be enabled. WizardButtons has two values:
BackButton and NextButton.

void ShowWarningMessage(LPCTSTR message)

This method displays a warning message at the bottom of the page content area. This
message can be any text you want.

void HideWarningMessage(void)

Hide a warning message that you displayed with a call to ShowWarningMessage.

<!-- p.1677 -->

IXmlDocument Interface

  C++

  __interface IXmlDocument : IUnknown
      HRESULT Load(LPCTSTR filename);
      HRESULT LoadXml(LPCTSTR xml);
      HRESULT Save(LPCWSTR filename);
      HRESULT GetParseErrorMessage(LPBSTR pMessage);
      HRESULT SelectNodes(LPCTSTR xpath, IXMLDOMNodeList **ppNodes);
      HRESULT SelectSingleNode(LPCTSTR xpath, IXMLDOMNode **ppNode);
      HRESULT AddSchema(LPCTSTR filename, LPCTSTR ns);
      HRESULT AddAttribute(IXMLDOMNode *pNode, LPCWSTR name, LPCWSTR value);
      HRESULT CreateNode(DOMNodeType type, LPCWSTR name, LPCWSTR ns,
  IXMLDOMNode **ppNode);
  };

Overview

This interface is implemented by the ID_IXmlDocument component, which is a façade
designed to make it easier to work with XML documents in C++.

HRESULT Load(LPCTSTR filename)

This method loads an XML document from an external file. It returns S_OK if the file was
loaded without errors or S_FALSE if an error occurred. When there is an error, you can
get the error message by calling GetParseErrorMessage.

HRESULT LoadXml(LPCTSTR xml)

This method loads an XML document from a string instead of an external file. Other
than the source for reading the XML, the behavior is the same as the Load method.

HRESULT Save(LPCWSTR filename)

This method saves the XML document that is in memory to an external file.

HRESULT GetParseErrorMessage(LPBSTR pMessage)

This method returns a new string with the error message from loading the XML
document, if any. It always returns S_OK.

<!-- p.1678 -->

HRESULT SelectNodes(LPCTSTR xpath, IXMLDOMNodeList
**ppNodes)

This method allows you to use an XPath expression to retrieve a collection of nodes
from the document. It always returns S_OK.

HRESULT SelectSingleNode(LPCTSTR xpath, IXMLDOMNode
**ppNode)

This method allows you to use an XPath expression to retrieve one node from the
document. It always returns S_OK.

HRESULT AddSchema(LPCTSTR filename, LPCTSTR ns)

This method adds the name of an external schema file that will be used to validate the
schema of your XML document when it is loaded. The namespace you provide is the
string you can use in XPath queries, although this has not been tested.

HRESULT AddAttribute(IXMLDOMNode *pNode, LPCWSTR name,
LPCWSTR value)

This method adds a new attribute to an existing node in the XML document. See Table
53.

Table 53. HRESULT AddAttribute

                                                                          ﾉ   Expand table

 Parameter         Description

 pNode             The node to which you want to add an attribute

 Name              Name of the new attribute

 Value             The value for the new attribute

HRESULT CreateNode(DOMNodeType type, LPCWSTR name,
LPCWSTR ns, IXMLDOMNode **ppNode)

Call this method to create a new node:

  C++

<!-- p.1679 -->

  Pointer<IXMLDOMNode> pNewChild
  pXmlDom->CreateNode(NODE_ELEMENT, L"MyElement", L"", &pNewChild);

Once you create a new node, you can add it as a child to another node by calling the
parent's appendChild method.

Helper Functions

CreateInstance Template Function

  C++

  HRESULT CreateInstance(IWizardPageContainer *pContainer, LPCTSTR type, I
  **ppObject)

This function is defined in IWizardPageContainer.h and provides a type-safe wrapper
over the IWizardPageContainer->CreateInstance method—for example:

  C++

  CreateInstance<IDirectory>(Container(), ID_Directory, &pDirectory);

This code creates a new ID_Directory component to retrieve the IDirectory interface of
that component.

GetService Template Function

  C++

  void GetService(IWizardPageContainer *pContainer, I **ppService)

This function is defined in IWizardPageContainer.h and provides a type-safe wrapper
over the IWizardPageContainer->GetService method—for example:

  C++

  GetService<ITSVariableBag>(Container(), &pTsBag);

This function retrieves the task sequence component, which supports the
ITSVariableBag interface. (For ITSVariableBag, you can use the TSVariables method of
the WizardPageImpl class, instead.)

<!-- p.1680 -->

UDI Wizard Designer Configuration File Schema
Reference
This file is consumed by the UDI Wizard Designer. A separate file is created for each
custom .dll file, which can contain custom wizard page editors, custom tasks, or custom
validators. The file must end with .config and reside in the installation_folder\Bin\Config
folder (where installation_folder is the folder in which you installed MDT).

Table 54 lists the elements in the UDI Wizard Designer configuration file and their
descriptions. The DesignerConfig element is the root node for this reference.

Table 54. Elements in the UDI Wizard Designer
Configuration File and Their Descriptions

                                                                                   ﾉ   Expand table

 Element Name        Description

 DesignerConfig      Specifies the root for all other elements

 DesignerMappings    Groups a set of Pageelements

 Page                Specifies a wizard page editor to be loaded in the UDI Wizard Designer,
                     which is used to edit the configuration settings for a wizard page

 Param               Specifies a parameter that is passed to the parent Task or Validator element
                     and corresponds to a Setter element in the UDI Wizard configuration file
                     Note: The attributes for this element are different if the parent is the Task or
                     Validator element.

 Task                Specifies a task within the task library

 TaskItem            Specifies a group of parameters that are passed to the task

 TaskLibrary         Groups a set of Task elements

 Validator           Specifies a validator within the validator library

 ValidatorLibrary    Groups a set of Validator elements

DesignerConfig
This element specifies the root for all other elements.

Element Information
