#
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT
#

from django.db import models
from cvat.apps.engine.models import Task

class AnnotationFlag(models.Model):
    task = models.OneToOneField(Task, on_delete = models.CASCADE)
    is_being_annotated = models.BooleanField(default = False)
    last_ann_successful = models.BooleanField(default = False)
