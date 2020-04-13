from sqlalchemy import create_engine
from sqlalchemy import sql
from WIFI import config
engine = create_engine(config.database_uri)


def get_all():
    with engine.connect() as con:
        rs = con.execute("select * from wifi_info")
        return [dict(row) for row in rs]

def get_name(BSSID):
    with engine.connect() as con:
        rs = con.execute("select SSID from SSID where BSSID =:BSSID")
        return [dict(row) for row in rs]

def get_cord(BSSID):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM cord WHERE BSSID = :BSSID;"
        )

        rs = con.execute(query, BSSID=BSSID)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def get_label(BSSID):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM label WHERE BSSID = :BSSID;"
        )

        rs = con.execute(query, BSSID=BSSID)
        result = rs.first()
        if result is None:
            return None
        return dict(result)