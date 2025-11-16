const container = document.getElementById("video-container");
const video = document.getElementById("introVideo");

if (!localStorage.getItem("introPlayed")) {
    video.play().catch(() => {
        video.muted = true;
        video.play();
    });

    video.addEventListener("ended", () => {
        container.style.display = "none";
        localStorage.setItem("introPlayed", "true");
    });
} else {
    container.style.display = "none";
}