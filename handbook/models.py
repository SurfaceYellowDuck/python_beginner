import orm_sqlite


class PhoneNumbers(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    name = orm_sqlite.StringField()
    phone_number = orm_sqlite.StringField()
