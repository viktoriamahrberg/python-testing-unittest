import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")
    
    @classmethod
    def tearDownClass(cls):
        print("teadown class")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("teardown")
        self.student = Student("John", "Doe")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


    def test_apply_extension(self):
            old_end_date = self.student.end_date
            self.student.apply_extension(5)
            self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
            """
            The method below is also great!  But keep in mid that  it will
            only be correct if a student has received 1 extenstion.  If 
            they receive a second - it would return false
            self.student.apply_extension(5)
            self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
            """

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "something went wrong with the request")




if __name__ == '__main__':
    unittest.main()