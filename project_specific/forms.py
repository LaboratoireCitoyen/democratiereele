from fluent_comments.forms import FluentCommentForm

from .models import ProjectComment


class ProjectCommentForm(FluentCommentForm):
    def get_comment_model(self):
        return ProjectComment
