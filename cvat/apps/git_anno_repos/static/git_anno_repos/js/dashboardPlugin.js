"use strict";

function updateCreateDialog() {
    let gitAnnoReposInput = $(`
        <tr>
            <td> <label class="regular h2"> Git Repos: </label> </td>
            <td> <input type="text" id="gitAnnoReposInput" class="regular" style="width: 90%", placeholder="github.com/user/repos"/> </td>
        </tr>
    `).insertAfter($("#dashboardBugTrackerInput").parent().parent());
}

document.addEventListener("DOMContentLoaded", updateCreateDialog);
