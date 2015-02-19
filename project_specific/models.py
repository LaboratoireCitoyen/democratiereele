from django.contrib.comments.managers import CommentManager

from decision.models import Poll
from threadedcomments.models import ThreadedComment


class ProjectCommentManager(CommentManager):
    def get_queryset(self):
        return super(ProjectCommentManager, self).get_queryset(
                ).select_related('user', 'user__account')


class ProjectComment(ThreadedComment, Poll):
    objects = ProjectCommentManager()
