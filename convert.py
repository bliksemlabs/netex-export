import psycopg2
import psycopg2.extras

from servicecalendarframe import servicecalendarframe
from serviceframe import serviceframe
from timetableframe import timetableframe

conn = psycopg2.connect("dbname=kv1netex")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#print servicecalendarframe(cur, 'arr', 1)
print serviceframe(cur, 'arr', 1)
#print timetableframe(cur, 'arr', 1)
