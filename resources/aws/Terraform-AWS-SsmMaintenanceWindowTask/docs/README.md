# Terraform::AWS::SsmMaintenanceWindowTask

Provides an SSM Maintenance Window Task resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmMaintenanceWindowTask",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>" : <i>String</i>,
        "<a href="#maxerrors" title="MaxErrors">MaxErrors</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#taskarn" title="TaskArn">TaskArn</a>" : <i>String</i>,
        "<a href="#tasktype" title="TaskType">TaskType</a>" : <i>String</i>,
        "<a href="#windowid" title="WindowId">WindowId</a>" : <i>String</i>,
        "<a href="#logginginfo" title="LoggingInfo">LoggingInfo</a>" : <i>[ <a href="logginginfo.md">LoggingInfo</a>, ... ]</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ <a href="targets.md">Targets</a>, ... ]</i>,
        "<a href="#taskinvocationparameters" title="TaskInvocationParameters">TaskInvocationParameters</a>" : <i>[ <a href="taskinvocationparameters.md">TaskInvocationParameters</a>, ... ]</i>,
        "<a href="#taskparameters" title="TaskParameters">TaskParameters</a>" : <i>[ <a href="taskparameters.md">TaskParameters</a>, ... ]</i>,
        "<a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>" : <i>[ <a href="automationparameters.md">AutomationParameters</a>, ... ]</i>,
        "<a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>" : <i>[ <a href="lambdaparameters.md">LambdaParameters</a>, ... ]</i>,
        "<a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>" : <i>[ <a href="runcommandparameters.md">RunCommandParameters</a>, ... ]</i>,
        "<a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>" : <i>[ <a href="stepfunctionsparameters.md">StepFunctionsParameters</a>, ... ]</i>,
        "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameter.md">Parameter</a>, ... ]</i>,
        "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfig.md">NotificationConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmMaintenanceWindowTask
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>: <i>String</i>
    <a href="#maxerrors" title="MaxErrors">MaxErrors</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#taskarn" title="TaskArn">TaskArn</a>: <i>String</i>
    <a href="#tasktype" title="TaskType">TaskType</a>: <i>String</i>
    <a href="#windowid" title="WindowId">WindowId</a>: <i>String</i>
    <a href="#logginginfo" title="LoggingInfo">LoggingInfo</a>: <i>
      - <a href="logginginfo.md">LoggingInfo</a></i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - <a href="targets.md">Targets</a></i>
    <a href="#taskinvocationparameters" title="TaskInvocationParameters">TaskInvocationParameters</a>: <i>
      - <a href="taskinvocationparameters.md">TaskInvocationParameters</a></i>
    <a href="#taskparameters" title="TaskParameters">TaskParameters</a>: <i>
      - <a href="taskparameters.md">TaskParameters</a></i>
    <a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>: <i>
      - <a href="automationparameters.md">AutomationParameters</a></i>
    <a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>: <i>
      - <a href="lambdaparameters.md">LambdaParameters</a></i>
    <a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>: <i>
      - <a href="runcommandparameters.md">RunCommandParameters</a></i>
    <a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>: <i>
      - <a href="stepfunctionsparameters.md">StepFunctionsParameters</a></i>
    <a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameter.md">Parameter</a></i>
    <a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfig.md">NotificationConfig</a></i>
</pre>

## Properties

#### Description

The description of the maintenance window task.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrency

The maximum number of targets this task can be run for in parallel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxErrors

The maximum number of errors allowed before this task stops being scheduled.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the maintenance window task.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

The role that should be assumed when executing the task.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskArn

The ARN of the task to execute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskType

The type of task being registered. The only allowed value is `RUN_COMMAND`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowId

The Id of the maintenance window to register the task with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingInfo

_Required_: No

_Type_: List of <a href="logginginfo.md">LoggingInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

_Required_: No

_Type_: List of <a href="targets.md">Targets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskInvocationParameters

_Required_: No

_Type_: List of <a href="taskinvocationparameters.md">TaskInvocationParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskParameters

_Required_: No

_Type_: List of <a href="taskparameters.md">TaskParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomationParameters

_Required_: No

_Type_: List of <a href="automationparameters.md">AutomationParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaParameters

_Required_: No

_Type_: List of <a href="lambdaparameters.md">LambdaParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandParameters

_Required_: No

_Type_: List of <a href="runcommandparameters.md">RunCommandParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepFunctionsParameters

_Required_: No

_Type_: List of <a href="stepfunctionsparameters.md">StepFunctionsParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameter.md">Parameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfig.md">NotificationConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

