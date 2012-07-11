from signals import signal_ping

def send_ping(ping_name, *args, **kwargs):
    signal_ping.send(sender=None, ping_name=ping_name, args=args, kwargs=kwargs)

def pong(ping_name):
    """
    usage example:
    
        @pong("hourly")
        def listen_to_hourly_ping(**kwargs):
            ...
    
    which will be triggered by
    
        $ python manage.py pong hourly
    """
    def decorator(fn):
        def wrapper(*args, **kwargs):
            # only trigger callback if the ping_name matches
            if kwargs['ping_name'] == ping_name:
                fn(*args, **kwargs)
                
        signal_ping.connect(wrapper)
        
        # keep a reference to the wrapper fn since django signals use weakref
        fn.pongs = getattr(fn, "pongs", [])
        fn.pongs.append(wrapper)
        
        return fn
    return decorator