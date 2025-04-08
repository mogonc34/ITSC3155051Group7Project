/**
 * Toggles the display of an individual team member's bio
 * @param {string} bioId - The ID of the bio section to show or hide
 */
function toggleBio(bioId) {
    const bio = document.getElementById(bioId);
    // Toggle between showing and hiding the bio section
    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
    } else {
        bio.style.display = "none";
    }
}
<<<<<<< HEAD
function toggleMoodboard(moodboard) {
    const moodBoard = document.getElementById(moodboard);
=======
>>>>>>> 65c136efd34c1d35ad876d3a023e406cb6e1e0bf
    // Toggle between showing and hiding the bio section
    if (moodBoard.style.display === "none" || moodBoard.style.display === "") {
        moodBoard.style.display = "block";
    } else {
        moodBoard.style.display = "none";
    }
}

function showSection(sectionId) {
    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");

    // Display the bios section and hide the vision section
    if (sectionId === "bios") {
        biosSection.style.display = "flex";
        visionSection.style.display = "none";
    }
    // Display the vision section and hide the bios section
    else if (sectionId === "vision") {
        biosSection.style.display = "none";
        visionSection.style.display = "grid";
    }
}