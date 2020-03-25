# Terraform::NewRelic::NrqlAlertCondition

Use this resource to create and manage NRQL alert conditions in New Relic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::NrqlAlertCondition",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#expectedgroups" title="ExpectedGroups">ExpectedGroups</a>" : <i>Double</i>,
        "<a href="#ignoreoverlap" title="IgnoreOverlap">IgnoreOverlap</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#valuefunction" title="ValueFunction">ValueFunction</a>" : <i>String</i>,
        "<a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>" : <i>Double</i>,
        "<a href="#nrql" title="Nrql">Nrql</a>" : <i>[ <a href="nrql.md">Nrql</a>, ... ]</i>,
        "<a href="#term" title="Term">Term</a>" : <i>[ <a href="term.md">Term</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::NrqlAlertCondition
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#expectedgroups" title="ExpectedGroups">ExpectedGroups</a>: <i>Double</i>
    <a href="#ignoreoverlap" title="IgnoreOverlap">IgnoreOverlap</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#valuefunction" title="ValueFunction">ValueFunction</a>: <i>String</i>
    <a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>: <i>Double</i>
    <a href="#nrql" title="Nrql">Nrql</a>: <i>
      - <a href="nrql.md">Nrql</a></i>
    <a href="#term" title="Term">Term</a>: <i>
      - <a href="term.md">Term</a></i>
</pre>

## Properties

#### Enabled

Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `value_function` - (Optional) Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedGroups

Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOverlap

Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static` or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `value_function` - (Optional) Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition should be used.
- `name` - (Required) The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static` or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `value_function` - (Optional) Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `value_function` - (Optional) Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the condition. Valid values are `static` or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `value_function` - (Optional) Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueFunction

Possible values are `single_value`, `sum`.
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `ignore_overlap` - (Optional) Whether to look for a convergence of groups when using `outlier` detection.
- `violation_time_limit_seconds` - (Optional) Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTimeLimitSeconds

Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.  Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

_Required_: No

_Type_: List of <a href="nrql.md">Nrql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Term

_Required_: No

_Type_: List of <a href="term.md">Term</a>

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

