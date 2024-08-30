const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const aboutForm = document.getElementById("aboutform");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (event) => {
    let storyId = event.target.dataset.stories_id;
    let node = document.getElementById(`stories${storyId}`);
    let storyContent = node.textContent;
    commentText.value = storyContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_story/${storyId}/`);
  });
}


const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
  
    let stories_id = a.target.dataset.stories_id;
    deleteConfirm.href = `delete_story/${stories_id}/`;
    myModal.show();
  });
}

