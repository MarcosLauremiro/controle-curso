from rest_framework import serializers
from accounts.models import Account
from accounts.serializers import AccountSerializer
from contents.serializers import ContentSerializer
from courses.models import Course
from students_courses.serializers import StudentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "students_courses",
            "contents",
        ]
        extra_kwargs = {
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = AccountSerializer(read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "students_courses",
            "contents",
        ]


class RegisterCourserSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        depth = 1
        extra_kwargs = {
            "name": {"read_only": True},
        }

    def update(self, instance, validated_data):
        meet_students = []
        do_not_students = []

        for student_course in validated_data["students_courses"]:
            student = student_course["student"]

            account = Account.objects.filter(email=student["email"]).first()

            if account is None:
                do_not_students.append(student["email"])
            else:
                meet_students.append(account)
        if do_not_students:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(do_not_students)}."
                }
            )
        if not self.partial:
            instance.students.add(*meet_students)
            return instance
        return super().update(instance, validated_data)
