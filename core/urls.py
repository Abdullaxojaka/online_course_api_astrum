from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register('instructors', InstructorViewSet)
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)

urlpatterns = router.urls
