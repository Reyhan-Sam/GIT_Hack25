document.addEventListener('DOMContentLoaded', () => {
    const uploadIcon = document.getElementById('uploadIcon');
    const fileInput = document.getElementById('fileInput');

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
