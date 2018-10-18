
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from cvat.apps.engine.log import slogger
from cvat.apps.engine.models import Task
from cvat.apps.git_anno_repos.models import GitRepos

import json

def createGitRecord(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        tid = data['tid']
        value = data['value']

        db_task = Task.objects.get(pk = tid)
        if not db_task:
            raise Exception("Task with id {} isn't found".format(tid))

        db_git_repos = GitRepos()
        db_git_repos.task = db_task
        db_git_repos.value = value
        db_git_repos.save()

        return HttpResponse()
    except Exception as e:
        slogger.glob.error("cannot create git record for task#{}".format(tid), exc_info=True)
        return HttpResponseBadRequest(str(e))


def deleteGitRecord(request, tid):
    try:
        git_repos = GitRepos.objects.filter(task__id = tid).select_for_update()
        git_repos.delete()

        return HttpResponse()
    except Exception as e:
        slogger.glob.error("cannot delete git record for task#{}".format(tid), exc_info=True)
        return HttpResponseBadRequest(str(e))