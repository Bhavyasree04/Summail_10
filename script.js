function readSummary() {
    const summaryText = document.getElementById("summaryText").innerText;
    const speech = new SpeechSynthesisUtterance(summaryText);
    speechSynthesis.speak(speech);
}

function downloadSummary() {
    const text = document.getElementById("summaryText").innerText;
    const blob = new Blob([text], { type: 'text/plain' });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "summary.txt";
    link.click();
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}