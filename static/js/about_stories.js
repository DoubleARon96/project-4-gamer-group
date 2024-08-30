const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("stories${ content.id }");
const aboutForm = document.getElementById("aboutForm");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (a) => {
    let stories_id = a.target.dataset.stories_id;
    let node = document.getElementById(`stories${stories_id}`);
    console.log(node)
    let storiesContent = node.textContent;
    commentText.value = storiesContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_story/${stories_id}/`);
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

