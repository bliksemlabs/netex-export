from destinationdisplays import destinationdisplays

def timetableframe(cur, operator, sequence):
    out = '<TimetableFrame version="any" id="%(operator)s:TimetableFrame:%(sequence)s">' % {'operator': operator, 'sequence': sequence}
    print out

    print destinationdisplays(cur)

    out = '<vehicleJourneys>'

    sql = 'SELECT * FROM servicepatterns;'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        out += """<ServicePattern version="any" id="%(id)s"><RouteRef version="any" ref="%(routeref)s"/><pointsInSequence>""" % row
        sql = 'SELECT * FROM stoppointinjourneypatterns WHERE servicepatternref = %(id)s';
        cur.execute(sql, row)
        for row2 in cur.fetchall():
            out += """<StopPointInJourneyPattern version="any" id="%(id)s" order="%(stoporder)d"><ScheduledStopPointRef version="any" ref="%(scheduledstoppointref)s"/><AuthorityRef version="any" ref="%(authorityref)s"/><DestinationDisplayRef version="any" ref="%(destinationdisplayref)s"/></StopPointInJourneyPattern>""" % row2
        out += """</pointsInSequence></ServicePattern>"""
        print out
        out = ''

    sql = 'SELECT * FROM servicejourney;'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        out += """<ServiceJourney version="any" id="%(id)s"><dayTypes><DayTypeRef version="any" ref="%(daytyperef)s"/></dayTypes><ServicePatternRef version="any" ref="%(servicepatternref)s"/>""" % row

        if row['destinationdisplayref']:
            out += """<DestinationDisplayRef version="any" ref="%(destinationdisplayref)s"/>"""

        out += """<OperatorRef version="any" ref="%(operatorref)s"/><passingTimes>"""
        
        sql = 'SELECT * FROM timetabledpassingtimes WHERE servicejourneyref = %(id)s;'
        
        cur.execute(sql, row)
        for row2 in cur.fetchall():
            pre = """<TimetabledPassingTime version="any" id="%(id)s"><StopPointInJourneyPatternRef version="any" ref="%(stoppointinjourneypatternref)s"/>"""
            if row2['arrivaltime']:
                pre += '<ArrivalTime>%(arrivaltime)s</ArrivalTime>'
            if row2['departuretime']:
                pre += '<DepartureTime>%(departuretime)s</DepartureTime>'
            if row2['waitingtime']:
                pre += '<WaitingTime>%(waitingtime)s</WaitingTime>'

            out += pre % row2

            out += """</TimetabledPassingTime>"""

        out += """</passingTimes></ServiceJourney>"""
        print out
        out = ''

    out += '</vehicleJourneys></TimetableFrame>'
    print out

    return ''
