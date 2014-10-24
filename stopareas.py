def stopareas(cur):
    out = '<stopAreas>'

    sql = 'SELECT * FROM stopareas;'
    cur.execute(sql)
    for row in cur.fetchall():
        optional = ''
        if row['description']:
            optional = '    <Description>%(description)s</Description>\n'
        out += ("""<StopArea version="any" id="%(id)s">
    <Name>%(name)s</Name>
    <TopographicPlaceView>
        <TopographicPlace>
            <Name>%(topographicplacename)s</Name>
            <TopographicPlaceType>town</TopographicPlaceType>
        </TopographicPlace>
    </TopographicPlaceView>
"""+optional+'</StopArea>\n') % row
    out += '</stopAreas>'
    return out 
