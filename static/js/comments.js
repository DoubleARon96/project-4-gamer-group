const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

$(".btn-delete").on("click", function() {
  const commentId = $(this).data("comment_id");
  $.ajax({
      url: `/delete-comment/${commentId}/`,  // URL to your delete_comment view
      method: "POST",
      success: function(response) {
          // Handle success (e.g., remove the comment from the UI)
      },
      error: function(error) {
          // Handle error
      }
  });
});