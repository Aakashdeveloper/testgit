import boto3
client = boto3.client('ce')

response = client.get_cost_and_usage(
    TimePeriod={
         'Start': '2020-05-01',
        'End': '2020-05-20'
    },
    Granularity='DAILY',
    Filter={
        'Or': [
            {'... recursive ...'},
        ],
        'And': [
            {'... recursive ...'},
        ],
        'Not': {'... recursive ...'},
        'Dimensions': {
             "Key": "LINKED_ACCOUNT",
                "Values": [751900335485],
            'MatchOptions': [
                'EQUALS',
            ]
        },
        'CostCategories': {
            'Key': 'string',
            'Values': [
                'string',
            ]
        }
    },
    Metrics=[
        'string',
    ],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'string'
        },
    ],
    NextPageToken='string'
)
'''result = client.get_cost_and_usage(
    TimePeriod = {
        'Start': '01-05-2020',
        'End': '20-05-2020'
    },
    Granularity = 'DAILY',
    Filter = {
        "And": [{
            "Dimensions": {
                "Key": "LINKED_ACCOUNT",
                "Values": [751900335485]
            }
        }, {
            "Not": {
                "Dimensions": {
                    "Key": "RECORD_TYPE",
                    "Values": ["Credit", "Refund"]
                }
            }
        }]
    },
    Metrics = ["BlendedCost"],
    GroupBy = [
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
        {
            'Type': 'DIMENSION',
            'Key': 'USAGE_TYPE'
        }
    ]
)
'''