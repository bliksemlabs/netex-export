from scheduledstoppoints import scheduledstoppoints
from stopareas import stopareas

hasdescription = '<Description>%(description)s</Description>'

def serviceframe(cur, operator, sequence):
    out = '<ServiceFrame xmlns:gml="http://www.opengis.net/gml/3.2" version="any" id="%(operator)s:ServiceFrame:%(sequence)s">' % {'operator': operator, 'sequence': sequence}

    print out
    print stopareas(cur)
    print scheduledstoppoints(cur)

    out = '<routePoints>'

    sql = 'SELECT * FROM routepoint;'
    cur.execute(sql)
    for row in cur.fetchall():
        optional = ''
        if row['description']:
            optional += hasdescription
        if row['bordercrossing'] == True:
            optional += '<BorderCrossing>true</BorderCrossing>'
        if row['via'] == True:
            optional += '<Via>true</Via>'

        out += ("""<RoutePoint version="any" id="%(id)s"><Location><gml:pos srsName="EPSG:28992">%(x)d %(y)d</gml:pos></Location>"""+optional+'</RoutePoint>') % row
        print out
        out = ''

    out += '</routePoints><routes>'

    sql = 'SELECT * FROM routes;'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        optional = ''
        if row['description']:
            optional += hasdescription
        out += ("""<Route version="any" id="%(id)s"><DirectionType>%(directiontype)s</DirectionType><LineRef>%(lineref)s</LineRef>"""+optional+"""<pointsInSequence>""") % row

        sql = 'SELECT * FROM pointonroute WHERE routeref = %(id)s';
        cur.execute(sql, row)
        for row2 in cur.fetchall():
            out += '<PointOnRoute version="any" id="%(id)s" order="%(stoporder)d"><RoutePointRef version="any" ref="%(pointref)s"/></PointOnRoute>'%row2
            print out 
            out = ''
        out += """</pointsInSequence></Route>"""
    
    out += '</routes><lines>'

    sql = 'SELECT * FROM lines;'
    cur.execute(sql)
    for row in cur.fetchall():
        optional = ''
        if row['monitored']:
            optional += '<Monitored>%(monitored)s</Monitored>'
        if row['description']:
            optional += hasdescription

        out += ("""<Line version="any" id="%(id)s"><Name>%(name)s</Name><TransportMode>%(transportmode)s</TransportMode><PublicCode>%(publiccode)s</PublicCode><PrivateCode>%(privatecode)s</PrivateCode>"""+optional+"""</Line>""") % row
        print out
        out = ''
    
    out += '</lines></ServiceFrame>'
    print out
    out = ''
    
    return out
