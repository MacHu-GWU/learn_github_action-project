const selector = "input[type='text']";

document.addEventListener("DOMContentLoaded", function(event) {
    // Trigger Read the Docs' search addon instead of the default search
    document.querySelector(selector).addEventListener("click", (e) => {
        const event = new CustomEvent("readthedocs-search-show");
        document.dispatchEvent(event);
    });
});