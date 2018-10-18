
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.db import models
from cvat.apps.engine.models import Task

class GitRepos(models.Model):
    task = models.ForeignKey(Task, null = False, on_delete = models.CASCADE)
    git_repos = models.CharField(max_length = 2000, null = False)
