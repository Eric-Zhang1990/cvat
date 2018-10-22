
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import permission_required

from cvat.apps.authentication.decorators import login_required
from cvat.apps.engine.log import slogger
from cvat.apps.engine.models import Task, Job
from cvat.apps.git_anno_repos.models import GitRepos

import json


@login_required
def createRepository(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        tid = data['tid']
        value = data['value']

        db_task = Task.objects.get(pk = tid)

        if GitRepos.objects.filter(pk = db_task).exists():
            raise Exception('Repository record for task already exists. Use update request instead.')

        db_git_repos = GitRepos()
        db_git_repos.task = db_task
        db_git_repos.git_repos = value
        db_git_repos.save()

        return HttpResponse()
    except Exception as e:
        slogger.glob.error("cannot create git record for task #{}".format(tid), exc_info=True)
        return HttpResponseBadRequest(str(e))

@login_required
@permission_required(perm=['engine.view_task', 'engine.change_task'], raise_exception=True)
def updateRepository(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        jid = data['jid']
        value = data['value']

        db_job = Job.objects.select_related('segment__task').get(pk = jid)
        db_task = db_job.segment.task

        if GitRepos.objects.filter(pk = db_task).exists():
            db_repos = GitRepos.objects.select_for_update().get(pk = db_task)
            db_repos.git_repos = value
            db_repos.save()
        else:
            db_repos = GitRepos()
            db_repos.task = db_task
            db_repos.git_repos = value
            db_repos.save()

        return HttpResponse()
    except Exception as e:
        slogger.job[jid].error("cannot delete git record", exc_info=True)
        return HttpResponseBadRequest(str(e))


@login_required
@permission_required(perm=['engine.view_task'], raise_exception=True)
def getRepository(request, jid):
    try:
        db_job = Job.objects.select_related("segment__task").get(pk = jid)
        db_task = db_job.segment.task

        if not GitRepos.objects.filter(pk = db_task).exists():
            return JsonResponse({
                'url': {}
            })

        response = {
            'url': {
                'value': GitRepos.objects.get(pk = db_task).git_repos
            },
            'status': {}
        }

        response['status']['error'] = 'Not implemented'

        return JsonResponse(response)
    except Exception as e:
        slogger.job[jid].error("cannot get git record", exc_info=True)
        return HttpResponseBadRequest(str(e))


@login_required
@permission_required(perm=['engine.view_task', 'engine.change_task'], raise_exception=True)
def deleteRepository(request, jid):
    try:
        db_job = Job.objects.select_related("segment__task").get(pk = jid)
        db_task = db_job.segment.task

        if GitRepos.objects.filter(pk = db_task).exists():
            git_repos = GitRepos.objects.select_for_update().get(pk = db_task)
            git_repos.delete()

        return HttpResponse()
    except Exception as e:
        slogger.job[jid].error("cannot delete git record", exc_info=True)
        return HttpResponseBadRequest(str(e))