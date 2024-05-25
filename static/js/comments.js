const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
    button.addEventListener("click", (a) => {
    let commentId = a.target.dataset.comment_id;
    let node = document.getElementById(`comment${commentId}`);

    let commentContent = node.textContent;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}/`);
  });
}


const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
  
    let commentId = a.target.dataset.comment_id;
    deleteConfirm.href = `delete_comment/${commentId}`;
    myModal.show();
  });
}