from mongoengine import *


class StudentModel(Document):
    meta = {
        'collection': 'account_student'
    }

    uuid = StringField(
        required=True
    )

    student_id = StringField(
        required=True
    )

    name = StringField(
        required=True
    )

    birth = StringField(
        required=True
    )


def get_student_by_uuid(uuid):
    return StudentModel.objects(uuid=uuid).first()