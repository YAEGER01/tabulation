from django.db import connection
import hashlib

def create_tables_and_admins():
    table_sqls = [
        '''CREATE TABLE IF NOT EXISTS sadmin(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50),
            userlevel VARCHAR(5),
            uname VARCHAR(50),
            spassword TEXT
        )''',
        '''CREATE TABLE IF NOT EXISTS scorevents(
            evid INTEGER PRIMARY KEY AUTOINCREMENT,
            evdes VARCHAR(150)
        )''',
        '''CREATE TABLE IF NOT EXISTS sjudge(
            ejid INTEGER PRIMARY KEY AUTOINCREMENT,
            evid INTEGER,
            jname VARCHAR(100),
            uname VARCHAR(30),
            category VARCHAR(20),
            spassword TEXT,
            FOREIGN KEY (evid) REFERENCES scorevents(evid) ON DELETE RESTRICT ON UPDATE CASCADE
        )''',
        '''CREATE TABLE IF NOT EXISTS scri(
            scri INTEGER PRIMARY KEY AUTOINCREMENT,
            ctitle VARCHAR(50),
            cper INTEGER,
            evid INTEGER,
            category VARCHAR(20),
            minrate VARCHAR(5),
            status VARCHAR(2)
        )''',
        '''CREATE TABLE IF NOT EXISTS scandidates(
            sconid INTEGER PRIMARY KEY AUTOINCREMENT,
            evid INTEGER,
            ejid INTEGER,
            cano INTEGER,
            cname VARCHAR(100),
            course VARCHAR(10),
            category VARCHAR(20),
            canstatus VARCHAR(2),
            FOREIGN KEY (evid) REFERENCES scorevents(evid) ON DELETE RESTRICT ON UPDATE CASCADE,
            FOREIGN KEY (ejid) REFERENCES sjudge(ejid) ON DELETE RESTRICT ON UPDATE CASCADE
        )''',
        '''CREATE TABLE IF NOT EXISTS sinscore(
            sconid INTEGER,
            evid INTEGER,
            ejid INTEGER,
            scri INTEGER,
            inscore VARCHAR(6) DEFAULT '0',
            category VARCHAR(20),
            subdon VARCHAR(2) DEFAULT '0',
            cristat VARCHAR(2),
            FOREIGN KEY (sconid) REFERENCES scandidates(sconid) ON DELETE RESTRICT ON UPDATE CASCADE,
            FOREIGN KEY (evid) REFERENCES scorevents(evid) ON DELETE RESTRICT ON UPDATE CASCADE,
            FOREIGN KEY (ejid) REFERENCES sjudge(ejid) ON DELETE RESTRICT ON UPDATE CASCADE
        )''',
        '''CREATE TABLE IF NOT EXISTS resall(
            sconid INTEGER,
            evid INTEGER,
            ejid INTEGER,
            scri INTEGER,
            inscore VARCHAR(6),
            category VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS rescri(
            sconid INTEGER,
            evid INTEGER,
            ejid INTEGER,
            scri INTEGER,
            inscore VARCHAR(6),
            category VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS resnoshow(
            noshow VARCHAR(3)
        )''',
        '''CREATE TABLE IF NOT EXISTS judgesapproved(
            ejid INTEGER,
            evid INTEGER,
            sconid INTEGER,
            aprem VARCHAR(2)
        )''',
        '''CREATE TABLE IF NOT EXISTS judgecriteria(
            ejid INTEGER,
            scri INTEGER
        )''',
    ]
    with connection.cursor() as cursor:
        for sql in table_sqls:
            cursor.execute(sql)
        # Check if sadmin has any rows
        cursor.execute("SELECT COUNT(*) FROM sadmin")
        num = cursor.fetchone()[0]
        if num <= 0:
            # Insert default admin users
            admin_users = [
                ("joelgumiran", hashlib.md5("statadmin".encode()).hexdigest(), "0", "joelgumiran"),
                ("admin", hashlib.md5("isuadmin".encode()).hexdigest(), "1", "administrator"),
            ]
            for username, spassword, userlevel, uname in admin_users:
                cursor.execute(
                    "INSERT INTO sadmin (username, spassword, userlevel, uname) VALUES (?, ?, ?, ?)",
                    [username, spassword, userlevel, uname]
                )
