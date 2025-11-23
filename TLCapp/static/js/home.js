const video = document.getElementById("intro-video");
  const image = document.getElementById("final-image");
  const wrapper = document.getElementById("intro-wrapper");

  function enterFullscreen(elem) {
    if (elem.requestFullscreen) elem.requestFullscreen();
    else if (elem.webkitRequestFullscreen) elem.webkitRequestFullscreen();
    else if (elem.webkitEnterFullscreen) elem.webkitEnterFullscreen();
  }

  window.addEventListener("load", () => {
    setTimeout(() => enterFullscreen(wrapper), 100);
  });

  video.removeAttribute("loop");

  video.addEventListener("ended", () => {
    video.style.display = "none";
    image.style.display = "block";

    setTimeout(() => {
      wrapper.style.display = "none";
      if (document.fullscreenElement) document.exitFullscreen();
    }, 1000);
  });