document.addEventListener('DOMContentLoaded', () => {
    const uploadIcon = document.getElementById('uploadIcon');
    const fileInput = document.getElementById('fileInput');
    
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
});
    var myTextArea = document.getElementsByTagName('textarea')[0];
    var myTextLength = myTextArea.value.length
    var myTextWidth = parseInt(window.getComputedStyle(myTextArea).width);
    var myTextMinLength = 20;
    var myTextMaxWidth = ((parseInt(window.getComputedStyle(document.body).width) / 100) * 80);
    myTextArea.addEventListener('keypress', checkTextLength, false);

    // Add event listener to the cloud icon to trigger the file input
    
    function uploadFile(name) {
        console.log("Uploading file:", name);
        
    }

    function animateProgressBar() {
            
            let width = 0;
            let interval = setInterval(() => {
                if (width >= 100) {
                    clearInterval(interval); // Stop animation at 100%
                } else {
                    width += 1; // Increase width by 1% each step
                    progress.style.width = width + "%";
                }
            }, 50); 
            
        }
        
       
 


    

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


