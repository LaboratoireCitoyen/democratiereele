from django.contrib.comments.managers import CommentManager

from decision.models import Poll
from threadedcomments.models import ThreadedComment


class ProjectComment(ThreadedComment, Poll):
    objects = CommentManager()
