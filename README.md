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

### Important! Read it before experience the demo page.

1) We want to simulate if the primary server is down, what is going to happen.
2) In the normal situation, the primary server(sendgrid) will not go down(that mean secondary server will not get activated).
3) If we want to let primary server goes down, then we need to manually assign a non 200 status.
4) Demo page is for verifying the service is true and functionable.
5) It should be automatic in production stage.

### Demo Page
https://send-mail-t1-php.herokuapp.com/

The demo page is a simulation of email server online status and offline status.

- User input an email address
- The dropdown option is to simulate the primary email server is online or offline (200 or 400)
- Concept: if the primary email server goes down (not return 200) then the secondary email server will send the emails.
- The email subject will show that where the sender come from.
- Please check the email in the spam folder if not in inbox.

### Technical Part

- The page coded by html & css
- Email API is using python and php
- Hosting two apps on heroku, 1 for php and 1 for python
