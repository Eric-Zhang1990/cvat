/*
 * Copyright (C) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 */

"use strict";

function updateCreateDialog() {
    $(`
        <tr>
            <td> <label class="regular h2"> Git Repos: </label> </td>
            <td> <input type="text" id="gitAnnoReposInput" class="regular" style="width: 90%", placeholder="github.com/user/repos"/> </td>
        </tr>
    `).insertAfter($("#dashboardBugTrackerInput").parent().parent());

    let originalCreateTaskRequest = createTaskRequest;

    window.createTaskRequest = function(oData, onSuccessRequest, onSuccessCreate, onError, onComplete, onUpdateStatus) {
        let originalOnSuccessCreate = onSuccessCreate;

        onSuccessCreate = (tid) => {
            let value = $('#gitAnnoReposInput').prop('value');

            $.ajax({
                type: 'POST',
                url: '/repository/create',
                data: JSON.stringify({
                    'tid': tid,
                    'value': value,
                }),
                contentType: 'application/json;charset=utf-8',
                error: (data) => {
                    let message = `Warning: Can't create git record for task ${tid}: ${data.responseText}`;
                    showMessage(message);
                }
            });

            originalOnSuccessCreate();
        }

        originalCreateTaskRequest(oData, onSuccessRequest, onSuccessCreate, onError, onComplete, onUpdateStatus);
    }
}

document.addEventListener("DOMContentLoaded", updateCreateDialog);
