def servicecalendarframe(cur, operator, sequence):
    sql = "SELECT min(date) AS mindate, max(date) AS maxdate FROM daytypeassignments;"
    cur.execute(sql)
    row = cur.fetchone()
    out = """<ServiceCalendarFrame version="any" id="%(operator)s:ServiceCalendarFrame:%(sequence)s">
    <ServiceCalendar version="any" id="%(operator)s:ServiceCalendar:%(sequence)s">
        <FromDate>%(mindate)s</FromDate>
        <ToDate>%(maxdate)s</ToDate>
    </ServiceCalendar>
<dayTypes>""" % {'operator': operator, 'sequence': sequence, 'mindate': row['mindate'], 'maxdate': row['maxdate']}

    sql = "SELECT DISTINCT * FROM daytype;"
    cur.execute(sql)
    for row in cur.fetchall():
        out += """<DayType version="any" id="%(id)s">
    <Description>%(description)s</Description>
</DayType>""" % row
    
    out += """</dayTypes>
<dayTypeAssignments>"""
    
    sql = "SELECT * FROM daytypeassignments;"
    cur.execute(sql)
    for row in cur.fetchall():
        optional = ''
        if row['description']:
            optional = '    <Description>%(description)s</Description>\n'
        out += ("""<DayTypeAssignment version="any">
    <Date>%(date)s</Date>
    <DayTypeRef version="any" ref="%(daytyperef)s"/>"""+optional+"""
</DayTypeAssignment>
""") % row

    out += """</dayTypeAssignments>
</ServiceCalendarFrame>"""

    return out
