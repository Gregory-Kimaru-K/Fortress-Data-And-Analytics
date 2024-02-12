    const themeToggle = document.getElementById("theme-toggle");

    // Add a click event listener to the button
    themeToggle.addEventListener("click", () => {
      // Get the current value of the button
      const currentTheme = themeToggle.textContent;

      // Toggle the theme and the button content
      if (currentTheme === "🌙") {
        document.body.classList.add("dark-mode");
        themeToggle.textContent = "☀️";
      } else {
        document.body.classList.remove("dark-mode");
        themeToggle.textContent = "🌙";
      }
    });