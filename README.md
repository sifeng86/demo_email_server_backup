# Terminal 1 Assessment


https://github.com/uber-archive/coding-challenge-tools/blob/master/coding_challenge.md

## Email Service

Create a service that accepts the necessary information and sends emails. It should provide an abstraction between two different email service providers. If one of the services goes down, your service can quickly failover to a different provider without affecting your customers.

### Hosting: 
- Heroku
### Email Service: 
- Sendgrid (Primary)
- Cachigo (Secondary)

### Languanges:
- Python
- PHP
- HTML & CSS

# How it works:

### Demo Page
https://send-mail-t1-php.herokuapp.com/

The demo page is a simulation of email server online status and offline status.

- User input an email address
- The dropdown option is to simulate the primary email server is online or offline
- Concept: if the primary email server goes down (not return 200) then the secondary email server will send the emails.

