// Get modal element
var modal = document.getElementById("popupModal");

// Get open button
var openModalBtn = document.getElementById("openModalBtn");

// Get close button
var closeModalBtn = document.getElementById("closeModalBtn");

// Open modal when the button is clicked
openModalBtn.onclick = function() {
  modal.style.display = "block";
}

// Close modal when the user clicks the "x"
closeModalBtn.onclick = function() {
  modal.style.display = "none";
}

// Close modal if the user clicks anywhere outside of the modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}









/*@Author Shreeya Chugh*/

function validate() {
    document.getElementById('plotSummaryError').textContent = '';
    document.getElementById('genreError').textContent = '';
    document.getElementById('keywordsError').textContent = '';

    
    const plotSummary = document.getElementById('plotSummary').value;
    const genre = document.getElementById('genre').value;
    const keywords = document.getElementById('keywords').value;

    // Validation checks
    let isValid = true;

    if (plotSummary.trim() === '') {
        document.getElementById('plotSummaryError').textContent = 'Plot Summary cannot be empty.';
        isValid = false;
    }

    if (genre.trim() === '') {
        document.getElementById('genreError').textContent = 'Genre cannot be empty.';
        isValid = false;
    }

    if (keywords.trim() === '') {
        document.getElementById('keywordsError').textContent = 'Keywords cannot be empty.';
        isValid = false;
    }

    
    
}