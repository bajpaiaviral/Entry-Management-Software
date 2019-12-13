
*Note api keys,email ids,message apis are removed for you to enter . 
Logic Used -

Check-In -
1.The user coming on the homepage was given the options to check-in or check-out . 

2.The user wanting to checkout will have to to enter his contact details along with the host's details .

3.As soon as he fills the form for check-in , the host would be notified on e-mail and mobile number . 

4.CheckIn time will be stored in database along with a boolean value storing information that the guest has checked-in .

5. On successful checkin , guest will be notified on screen for successful request And will also be told to check entered details on failure .

Check-Out -

1. When the guest want to checkout , the checkin object with the e-mail same as guest and boolean set to already checked-in will be called and set to checked out . 

2.The guest will be sent a mail and a message on mobile about his visit details .

3.And hence the multiple visits of same guests are also managed .

4.On successful checkout , guest will be notified on screen for successful request And will also be told to check entered details on failure .


Technology Used -
For FrontEnd  - HTML,CSS,BootStrap,Javascript
For BackEnd - Python ,Django Framework,SQlite





