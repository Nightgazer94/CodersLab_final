// Waits for the DOM to load, then attaches a click event to the logout link.
// Prevents default link behavior and submits the logout form programmatically.

document.addEventListener('DOMContentLoaded', function() {
  const logoutLink = document.querySelector('.logout-link');
  if (logoutLink) {
    logoutLink.addEventListener('click', function(e) {
      e.preventDefault();
      document.getElementById('logout-form').submit();
    });
  }
});
