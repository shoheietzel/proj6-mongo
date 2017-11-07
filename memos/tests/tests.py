#########################
# PLEASE DO THESE TESTS ON AN INITIALLY EMPTY MEMO DATABASE #########################

### Date formatting ###
# not required since date is automatically
# formatted by our HTML form.

### Timezone testing ###
# timezone always entered as UTC thentakes into account local timezone, so I do not see how we can test for any issues.

### Close dates ##
# Project asks to test close dates, but I see that humanize
# rounds date to nearest day. Therefore if we set utcnow
# after noon it will default to "tomorrow" (since the
# beginning of tomorrow is closer than the beginning of today),
# but if it is before noon it will default to "today".
# Therefore test cases are difficult unless we know what
# time of the day the tester is testing.


import flask_main
import config
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)
import arrow
from pymongo import MongoClient

# set database
dbclient = MongoClient(flask_main.MONGO_CLIENT_URL)
db = getattr(dbclient, flask_main.CONFIG.DB)
collection = db.date
database = flask_main.dbclient.memos_of_mongo.memos


def test_create_and_delete_memo():
    """
    Tests insertion and deletion functions of our server.
    Insert a memo, confirm its there,
    then immediately delete it, to return to its original state. If deletion is incorrect following tests will fail.
    """
    date = '2017-12-25T00:00:00+00:00'
    text = 'this is a memo'

    data_to_send = {'date': date, 'text': text}

    database.insert(data_to_send)

    record = database.find_one()
    assert record['date'] == '2017-12-25T00:00:00+00:00'
    database.remove()


def test_order_memo():
    """
    Tests our ordering logic behind our server.
    """
    date1 = '2017-12-25T00:00:00+00:00'
    text1 = 'Christmas'
    date2 = '2017-11-23T00:00:00+00:00'
    text2 = 'Thanksgiving'
    date3 = '2017-09-22T00:00:00+00:00'
    text3 = 'School started'

    data_to_send1 = {'date': date1, 'text': text1}
    data_to_send2 = {'date': date2, 'text': text2}
    data_to_send3 = {'date': date3, 'text': text3}

    database.insert(data_to_send1)
    database.insert(data_to_send2)
    database.insert(data_to_send3)

    records = flask_main.get_memos()

    # Should be ordered old to new
    assert records[0]['date'] == '2017-09-22T00:00:00+00:00'
    assert records[1]['date'] == '2017-11-23T00:00:00+00:00'
    assert records[2]['date'] == '2017-12-25T00:00:00+00:00'

    database.remove()
    database.remove()
    database.remove()
