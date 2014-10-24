def scheduledstoppoints(cur):
    out = '<scheduledStopPoints>'

    sql = "SELECT * FROM scheduledstoppoints;"
    cur.execute(sql)
    for row in cur.fetchall():
        optional = ''
        if row['stoparearef']:
            optional += """    <stopAreas>
        <StopAreaRef ref="%(stoparearef)s"/>
    </stopAreas>\n"""
        if row['description']:
            optional += '    <Description>%(description)s</Description>\n'
        out += ("""<ScheduledStopPoint version="any" id="%(id)s">
    <Name>%(name)s</Name>
    <Location>
        <gml:pos srsName="EPSG:28992">%(x)d %(y)d</gml:pos>
    </Location>
    <TimingPointType>%(timingpointtype)s</TimingPointType>
    <PublicCode>%(publiccode)s</PublicCode>
    <ForBoarding>%(forboarding)s</ForBoarding>
    <ForAlighting>%(foralighting)s</ForAlighting>
    <TopographicPlaceView>
        <TopographicPlace>
            <Name>%(topographicplacename)s</Name>
            <TopographicPlaceType>town</TopographicPlaceType>
        </TopographicPlace>
    </TopographicPlaceView>"""+optional+"""
</ScheduledStopPoint>
""") % row

    out += '</scheduledStopPoints>'
    return out
