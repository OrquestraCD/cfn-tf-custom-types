# Terraform::AWS::MskCluster BrokerLogs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ <a href="brokerlogs-cloudwatchlogs.md">CloudwatchLogs</a>, ... ]</i>,
    "<a href="#firehose" title="Firehose">Firehose</a>" : <i>[ <a href="brokerlogs-firehose.md">Firehose</a>, ... ]</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="brokerlogs-s3.md">S3</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - <a href="brokerlogs-cloudwatchlogs.md">CloudwatchLogs</a></i>
<a href="#firehose" title="Firehose">Firehose</a>: <i>
      - <a href="brokerlogs-firehose.md">Firehose</a></i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="brokerlogs-s3.md">S3</a></i>
</pre>

## Properties

#### CloudwatchLogs

_Required_: No

_Type_: List of <a href="brokerlogs-cloudwatchlogs.md">CloudwatchLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firehose

_Required_: No

_Type_: List of <a href="brokerlogs-firehose.md">Firehose</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="brokerlogs-s3.md">S3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

