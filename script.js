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