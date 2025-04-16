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
function toggleMoodboard(moodboard) {
    const moodBoard = document.getElementById(moodboard);

function toggleMoodboard(moodboard) {
    const moodBoard = document.getElementById(moodboard);


function toggleMoodBoard(moodBoardId) {
    const moodBoard = document.getElementById(moodBoardId);
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