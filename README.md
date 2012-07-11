`pingpong` is a library to aimed at simplifying email in django.

[You should probably send more email](http://www.kalzumeus.com/2012/05/31/can-i-get-your-email/)… and this will make it so easy that you don't think twice about it!

## Installation ##

 1. Install lib with pip:
 
    `pip install pingpong`
   
    **- OR -**

    Put the "pingpong" directory somewhere in your python path

 2. Add "pingpong" to your installed apps (in the settings.py file)

## A better way to fire off emails

    from pingpong.email import render_to_email
    
    def some_function():
    
        template = "emails/muffins.email"
        context = { "your_mom": "Betty Crocker", "muffin_type": "blueberry" }
        recipients = ['somebody@example.com']
        
        # send an email!
        render_to_email(template, context, recipients)
        
And the template, `emails/my_email_template.email` would be in your main 
templates folder:

    Delicious muffins thanks to {{ your_mom }}
    
    
    Hi friend,
    
    I'm writing to let you know that {{ your_mom }} made some superb 
    {{ muffin_type }} muffins. Please tell her thank you!
    
    Thanks,
    A Robot
    
The first non-blank line is the subject, everything following is the message.

Subject: 

    Delicious muffins thanks to Betty Crocker

Message:

    I'm writing to let you know that Betty Crocker made some superb 
    blueberry muffins. Please tell her thank you!
    
    Thanks,
    A Robot

Whitespace is stripped from the beginning and end of the message.

## Passing system events to your app (and then sending an email?)

set up listeners:

    # listeners.py
    
    from pingpong.utils import pong
    
    @pong("dailycron")
    def email_admins_about_daily_activity(ping_name, args, kwargs, **kw):
        render_to_email(…)
        
        
    # models.py
    
    ... your models...
    
    import listeners
      
Then you trigger all functions listening to "dailycron" like so:

    $ python manage.py pong dailycron
    
If you pass extra args to the management command they will get passed along...

    $ python manage.py pong cachecleared memcache:38174
    
You can use pong to pass *any* system event into your app. 

In this case we're letting the app know that memcache on port 38174 just got cleared.

    from pingpong.utils import pong
    
    @pong("cachecleared")
    def warm_up_cache(ping_name, args, kwargs, **kw):
        assert ping_name == "cachecleared"
        assert args[0] == "memcache:38174"
        
        cache_type, port = args[0].split(":")
        ...