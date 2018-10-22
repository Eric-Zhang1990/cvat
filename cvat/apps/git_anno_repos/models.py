
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.db import models
from cvat.apps.engine.models import Task

class GitRepos(models.Model):
    task = models.OneToOneField(Task, on_delete = models.CASCADE, primary_key = True)
    git_repos = models.CharField(max_length = 2000)
