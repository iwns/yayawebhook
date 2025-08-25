## Description
**yayawebhook** is a simple API that demonstrates how to handle webhooks sent from **YaYa Wallet** whenever a transaction occurs on a user account.

## How It’s Built
This project was developed by following the official YaYa Wallet Help Center guide.  
The handler is designed to:
- Parse and filter the data received from YaYa Wallet webhooks.
- Use the data for different application-specific purposes.
- Verify incoming events to ensure they are authentic, as outlined in the YaYa Wallet documentation.

## Tech Stack
- **Django**

## Test
Test part done using Postman and follow structure of a webhook payload as stated on YaYa wallet documentation. To do that
- I create Post method request from postman which include
  -body same structure webhook handler and
  -add header 'YAYA-SIGNTURE' key which is used for verification of authentic
