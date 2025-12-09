import socket
import platform
import datetime
import subprocess

def get_flag_context(request=None):
    """
    Mimics the PHP flag.php: returns judgeid, ctrlid, categ from session, date, time, pc name, and local IP.
    If request is None, session values will be None.
    """
    session = request.session if request else {}
    myjudgeid = session.get('judgeid') if request else None
    myctrlid = session.get('ctrlid') if request else None
    mycateg = session.get('categ') if request else None
    mydate = datetime.datetime.now().strftime('%m/%d/%Y')
    mytime = datetime.datetime.now().strftime('%A %dth of %B %Y %I:%M:%S %p')
    mypcname = platform.node()
    myip = None
    try:
        # Try to get the first non-loopback IPv4 address
        hostname = socket.gethostname()
        myip = socket.gethostbyname(hostname)
        if myip.startswith('127.'):
            # Try to get from ipconfig (Windows)
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if 'IPv4 Address' in line or 'IP Address' in line:
                    parts = line.split(':')
                    if len(parts) > 1:
                        myip = parts[1].strip()
                        break
    except Exception:
        pass
    return {
        'myjudgeid': myjudgeid,
        'myctrlid': myctrlid,
        'mycateg': mycateg,
        'mydate': mydate,
        'mytime': mytime,
        'mypcname': mypcname,
        'myip': myip,
    }
