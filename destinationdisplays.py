def destinationdisplays(cur):
    out = '<destinationDisplays>'

    sql = "SELECT * FROM destinationdisplays;"
    cur.execute(sql)
    for row in cur.fetchall():
        out += """<DestinationDisplay version="any" id="%(id)s"><Name>%(name)s</Name><ShortName>%(shortname)s</ShortName>""" % row
        if row['via']:
            out += "<vias><Via>%(via)s</Via></vias>" % row

        out += '</DestinationDisplay>\n'
    out += '</destinationDisplays>\n'
    return out        
