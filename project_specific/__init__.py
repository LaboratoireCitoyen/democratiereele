def get_model():
    from .models import ProjectComment
    return ProjectComment


def get_form():
    from .forms import ProjectCommentForm
    return ProjectCommentForm
