const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const aboutForm = document.getElementById("aboutForm");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (a) => {
    let stories_id = a.target.dataset.stories_id;
    let node = document.getElementById(`stories${stories_id}`);

    let storiesContent = node.innerText;
    commentText.value = storiesContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_story/${stories_id}/`);
  });
}


