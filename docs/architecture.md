┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    ┌────────────┐
│   Client    │────│ API Gateway  │────│ Lambda Functions│────│ DynamoDB   │
│ (Web/Mobile)│    │              │    │                 │    │            │
└─────────────┘    └──────────────┘    └─────────────────┘    └────────────┘
│
│
┌─────────────┐
│ CloudWatch  │
│    Logs     │
└─────────────┘


## Components:
- **API Gateway**: RESTful endpoints for banking operations
- **Lambda Functions**: Serverless compute for business logic
- **DynamoDB**: NoSQL database for accounts and transactions
- **CloudWatch**: Monitoring and logging
