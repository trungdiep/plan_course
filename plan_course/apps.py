from django.apps import AppConfig


class PlanCourseConfig(AppConfig):
    name = 'plan_course'
    verbose_name = "plan Course"
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'plan_course',
                'relative_path': 'urls',
            },
        }
    }