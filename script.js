document.addEventListener('DOMContentLoaded', () => {
    const uploadIcon = document.getElementById('uploadIcon');
    const fileInput = document.getElementById('fileInput');


    var myTextArea = document.getElementsByTagName('textarea')[0];
    var myTextLength = myTextArea.value.length
    var myTextWidth = parseInt(window.getComputedStyle(myTextArea).width);
    var myTextMinLength = 20;
    var myTextMaxWidth = ((parseInt(window.getComputedStyle(document.body).width) / 100) * 80);
    myTextArea.addEventListener('keypress', checkTextLength, false);

    // Add event listener to the cloud icon to trigger the file input
    uploadIcon.addEventListener('click', () => {
        fileInput.click();
    });

    uploadIcon.onchange = ({target}) =>{
        let file = target.files[0];
        if(file){
            let fileName = file.name;
            uploadFile(fileName);
        }

        function uploadFile(name){
            
        }
    }

    // Optional: Show file name when file is selected
    // fileInput.addEventListener('change', (event) => {
    //     const file = event.target.files[0];
    //     if (file) {
    //         alert(`File Selected: ${file.name}`); // Or you can display it somewhere on the page
    //     }
    // });
});
// function resizeInput() {
//     var myTextArea = document.getElementsByTagName('textarea')[0];
//     var myTextLength = myTextArea.value.length
//     var myTextWidth = parseInt(window.getComputedStyle(myTextArea).width);
//     var myTextMinLength = 20;
//     var myTextMaxWidth = ((parseInt(window.getComputedStyle(document.body).width) / 100) * 80); 
// }

function insertText() {
    const inputText = document.getElementById('textInput').value;
    if (inputText.trim() !== "") {
        window.location.href = "formattedText.html"; // Redirect to another page
    } else {
        document.getElementById('textContent').textContent = "No text inserted.";
    }
}

function goToIndexPage() {
    window.location.href = "index.html"; // Redirect to another page
}

function goToFeedbackPage() {
    window.location.href = "index.html"; // Redirect to another page
}
